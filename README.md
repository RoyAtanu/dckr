# dckr
A Docker CLI alternative with shortcuts and added functionalities

[![Build](https://github.com/RoyAtanu/dckr/actions/workflows/build_executables.yml/badge.svg?branch=main)](https://github.com/RoyAtanu/dckr/actions/workflows/build_executables.yml)
****
## How to build the executable from source
### Prerequisites
You should have following packages installed -
* python 3
* pip3
* pyinstaller
### Instructions
1. Go to the root folder of repo
2. Run the following command to run the dependencies 
``` pip3 install -r requirements.txt ```
3. Run the following command to build the executable
``` pyinstaller --onefile --console dckr/dckr.py ```
***




