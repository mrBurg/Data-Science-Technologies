# links

- https://www.geeksforgeeks.org/python-if-else/
- https://www.geeksforgeeks.org/python-while-loop/
- https://www.geeksforgeeks.org/python-nested-loops/
- https://www.learnpython.dev/02-introduction-to-python/110-control-statements-looping/40-break-continue/
- https://www.learnpython.dev/02-introduction-to-python/110-control-statements-looping/40-break-continue/

### Environment

1. python -m venv venv #/path/to/new/environment
2. .\venv\Scripts\activate (powershell) ./venv/Scripts/activate (Git bash)
3. deactivate
4. pip install [module name]

### Generate requirements

1. pip freeze > requirements.txt
2. pip install -r requirements.txt

### Ignore error

Inline # pylint: disable-msg=C0209 or disable-msg=E0401, C0413, E0611 or disable=R0913, W0221
In flie # pylint: disable=E1101, W0237, R0913, R0902, C0301, R0913, R1705, R0911
Global in config --disable=C0209

# type: ignore

### Add to dependencies

Ubuntu: pip freeze | grep -v "pkg==\|pkg===\|pkg~=" > '.\requirements.txt'
Windows: pip freeze | findstr /V "pkg== pkg=== pkg~=" > '.\requirements.txt'

echo "requests==2.25.1" >> '.\requirements.txt'
echo "numpy" >> '.\requirements.txt'
echo "Flask>=2.0.0,<3.0.0" >> '.\requirements.txt'

### Import from different folder

import sys

1:---------
import pathlib

LIBS_PATH = pathlib.Path(**file**).parent.joinpath("../").resolve()
sys.path.append(str(LIBS_PATH))

---

2:---------
import os

PARENT_DIR = os.path.dirname(os.path.abspath(**file**))
LIBS_DIR = os.path.dirname(PARENT_DIR)
sys.path.append(LIBS_DIR)

---

3:---------
import pathlib

LIBS_PATH = pathlib.Path(**file**).parent.joinpath("../").resolve()
sys.path.append(str(LIBS_PATH))

В корне проекта создать файл pyrightconfig.jso
{
"python.autoComplete.extraPaths": ["./libs"]
}

---

import libs.figure_factory as figure_factory

print(figure_factory)

index file **init**.py

""" Module """

print("Index")

### ImportError

В корне проекта создать файл pyrightconfig.jso
{
"reportMissingImports": false
}

# KeyError \*\*kwargs

matrix = kwargs.get("matrix", default_value)
matrix = kwargs["matrix"] if "matrix" in kwargs else default_value
matrix = kwargs.pop("matrix", default_value)

{
"reportMissingImports": true,
"exclude": ["**/node_modules", "**/__pycache__"]
}
