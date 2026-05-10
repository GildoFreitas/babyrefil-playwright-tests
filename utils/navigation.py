"""Navigation helpers: homepage and subscribe URL assertions."""

import re

from playwright.sync_api import Page, expect

from utils.env import get_base_url


def expect_subscribe_url(page: Page) -> None:
    """Assert current URL is the subscribe page (``/subscribe``) for ``BASE_URL``."""
    base = get_base_url()
    expect(page).to_have_url(re.compile(re.escape(base) + r"/subscribe/?$"))


def open_homepage(page: Page):
    """``page.goto(BASE_URL)`` and assert the home URL (root path)."""
    base = get_base_url()

    page.goto(base)

    expect(page).to_have_url(
        re.compile(re.escape(base) + r"/?$")
    )

    return base