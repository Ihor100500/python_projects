# Project Setup

## 1. Clone & create venv
git clone <repo-url>
cd <repo>
python3 -m venv .venv
source .venv/bin/activate

## 2. Install tools
pip install -r requirements.txt
pip install black isort mypy pytest
pip install pytest-pythonpath

## 3. VS Code setup
- Select interpreter: Cmd+Shift+P → "Python: Select Interpreter" → .venv/bin/python
- Install extensions: Python, Pylance, Black Formatter, isort, Mypy Type Checker
- Copy `.vscode/settings.json` from repo

## 4. Type checking
mypy src/
