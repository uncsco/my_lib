## Installation - (using Poetry)

- See `init.sh` file:

```sh
python3 -m poetry remove numpy
```

```sh
python3 -m poetry add --dev pytest
python3 -m poetry add --dev mypy

python3 -m poetry add pydantic
```

----

```
pytest.ini
```

### Running Python progs (in the SHELL)

```sh
# PyTEST
python3 -m pytest
# MyPy
python3 -m mypy my_lib
```

----

## Template for a Lib - (SETUP.py)

https://github.com/simonw/python-lib

```
- setup.py

- my_lib
  - __init__.py
  
```

- setup.py: https://github.com/simonw/python-lib/blob/main/%7B%7Bcookiecutter.hyphenated%7D%7D/setup.py