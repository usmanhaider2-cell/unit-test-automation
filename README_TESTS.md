\# Unit Test Automation: python-slugify



\## Setup

&#x20;   python -m venv venv

&#x20;   venv\\Scripts\\activate

&#x20;   pip install -e .

&#x20;   pip install pytest pytest-xdist pytest-order pytest-html



\## Run

&#x20;   pytest                      # all tests

&#x20;   pytest -m smoke             # smoke suite

&#x20;   pytest -m boundary          # BVA suite

&#x20;   pytest -m regression        # regression suite

&#x20;   pytest -m data\_driven       # CSV data-driven suite

&#x20;   pytest -n 4                 # parallel (4 workers)

&#x20;   pytest --html=report.html --self-contained-html



\## Structure

\- tests/test\_slugify\_main.py: slugify() and \_modern\_truncate()

\- tests/test\_smart\_truncate.py: smart\_truncate()

\- tests/test\_csv\_driven.py: CSV data-driven tests

\- tests/data/test\_data.csv: test data

\- docs/test\_design\_notes.md: ECP/BVA notes

\- docs/test\_cases.xlsx: Excel test cases

