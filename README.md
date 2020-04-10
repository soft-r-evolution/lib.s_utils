# lib.s_utils

![Python package](https://github.com/soft-r-evolution/lib.s_utils/workflows/Python%20package/badge.svg)

This library is used to provided some common operations for most of the projects. Such as:

* Get safely a key in a dictionary

## Installation

### Installing virtual-env

On ubuntu

```
sudo apt install vitualenv
```

### Create environment

```
virtualenv --python=python3 venv
```

## Activate environment

```
source venv/bin/activate
```

## Install locally

```
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install flake8
pip install pytest pytest-cov
```

## Run the linter

```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Run the tests

```
pytest --cov=s_utils --cov-report=html tests
xdg-open htmlcov/index.html
```
