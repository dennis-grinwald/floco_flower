// Copyright 2025 Flower Labs GmbH. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// =============================================================================

import {
  type ChatCompletionMessageParam,
  CreateMLCEngine,
  type InitProgressReport,
  type MLCEngineInterface,
} from '@mlc-ai/web-llm';
import {
  ChatResponseResult,
  FailureCode,
  Message,
  Progress,
  Result,
  StreamEvent,
  Tool,
} from '../typing';
import { BaseEngine } from './engine';
import { getEngineModelName } from './common';

async function runQuery(
  engine: MLCEngineInterface,
  messages: Message[],
  stream?: boolean,
  onStreamEvent?: (event: StreamEvent) => void,
  temperature?: number,
  maxTokens?: number
) {
  if (stream && onStreamEvent) {
    const reply = await engine.chat.completions.create({
      stream: true,
      messages: messages as ChatCompletionMessageParam[],
      temperature,
      max_tokens: maxTokens,
    });
    for await (const chunk of reply) {
      onStreamEvent({ chunk: chunk.choices[0]?.delta?.content ?? '' });
    }
    return await engine.getMessage();
  } else {
    const reply = await engine.chat.completions.create({
      messages: messages as ChatCompletionMessageParam[],
      temperature,
      max_tokens: maxTokens,
    });
    return reply.choices[0].message.content ?? '';
  }
}

export class WebllmEngine extends BaseEngine {
  #loadedEngines: Record<string, MLCEngineInterface> = {};

  async chat(
    messages: Message[],
    model: string,
    temperature?: number,
    maxCompletionTokens?: number,
    stream?: boolean,
    onStreamEvent?: (event: StreamEvent) => void,
    _tools?: Tool[]
  ): Promise<ChatResponseResult> {
    const modelNameRes = await getEngineModelName(model, 'webllm');
    if (!modelNameRes.ok) {
      return {
        ok: false,
        failure: {
          code: FailureCode.UnsupportedModelError,
          description: `The model ${model} is not supported on the WebLLM engine.`,
        },
      };
    }
    try {
      if (!(model in this.#loadedEngines)) {
        this.#loadedEngines.model = await CreateMLCEngine(
          modelNameRes.value,
          {},
          {
            context_window_size: 2048,
          }
        );
      }
      const result = await runQuery(
        this.#loadedEngines.model,
        messages,
        stream,
        onStreamEvent,
        temperature,
        maxCompletionTokens
      );
      return {
        ok: true,
        message: {
          role: 'assistant',
          content: result,
        },
      };
    } catch (error) {
      return {
        ok: false,
        failure: {
          code: FailureCode.LocalEngineChatError,
          description: `WebLLM engine failed with: ${String(error)}`,
        },
      };
    }
  }

  async fetchModel(model: string, callback: (progress: Progress) => void): Promise<Result<void>> {
    const modelNameRes = await getEngineModelName(model, 'webllm');
    if (!modelNameRes.ok) {
      return {
        ok: false,
        failure: {
          code: FailureCode.UnsupportedModelError,
          description: `The model ${model} is not supported on the WebLLM engine.`,
        },
      };
    }
    try {
      if (!(model in this.#loadedEngines)) {
        this.#loadedEngines.model = await CreateMLCEngine(
          modelNameRes.value,
          {
            initProgressCallback: (report: InitProgressReport) => {
              callback({ percentage: report.progress, description: report.text });
            },
          },
          {
            context_window_size: 2048,
          }
        );
      }
      return { ok: true, value: undefined };
    } catch (error) {
      return {
        ok: false,
        failure: { code: FailureCode.LocalEngineFetchError, description: String(error) },
      };
    }
  }

  async isSupported(model: string): Promise<boolean> {
    const modelNameRes = await getEngineModelName(model, 'webllm');
    return modelNameRes.ok;
  }
}
