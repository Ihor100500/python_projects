from pydantic import BaseModel
from typing import Any


class GlossaryEntry(BaseModel):
    term: Any
    definition: Any


class WeatherResponse(BaseModel):
    glossary: list[GlossaryEntry]
