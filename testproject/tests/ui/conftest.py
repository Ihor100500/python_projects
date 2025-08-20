import pytest

from playwright.sync_api import sync_playwright
from typing import TYPE_CHECKING
from typing import Generator as generator

if TYPE_CHECKING:
    from _pytest.config import Config
    from _pytest.config.argparsing import Parser
    from playwright.sync_api import Browser, BrowserContext, Page, Playwright


def pytest_addoption(parser: "Parser") -> None:
    # parser.addoption(
    #     "--browser", action="store", default="chromium", help="Browser to use"
    # )
    parser.addoption(
        "--headless", action="store_true", help="Run browsers in headless mode"
    )
    parser.addoption(
        "--app-base-url",
        action="store",
        default="https://google.com",
        help="Base URL for tests",
    )


@pytest.fixture(scope="session")
def browser_name(pytestconfig: "Config") -> str:
    return str(pytestconfig.getoption("--browser"))


@pytest.fixture(scope="session")
def headless(pytestconfig: "Config") -> bool:
    return bool(pytestconfig.getoption("--headless"))


@pytest.fixture(scope="session")
def base_url(pytestconfig: "Config") -> str:
    return str(pytestconfig.getoption("--app-base-url"))


@pytest.fixture(scope="session")
def slow_mo(pytestconfig: "Config") -> int:
    return int(pytestconfig.getoption("--slowmo") or 0)  # type: ignore


@pytest.fixture(scope="session")
def playwright_instance() -> (
    generator["Playwright", None, None]
):  # return PlaywrightContextManager
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(
    playwright_instance: "Playwright",
    browser_name: str,
    headless: bool,
    slow_mo: int,
) -> generator["Browser", None, None]:
    browser_type = getattr(playwright_instance, browser_name)
    browser = browser_type.launch(headless=headless, slow_mo=slow_mo)
    yield browser
    browser.close()


@pytest.fixture()
def context(
    browser: "Browser", base_url: str
) -> generator["BrowserContext", None, None]:
    context = browser.new_context(base_url=base_url, record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path="traces/trace.zip")
    context.close()


@pytest.fixture()
def page(context: "BrowserContext") -> generator["Page", None, None]:
    page = context.new_page()
    yield page
    page.close()
