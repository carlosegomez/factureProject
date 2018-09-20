# Facture Project
Example for Advanced Python formation. 

##Pytest

##Options
- passed tests: -v
- print: -s
- debug: --pdb
- last x performing: --duration=x
- On pytest.ini: `addopts` add options

###Profiling tests
- Only data: `pytest <pytest_file.py> --profile`
- Graph: `pytest <pytest_file.py> --profile-svg`

##Profiling
- Memory: `python -m memory_profiler <file.py>`
- Memory (other): `vmprof`
- Plot memory profile: `mprof run <file.py>`, `mprof plot`    
- Time: install `line_profiler`, then `kernprof -l <file.py>`
