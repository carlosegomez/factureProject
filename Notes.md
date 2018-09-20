#Pytest

##Modules
- `pytest-profiling`
- `pytest-flake8`
- `pytest-cov`
- `pytest-mock`

##Options
- passed tests: `-v`
- print: `-s`
- debug: `--pdb`
- last x performing: `--duration=x`
- code analyzer: `--pylint` or `--flake8`
- code coverage: `--cov --cov-report=html` 
- On pytest.ini: `addopts` add options

##Profiling tests
- Only data: `pytest <pytest_file.py> --profile`
- Graph: `pytest <pytest_file.py> --profile-svg`

#Profiling
- Memory: `python -m memory_profiler <file.py>`
- Memory (other): `vmprof`
- Plot memory profile: `mprof run <file.py>`, `mprof plot`    
- Time: install `line_profiler`, then `kernprof -l <file.py>`
- Code: `flake8`, `pylint`
- Organize code: `isort`

#Documentation
- `sphinx`

#Tools
- `EditorConfig`: share config between editors
- `virtualenv`, `virualfish`: manage virtual env
- `pipdevtree`: package dependency tree

#Binary
- egg
- wheels

