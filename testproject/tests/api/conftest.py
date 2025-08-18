import os
import pytest
import requests
import logging
from typing import Any
from typing import Generator as generator
from pathlib import Path
from requests import Session
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


log = logging.getLogger(__name__)


class Client:
    def __init__(self, session: Session, base_url: str):
        self.session = session
        self.base_url = base_url

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        log.info(f"GET request to {self.base_url}{endpoint} with params: {kwargs}")
        response: requests.Response = self.session.get(
            f"{self.base_url}{endpoint}", **kwargs
        )
        log.info(f"Response status code: {response.status_code}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response content: {response.text[:300]}...")  # Log first 300 chars
        return response

    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        log.info(f"POST request to {self.base_url}{endpoint} with data: {kwargs}")
        response: requests.Response = self.session.post(
            f"{self.base_url}{endpoint}", **kwargs
        )
        log.info(f"Response status code: {response.status_code}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response content: {response.text[:300]}...")  # Log first 300 chars
        return response

    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
        log.info(f"PUT request to {self.base_url}{endpoint} with data: {kwargs}")
        response: requests.Response = self.session.put(
            f"{self.base_url}{endpoint}", **kwargs
        )
        log.info(f"Response status code: {response.status_code}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response content: {response.text[:300]}...")  # Log first 300 chars
        return response

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        log.info(f"DELETE request to {self.base_url}{endpoint} with params: {kwargs}")
        response: requests.Response = self.session.delete(
            f"{self.base_url}{endpoint}", **kwargs
        )
        log.info(f"Response status code: {response.status_code}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response content: {response.text[:300]}...")  # Log first 300 chars
        return response


def _build_session(timeout: float = 0.0, retries: int = 3) -> Session:
    session = Session()
    retry = Retry(
        total=retries,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"Accept": "application/json"})
    session._default_timeout = timeout  # type: ignore[attr-defined]
    return session


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "http://localhost:8000")


# @pytest.fixture(scope="session")
# def auth_token(base_url: str) -> Any:
#     try:
#         resp = requests.post(
#             f"{base_url}/login", json={"username": "test", "password": "test"}
#         )
#         resp.raise_for_status()
#         token = resp.json().get("token")
#         if not token:
#             pytest.fail("Response received, but not token found")
#         return token
#     except requests.RequestException as e:
#         return "No authentication token provided"


@pytest.fixture(scope="session")
def http(base_url: str) -> generator[Client, None, None]:
    session = _build_session()
    # if not auth_token:
    #     raise RuntimeError("Authentication token is required for HTTP client.")
    # session.headers.update({"Authorization": f"Bearer {auth_token}"})
    yield Client(session, base_url)
    session.close()


@pytest.fixture
def sample_text(tmp_path: Path) -> Path:
    p = tmp_path / "sample.txt"
    p.write_text("line1\nline2\nline3\n", encoding="utf-8")
    return p
