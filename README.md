# dckr
[![Build Executables](https://github.com/RoyAtanu/dckr/actions/workflows/build_executables.yml/badge.svg)](https://github.com/RoyAtanu/dckr/actions/workflows/build_executables.yml)

A Docker CLI alternative with shortcuts and added functionalities
***
## What is different in **dckr** from Docker CLI
* ### **Search** function
    Docker artifacts (containers/images) can be searched by partially entering its ID or name

    ![Search functionality](documentation/images/screenshot_search.png?raw=true)
* ### **Shortcuts** for arguments
    You can use shortcuts in *dckr* instead of typing full argument names (e.g. **c** instead of **container**). Check documentation for more info.

    ![List functionality](documentation/images/screenshot_list.png?raw=true)
* ### **Cleanup** arguments
    *dckr* provides shortcuts to bulk cleanup of docker artifacts by running single command
* ### **Colored** console output
    *dckr* prints colored texts in console for highlighting key information (e.g. # of items, status etc.)

****
## How to build the executable from source
### Prerequisites
You should have following packages installed -
* Python 3
* pip3
* pyinstaller
### Instructions
1. Go to the root folder of repo
2. [Optional] Setup virtual env for python if not done already

    ``` python3 -m venv .venv ```

3. Run the following command to install the dependencies 

    ``` pip3 install -r requirements.txt ```

4. Run the following command to build the executable

    ``` pyinstaller --onefile --console dckr/dckr.py ```
***




