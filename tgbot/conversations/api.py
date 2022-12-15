import os
import httpx

from pydantic import BaseModel


class Siren(BaseModel):
    uid: int
    name: str
    district_id: int
    type: str
    own: str | None
    engineer: str | None
    date: str | None
    condition: str | None
    ident: str
    ip: str
    mask: str | None
    gateway: str | None
    adress: str | None
    geo: str | None
    comment: str | None
    photo: str | None
    disabled: int | None


class District(BaseModel):
    uid: int
    name: str


class DistrictClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/districts'

    def get_for_district(self, uid: int) -> list[District]:
        response = httpx.get(url=f'{self.url}/{uid}/sirens')
        response.raise_for_status()
        sirens = response.json()

        return [Siren(**siren) for siren in sirens]

    def get_by_name(self, name: str) -> list[District]:
        response = httpx.get(url=f'{self.url}/?name={name}')
        response.raise_for_status()
        districts = response.json()

        return [District(**district) for district in districts]

    def get_by_id(self, uid: int) -> District:
        response = httpx.get(url=f'{self.url}/{uid}')
        response.raise_for_status()
        district = response.json()

        return District(**district)


class SirenClient:
    def __init__(self, url: str) -> None:
        self.url = f'{url}/sirens'

    def get_siren(self, name: str) -> list[Siren]:
        response = httpx.get(url=f'{self.url}/?name={name}')
        response.raise_for_status()
        sirens = response.json()

        return [Siren(**siren) for siren in sirens]


class ApiClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self.districts = DistrictClient(url)
        self.sirens = SirenClient(url)


client = ApiClient(os.environ['API_URL'])
