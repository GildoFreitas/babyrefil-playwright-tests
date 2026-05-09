from playwright.sync_api import Page, expect
import re

from utils.env import get_base_url


def open_homepage(page: Page):
    base = get_base_url()

    page.goto(base)

    expect(page).to_have_url(
        re.compile(re.escape(base) + r"/?$")
    )

    return base