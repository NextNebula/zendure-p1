from types import TracebackType

import aiohttp

from .exceptions import (
    ZendureP1ConnectionError,
    ZendureP1ResponseError,
    ZendureP1TimeoutError,
)
from .models import Report

_REPORT_PATH = "/properties/report"


class ZendureP1Client:
    def __init__(self, host: str, *, timeout: float = 10.0) -> None:
        self._base_url = f"http://{host}"
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._session: aiohttp.ClientSession | None = None
        self._close_session: bool = False

    async def __aenter__(self) -> "ZendureP1Client":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        if self._session is not None and self._close_session:
            await self._session.close()
            self._session = None
            self._close_session = False

    async def get_report(self) -> Report:
        session = self._get_session()
        try:
            async with session.get(f"{self._base_url}{_REPORT_PATH}") as response:
                response.raise_for_status()
                data = await response.json(content_type=None)
                return Report.from_dict(data)
        except TimeoutError as e:
            raise ZendureP1TimeoutError from e
        except aiohttp.ClientConnectionError as e:
            raise ZendureP1ConnectionError from e
        except aiohttp.ClientResponseError as e:
            raise ZendureP1ResponseError(e.message) from e

    def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            self._session = aiohttp.ClientSession(timeout=self._timeout)
            self._close_session = True
        return self._session
