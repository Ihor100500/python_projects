from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Page


def test_open_google_page(page: "Page") -> None:
    page.goto("/")
    assert page.title() == "Google"
