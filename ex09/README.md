# ft_package

A simple Python package that provides a function to count how many times an item appears in a list.

## Features

- Count the occurrences of an item in a list.
- Installable using `pip`.
- Distributed as a source archive (`.tar.gz`) and a wheel (`.whl`).

## Project Structure

```text
ex09/
├── ft_package/
│   ├── __init__.py
│   └── count_in_list.py
├── pyproject.toml
├── README.md
├── LICENSE
└── dist/
    ├── ft_package-0.0.1.tar.gz
    └── ft_package-0.0.1-py3-none-any.whl
```

## Requirements

- Python 3.10 or newer.
- `pip`.
- The `build` package to generate the distributions.

## Installation and Build

### 1. Install the build tool

```bash
python -m pip install build
```

This installs the `build` tool, which prepares the project for distribution. The `pip` command installs packages, while `build` generates the files needed to distribute your own package.

### 2. Build the package

Run the command from the directory containing `pyproject.toml`:

```bash
python -m build
```

The build tool reads the project configuration and generates two distribution files in the `dist/` directory:

- `ft_package-0.0.1.tar.gz`: the source distribution.
- `ft_package-0.0.1-py3-none-any.whl`: the wheel distribution, ready for installation.

### 3. Install the package

You can install the package using either distribution.

Using the source archive:

```bash
python -m pip install ./dist/ft_package-0.0.1.tar.gz
```

Or using the wheel:

```bash
python -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

The wheel is generally the more direct option because it is already built for installation.

### 4. Verify the installation

Check that the package appears among the installed packages:

```bash
python -m pip list
```

Display the package metadata:

```bash
python -m pip show -v ft_package
```

The metadata includes information such as the package name, version, description, license, and installation location.

### 5. Use the package

Create a Python script and import the function directly from the package:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Expected output:

```text
2
0
```

## Function

### `count_in_list(lst, item)`

Returns the number of times `item` appears in `lst`.

**Parameters:**
- `lst`: the list to search.
- `item`: the element to count.

**Returns:** an integer representing the number of occurrences.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
