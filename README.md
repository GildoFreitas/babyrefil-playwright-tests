# Babyrefil Playwright E2E tests

## About this project

**Babyrefil** is a **subscription** web product focused on **baby-care goods** (a refill / recurring-delivery style model). The user journey spans marketing pages, plans, subscription signup, address, checkout, and payment—close to a real e-commerce flow and a strong fit for E2E practice.

That style of application was used in a **Playwright MCP test automation course by Fernando Papito called "Playwright MCP: Seu Copiloto em Testes"**. The system context and learning baseline come from that material.

To **level up my Playwright skills** and work through a real workflow using **MCP** (Model Context Protocol) and Playwright MCP, I went beyond the course exercises and built a **full project**: an organized test suite, reusable helpers, test-case documentation, a GitHub Actions CI pipeline (multi-browser, failure artifacts, HTML report), and this README so anyone can install and run it.

I used **Playwright MCP** as a copilot during the implementation of the automated tests and **ChatGPT** while designing and refining the test cases. Nothing was blindly copy-pasted: every generated test, helper, and test case was carefully reviewed, understood, refactored, and improved before becoming part of the project. This workflow significantly improved my technical skills by forcing me to analyze selectors, assertions, test stability, architecture decisions, and overall test design instead of treating AI-generated output as final. It also strengthened my ability to read, critique, and maintain automation code in a more structured and professional way.

The suite uses **Playwright** with **pytest** (`pytest-playwright`). Tests hit a **deployed** environment; you choose the target with **`BASE_URL`** (see below).

## Requirements

- **Python 3.12+** (same major version as CI)
- **Git**

## Install

### 1. Clone and enter the project

```bash
git clone https://github.com/GildoFreitas/babyrefil-playwright-tests.git
cd babyrefil-playwright-tests
```

### 2. Create a virtual environment (recommended)

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

Install the engines you need. **Chromium** is enough for a quick start:

```bash
playwright install chromium
```

To match CI (Chromium, Firefox, WebKit), install all three:

```bash
playwright install chromium firefox webkit
```

On **Linux**, system libraries are often required for headed or full browser support:

```bash
playwright install-deps chromium
# or, for all installed browsers:
playwright install-deps
```

On Windows and macOS, `playwright install …` is usually sufficient.

### 5. Configure `BASE_URL`

Tests read **`BASE_URL`** from the environment. The app URL must **not** end with a trailing slash.

Create a `.env` file in the project root (this file is gitignored):

```env
BASE_URL=https://babyrefil.vercel.app
```

You can use another staging or preview URL as long as it serves the same flows the tests expect.

## Run tests

With the virtual environment active and `.env` present:

```bash
pytest
```

### Useful options

| Goal | Command |
|------|---------|
| One file | `pytest tests/navigation/test_ct004_plans_navigation.py` |
| One test | `pytest tests/navigation/test_ct004_plans_navigation.py::test_name` |
| Specific browser (default is Chromium) | `pytest --browser=firefox` or `pytest --browser=webkit` |
| HTML report (optional) | `pytest --html=pytest-report.html --self-contained-html` |
| Shorter traceback | `pytest --tb=short` (also set in `pytest.ini`) |

`pytest.ini` sets `testpaths = tests` and default `addopts` (`-v --tb=short`).

### Traces, video, and screenshots (local)

Same flags as CI (see `.github/workflows/ci.yml`):

```bash
pytest --output=test-results --tracing=on --video=on --screenshot=on
```

Use `retain-on-failure` / `only-on-failure` instead of `on` if you only want artifacts when something fails.

Open a trace:

```bash
playwright show-trace path/to/trace.zip
```

## CI (GitHub Actions)

On push/PR to `main` or `master`, workflows run the suite in a matrix (**Chromium**, **Firefox**, **WebKit**) against `BASE_URL` defined in the workflow. On failure, artifacts include a **self-contained HTML report** and Playwright outputs under `test-results/`.

To change the URL in CI, edit `BASE_URL` in `.github/workflows/ci.yml` or set a repository variable and reference it in the workflow.

## Project layout

- `tests/` — test modules by area (`navigation`, `checkout`, `subscription`, `address`, `payment`)
- `utils/` — shared helpers (navigation, env, steps)
- `docs/` — test design / CT references

## Troubleshooting

- **`RuntimeError: Set BASE_URL in your .env file`** — Add `BASE_URL=…` to `.env` or export it in the shell before running `pytest`.
- **Browser not found / launch errors** — Run `playwright install` (and on Linux, `playwright install-deps` if needed).
- **Timeouts or flakes** — Network or the remote app may be slow; check `BASE_URL` and app availability.
