import pytest
import requests
import logging

from src.models.weather import WeatherResponse
from typing import Any
from services.client import Client

log = logging.getLogger(__name__)


@pytest.fixture
def weather_http(nice_client: Client) -> Client:
    """
    Fixture to provide a specialized HTTP client for weather-related endpoints.
    """

    class WeatherClient(Client):

        def __init__(self, client: Client):
            self.client = client
            self.client.base_url = "https://api.weather.gov"

        def _inject(self, kwargs: dict[str, Any]) -> dict[str, Any]:
            headers = kwargs.pop("headers", {})
            headers["User-Agent"] = "chrome"
            kwargs["headers"] = headers
            return kwargs

        def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
            response = self.client.get(endpoint, **self._inject(kwargs))
            if not isinstance(response, requests.Response):
                raise TypeError(f"Expected requests.Response, got {type(response).__name__}")
            return response

        def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
            response = self.client.post(endpoint, **self._inject(kwargs))
            if not isinstance(response, requests.Response):
                raise TypeError(f"Expected requests.Response, got {type(response).__name__}")
            return response

        def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
            response = self.client.put(endpoint, **self._inject(kwargs))
            if not isinstance(response, requests.Response):
                raise TypeError(f"Expected requests.Response, got {type(response).__name__}")
            return response

        def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
            response = self.client.put(endpoint, **self._inject(kwargs))
            if not isinstance(response, requests.Response):
                raise TypeError(f"Expected requests.Response, got {type(response).__name__}")
            return response

    return WeatherClient(nice_client)


@pytest.mark.api
def test_weather_gov_glossary_endpoint(weather_http: Client) -> None:
    """
    Test the /glossary endpoint of the weather.gov API.
    """
    log.info("Testing /glossary endpoint of the weather.gov API")
    response = weather_http.get("/glossary")
    assert (
        response.status_code == 200
    ), f"Expected status code 200, but was {response.status_code}"
    data = response.json()
    parsed = WeatherResponse.model_validate(data)
    assert parsed.glossary[4].term == "500 hPa"
    # print(f"The first fucking test: {data['glossary'][4].get('definition')}")
    # assert isinstance(data, dict), "Response data should be a dictionary"
