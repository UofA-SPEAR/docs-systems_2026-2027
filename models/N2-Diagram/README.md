# N2-Diagram

OpenMDAO model of the rover that tracks the system budgets and draws an N2
diagram of how the subsystems connect.

| Budget  | Rate units   | Total  |
|---------|--------------|--------|
| mass    |              | kg     |
| power   | W            | Wh     |
| storage | MB/s         | GB     |
| compute | GPU %, CPU % | RAM GB |
| network | Mbps         |        |

## Run

From the repo root:

```bash
source .venv/bin/activate
cd data/N2-Diagram
python3 N2.py
```

Or open `N2.py` in VS Code and press Run (the workspace `.vscode/settings.json`
runs it from this folder with the `.venv` Python).

First time setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Output

- Budget table in the terminal (total, left, GOOD / BAD)
- `n2_diagram.html`: the N2 diagram, opens in the browser
- `N2_out/`: OpenMDAO reports

Outputs are regenerated every run and are in `.gitignore`.

## Files

| File            | What it is                                    | Who edits it |
|-----------------|-----------------------------------------------|--------------|
| `N2.py`         | builds the model, budgets, summary, runs it   | no one (only for a new subsystem or budget) |
| `mechanical.py` | chassis, drive, arm                           | mechanical   |
| `science.py`    | science payload                               | science      |
| `electrical.py` | battery                                       | electrical   |
| `software.py`   | jetson, radios, cameras                       | software     |
| `specs.csv`     | every value (path, value, units)              | everyone, their own rows |

Values that are `-0.0` still need to be filled in.

See the wiki page for how to read the output and how to add parts.