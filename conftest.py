"""Shared pytest hooks (CI + local)."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config) -> None:
    # pytest-html / Playwright write under test-results; ensure it exists early
    Path("test-results").mkdir(parents=True, exist_ok=True)
