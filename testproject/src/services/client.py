
import requests
import logging

from requests import Session
from typing import Any


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