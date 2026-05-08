from playwright.sync_api import Page

def test_homepage(page: Page):
    page.goto("https://babyrefil.vercel.app")

    assert page.title() != ""