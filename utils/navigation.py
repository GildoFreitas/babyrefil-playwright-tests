import re

from playwright.sync_api import Page, expect

from utils.env import get_base_url


def expect_subscribe_url(page: Page) -> None:
    """Assere que a URL atual é a página de assinatura (/subscribe), respeitando BASE_URL."""
    base = get_base_url()
    expect(page).to_have_url(re.compile(re.escape(base) + r"/subscribe/?$"))


def open_homepage(page: Page):
    base = get_base_url()

    page.goto(base)

    expect(page).to_have_url(
        re.compile(re.escape(base) + r"/?$")
    )

    return base