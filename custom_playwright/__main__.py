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

import subprocess
import sys

from custom_playwright._impl import _driver

def main():
    try:
        driver_executable, driver_cli  = _driver.compute_driver_executable()
        print(f"✅ custom-playwright is installed.\nDriver: {driver_executable}")
        completed_process = subprocess.run(
                [driver_executable, driver_cli, *sys.argv[1:]], env=_driver.get_driver_env()
            )
        sys.exit(completed_process.returncode)
    except FileNotFoundError as e:
        print(f"❌ Driver missing: {e}")
        print("If you're seeing this in dev, re-run: python setup.py bdist_wheel")



if __name__ == "__main__":
    main()
