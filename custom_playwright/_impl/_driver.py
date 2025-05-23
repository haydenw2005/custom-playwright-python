# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import os
import sys
from pathlib import Path
from typing import Tuple

import custom_playwright
from custom_playwright._repo_version import version


def compute_driver_executable() -> Tuple[str, str]:
    driver_path = Path(inspect.getfile(custom_playwright)).parent / "driver"
    # driver_path = Path(__file__).resolve().parent.parent.parent / "driver"
    cli_path = str(driver_path / "package" / "cli.js")
    if sys.platform == "win32":
        return (str(driver_path / "node.exe"), cli_path)
    return (os.getenv("PLAYWRIGHT_NODEJS_PATH", str(driver_path / "node")), cli_path)
    # cache_dir = Path(os.getenv("CUSTOM_PLAYWRIGHT_CACHE_DIR", Path.home() / ".cache/custom-playwright"))
    # driver = cache_dir / "driver" / "node"
    # if not driver.exists():
    #     raise FileNotFoundError("Custom Playwright driver not found. Run `custom-playwright install`.")
    # return driver



def get_driver_env() -> dict:
    env = os.environ.copy()
    env["PW_LANG_NAME"] = "python"
    env["PW_LANG_NAME_VERSION"] = f"{sys.version_info.major}.{sys.version_info.minor}"
    env["PW_CLI_DISPLAY_VERSION"] = version
    return env
