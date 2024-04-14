# Binding Energy Calculator
The Binding Energy Calculator is a Python command-line tool designed to compute the total binding energy of a system of objects based on their pairwise distances. It utilises the following model to calculate the binding energy $u$ between pairs of objects distance $r$ apart:

$$
u(r) = 4\epsilon\left(\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right)
$$

where $\epsilon=1.65\times{10}^{-21}$ J and $\sigma=3.41\times10^{-10}$ m.

## Units
For this calculation, $\epsilon$ is in J, $\sigma$ is in m, and $r$ is in m.

# Features
- Calculation of binding energy for a pair of objects.
- Support for inputting distances $r$ directly via command line or from a file.
- Support for specifying values of $\epsilon$ and $\sigma$
- Option to output the total binding energy to a file.

# Installation
## Prerequisites
To install and run the binding energy calculator, Python 3.10 or later needs to be installed on your system.

Use your favourite shell (`bash`, `cmd`, `poweshell` or similar) to install and run the calculator.

## Virtual Environment
For a project requiring the binding energy calculator, it is recommended to create a Python virtual environment, then install the module following the steps below.

To create a virtual environment
```powershell
python -m venv <path\to\virtual\environment>
```
Typically, virtual environments are created a `.venv` folder in your home directory. Then you can activate the virtual environment. In `powershell`, this is done by:
```powershell
PS C:\> <path\to\virtual\environment>\Scripts\Activate.ps1
```

## Steps
To install the calculator:
1. Clone the repository:
    ```bash
    git clone https://github.com/fgalloway/binding_energy_calculator.git
    ```
1. Navigate to the cloned directory:
    ```bash
    cd binding_energy_calculator
    ```

1. Install the package:
    ```bash
    pip install .
    ```

# Usage
The program can be run directly from the command line using your favourite shell. Just remember to activate your Python virtual enviornment as necessary.

There are two modes of operation: inputting pairwise distances directly via command line arguments or reading distances from a file.

## Input distances
```powershell
python -m binding_energy -d DISTANCE1 DISTANCE2 DISTANCE3
```
In this case:
- `DISTANCE#`: Replace `DISTANCE1 DISTANCE2 DISTANCE3` with actual numbers (in appropriate units) representing the distances between pairs of objects.

## File Input
```powershell
python -m binding_energy -f INPUT_FILE
```
- `INPUT_FILE`: Specify the path to a file containing a list of distances (one per line).

## Other options
There are other options for the binding energy calculator:
- `-o OUTPUT_FILE`: path to a file where the resut will be written.

## Help
To display help on all options:
```
python -m bindingenergy --help
```

# Development
To set up a development environment for contributing to the Binding Energy Calculator, follow the installation steps but ensure to install the binding energy calculator as editable:
```powershell
pip install -e .
```

## Running Tests
For the tests, `pytest` is required. To install:
```powershell
pip install pytest
```

Then to run the tests, ensure you are in the project root directory and execute:
```powershell
pytest
```

# Contributing
Contributions to the Binding Energy Calculator are welcome!