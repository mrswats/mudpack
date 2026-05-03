# Mudpack

Sending UDP requests is simple. Let's make it even easier.

Mudpack is a simple UDP client for python.

## Usage

As a regular client:

```python
import mudpack

mudpack.Client("localhost", 1000)
mudpack.send("foo")
```

As a context manager:
```python
import mudpack


with mudpack.Client("localhost", 1000) as client:
    client.send("foo")
```

or use the method directly:
```python
import mudpack


mudpack.send("localhost", 1000, "foo")
```

## Virtual Environment

Create a virtual Environment

```
virtualenv .venv -p pytthon 3.14
source .venv/bin/activate
```

## Tests

Using pytest for Tests

```
python -m pytest
```

## Formatting and Linting

Using pre-commit for linting and formatting

```
pre-commit install
pre-commit run --all-files
```
