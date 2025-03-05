#!/bin/bash

# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# Generating the docs, rename and move the files such that the meet the convention used in Flower.
# Note that it involves two runs of sphinx-build that are necessary.
# The first run generates the .rst files (and the html files that are discarded)
# The second time it is run after the files are renamed and moved to the correct place. It generates the final htmls.

set -e

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )"  >/dev/null 2>&1 && pwd )"/../docs

# Remove the old docs from source/ref-api
REF_API_DIR="source/ref-api"
if [[ -d "$REF_API_DIR" ]]; then

  echo "Removing ${REF_API_DIR}"
  rm -r ${REF_API_DIR}
fi

# Remove the old html files
if [[ -d build ]]; then
  echo "Removing ./build"
  rm -r build
fi

# Docs generation: Generate new rst files
# It starts at the __init__ in the main directory and recursively generated the documentation for the
# specified classes/modules/packages specified in __all__.
# Note if a package cannot be reach via the recursive traversal, even if it has __all__, it won't be documented.
echo "Generating the docs based on only the functionality given in the __all__."
sphinx-build -M html source build

# Remove the autogenerated source files after the build
if find source/ref-api -maxdepth 1 -name "*.rst" | grep -q .; then
    find source/ref-api -maxdepth 1 -name "*.rst" -exec rm {} +
fi
