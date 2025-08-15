import pytest
import requests


from src.models.weather import WeatherResponse
from typing import Any
from conftest import Client


@pytest.fixture
def weather_http(http: Client) -> Client:
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
            return self.client.get(endpoint, **self._inject(kwargs))

        def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
            return self.client.post(endpoint, **self._inject(kwargs))

        def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
            return self.client.put(endpoint, **self._inject(kwargs))

        def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
            return self.client.delete(endpoint, **self._inject(kwargs))

    return WeatherClient(http)


def test_weather_gov_glossary_endpoint(weather_http: Client) -> None:
    """
    Test the /glossary endpoint of the weather.gov API.
    """
    response = weather_http.get("/glossary")
    assert (
        response.status_code == 200
    ), f"Expected status code 200, but was {response.status_code}"
    data = response.json()
    parsed = WeatherResponse.model_validate(data)
    assert parsed.glossary[4].term == "500 hPa"
    # print(f"The first fucking test: {data['glossary'][4].get('definition')}")
    # assert isinstance(data, dict), "Response data should be a dictionary"
