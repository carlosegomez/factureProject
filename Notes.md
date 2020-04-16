# Modules
- `pylint` > code analizer
- `intertools`
- `coverage` > test coverate analysis
- `factory_boy` + `faker` > fake data for tests 
- `pdb` > debug
- `weasyprint` > easy formatted print
- `psutils` > process analysis
- `cookiecutter` > template for Python packages
- `twine` > upload Python package to pypi
- `pipenv` > create a venv for package in dev

# Documentation
- `sphinx`

# Tools
- `EditorConfig`: share config between editors
- `virtualenv`, `virualfish`: manage virtual env
- `pipdevtree`: print package dependency tree
- `beautifulsoup`: to parse files
- `zeal`: find docs to be offline 
- `slack`: notifications
- `restic`: HD backup to cloud
- `ansible`: dev conf backup 
- `devpi`: pypi server
- `KeePassXC`: Password manager
- `Numba`: code optimizer

# Binary
- egg
- wheels

# Concepts
- Metaclass
- Decorators
- Mixing
- Descriptors

# Test: Pytest

## Modules
- `pytest-profiling`
- `pytest-flake8`
- `pytest-cov`
- `pytest-mock`
- `watchdog` > execute auto-test when code is changed
- `pytest-runner` > execute auto-test when test are changed
- `pytest-deamon` > execute auto-test when test are changed

## Options
- passed tests: `-v`
- print: `-s`
- debug: `--pdb`
- last x performing: `--duration=x`
- code analyzer: `--pylint` or `--flake8`
- code coverage: `--cov --cov-report=html` 
- On pytest.ini: `addopts` add options

## Profiling tests
- Only data: `pytest <pytest_file.py> --profile`
- Graph: `pytest <pytest_file.py> --profile-svg`

# Profiling
- Memory: `python -m memory_profiler <file.py>`
- Memory (other): `vmprof`
- Plot memory profile: `mprof run <file.py>`, `mprof plot`    
- Time: install `line_profiler`, then `kernprof -l <file.py>`
- Code: `flake8`, `pylint`
- Organize code: `isort`

# Pages
- http://devguide.python.org
- http://pymotw.com

# Books
- Head First Design Patterns
- Head-First Python: Paul Barry
- Python Testing with pytest: Brian Okken
- The Hacker's Guide to Scaling Python: Julien Danjou
