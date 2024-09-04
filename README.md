# [Boiler Plate] Making Python Executable with Pyinstaller

### Introduction
This is a boiler plate project to illustrate the process of building executable for a python project. In this project, a very specific 

### Install Pyinstaller
```shell
pip install -U pyinstaller
```

### General Usage Guide
1. Build streamlit executable to encapsulate all the packages and environments ([jump to section](#general-usage-guide))
2. Once built, one can start building the app in .py formats based on "sample_app.py"
3. "imported_packages.py" needs to be updated and "run_app.spec" needs to be rerun to include any new packages in the project

### Building Streamlit Executable
[Tutorial Link](https://ploomber.io/blog/streamlit_exe/)

_Explanations_

1. First time bootstraping the project
```shell
pyinstaller --onefile --additional-hooks-dir=./hooks run_app.py --clean
```
In this case, "run_app.py" is the main script (the script that will be executed to start a runtime session), and there will be additional hook files stored in /hooks. For more information about the hooks, see [this link](https://pyinstaller.org/en/stable/hooks.html#module-PyInstaller.utils.hooks)

2. After the bootstraping and reconfigure the .spec file
```shell
pyinstaller run_app.spec --clean
```

3. 
```python
"""run_app.py"""
import imported_packages

import streamlit

import streamlit.web.cli as stcli
import os, sys


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("../sample_app.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
```
In the above script, the .exe file will look for the python code "../sample_app.py" under the grandparent folder of itself.
4. Only the packages associated with the script that is compiled will be compiled. Thus, in order to utilize other packages in your app ("sample_app.py" in this sample project), one needs to include packages at the activation file ("run_app.py" here).
```python
"""imported_packages.py"""
import serial
```
