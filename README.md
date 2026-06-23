## pod-devops (demo)

Prosty projekt w Pythonie pod zajęcia z GitHub Actions:

- buduje paczkę (`wheel` + `sdist`) do katalogu `dist/`
- uruchamia testy `pytest`
- uruchamia lint/format check przez `ruff`
- workflow wrzuca artefakty z builda jako `dist/`

### Szybki start (lokalnie)

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
python -m pip install -e ".[dev]"

ruff check .
pytest -q
python -m build
```

### CLI

```bash
pod-devops-demo --help
pod-devops-demo greet "Ala"
```
