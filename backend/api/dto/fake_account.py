from dataclasses import dataclass

from django.conf import settings

from api.dto import GroupDTO


@dataclass
class FakeAccount:
    username: str
    password: str
    cookies: list[dict]
    proxy_ip: str
    groups: list[GroupDTO]

    new_cookies: list[dict] | None = None

    @property
    def proxy_url(self) -> str:
        return f"http://{settings.PROXY_USERNAME}:{settings.PROXY_PASSWORD}@{self.proxy_ip}"
