import aiohttp
import pytest
from aioresponses import aioresponses

from zendure_p1 import (
    Report,
    ZendureP1Client,
    ZendureP1ConnectionError,
    ZendureP1ResponseError,
    ZendureP1TimeoutError,
)

REPORT_PAYLOAD = {
    "timestamp": 1715000000,
    "deviceId": "abc123",
    "a_aprt_power": 100,
    "b_aprt_power": 200,
    "c_aprt_power": 300,
    "total_power": 600,
}

HOST = "192.168.1.1"
REPORT_URL = f"http://{HOST}/properties/report"


async def test_get_report_returns_report() -> None:
    with aioresponses() as mock:
        mock.get(REPORT_URL, payload=REPORT_PAYLOAD)
        async with ZendureP1Client(HOST) as client:
            report = await client.get_report()

    assert isinstance(report, Report)
    assert report.total_power == REPORT_PAYLOAD["total_power"]


async def test_get_report_maps_all_fields() -> None:
    with aioresponses() as mock:
        mock.get(REPORT_URL, payload=REPORT_PAYLOAD)
        async with ZendureP1Client(HOST) as client:
            report = await client.get_report()

    assert report.timestamp == REPORT_PAYLOAD["timestamp"]
    assert report.device_id == REPORT_PAYLOAD["deviceId"]
    assert report.a_apparent_power == REPORT_PAYLOAD["a_aprt_power"]
    assert report.b_apparent_power == REPORT_PAYLOAD["b_aprt_power"]
    assert report.c_apparent_power == REPORT_PAYLOAD["c_aprt_power"]


async def test_get_report_without_context_manager() -> None:
    with aioresponses() as mock:
        mock.get(REPORT_URL, payload=REPORT_PAYLOAD)
        client = ZendureP1Client(HOST)
        report = await client.get_report()
        await client.close()

    assert isinstance(report, Report)


async def test_get_report_raises_on_http_error() -> None:
    with aioresponses() as mock:
        mock.get(REPORT_URL, status=500)
        async with ZendureP1Client(HOST) as client:
            with pytest.raises(ZendureP1ResponseError):
                await client.get_report()


async def test_get_report_raises_on_connection_error() -> None:
    with aioresponses() as mock:
        mock.get(REPORT_URL, exception=aiohttp.ClientConnectionError())
        async with ZendureP1Client(HOST) as client:
            with pytest.raises(ZendureP1ConnectionError):
                await client.get_report()


async def test_get_report_raises_on_timeout() -> None:
    with aioresponses() as mock:
        mock.get(REPORT_URL, exception=TimeoutError())
        async with ZendureP1Client(HOST) as client:
            with pytest.raises(ZendureP1TimeoutError):
                await client.get_report()
