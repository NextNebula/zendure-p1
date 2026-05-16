import pytest

from zendure_p1.models import Report

REPORT_DATA = {
    "timestamp": 1715000000,
    "deviceId": "abc123",
    "a_aprt_power": 100,
    "b_aprt_power": 200,
    "c_aprt_power": 300,
    "total_power": 600,
}


def test_from_dict_maps_all_fields() -> None:
    report = Report.from_dict(REPORT_DATA)
    assert report.timestamp == REPORT_DATA["timestamp"]
    assert report.device_id == REPORT_DATA["deviceId"]
    assert report.a_apparent_power == REPORT_DATA["a_aprt_power"]
    assert report.b_apparent_power == REPORT_DATA["b_aprt_power"]
    assert report.c_apparent_power == REPORT_DATA["c_aprt_power"]
    assert report.total_power == REPORT_DATA["total_power"]


def test_from_dict_missing_key_raises() -> None:
    data = {k: v for k, v in REPORT_DATA.items() if k != "timestamp"}
    with pytest.raises(KeyError):
        Report.from_dict(data)


def test_report_is_immutable() -> None:
    report = Report.from_dict(REPORT_DATA)
    with pytest.raises(AttributeError):
        report.total_power = 999  # type: ignore[misc]
