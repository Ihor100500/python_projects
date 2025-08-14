import os
import pytest
import requests
from typing import Any
from pathlib import Path
from requests import Session
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def _build_session(timeout: float = 10.0, retries: int = 3) -> Session:
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


@pytest.fixture(scope="session")
def auth_token() -> Any:
    url = base_url()
    resp = requests.post(f"{url}/login", json={"username": "test", "password": "test"})
    resp.raise_for_status()
    return resp.json().get("token")


@pytest.fixture(scope="session")
def http(base_url: str, auth_token: Any):
    session = _build_session()
    if auth_token:
        session.headers.update({"Authorization": f"Bearer {auth_token}"})

    class Client:
        def __init__(self, session: Session, base_url: str):
            self.session = session
            self.base_url = base_url

        def get(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

        def post(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.post(f"{self.base_url}{endpoint}", **kwargs)

        def put(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.put(f"{self.base_url}{endpoint}", **kwargs)

        def delete(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

        yield Client(session, base_url)
        session.close()


@pytest.fixture
def sample_text(tmp_path: Path) -> Path:
    p = tmp_path / "sample.txt"
    p.write_text("line1\nline2\nline3\n", encoding="utf-8")
    return p
