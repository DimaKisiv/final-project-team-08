# Assistant from Team-08

## Installable Package

### Build
In the root directory of the project, run the following command to build the package.
This will create a dist directory with the package.
```bash
python3 -m build
```

### Install (without push to PyPI)
To install the package, run the following command in the root directory of the project.
This will install the package from the dist directory to site-packages.
```bash
pip install --find-links ./dist assistant_team_08
```

### Run
Get the bin directory path first, usually package install executable in same directory as python executable.
```bash
which python3 | sed 's/\/bin\/python3/\/bin/'`
```
Then run the assistant
```bash
$PATH_TO_EXECUTABLE/assistant_team_08
```

### Uninstall
```bash
pip uninstall assistant_team_08
```
