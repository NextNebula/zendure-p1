import pytest

from zendure_p1 import (
    ZendureP1ConnectionError,
    ZendureP1Error,
    ZendureP1ResponseError,
    ZendureP1TimeoutError,
)


def test_connection_error_is_zendure_error() -> None:
    assert issubclass(ZendureP1ConnectionError, ZendureP1Error)


def test_timeout_error_is_zendure_error() -> None:
    assert issubclass(ZendureP1TimeoutError, ZendureP1Error)


def test_response_error_is_zendure_error() -> None:
    assert issubclass(ZendureP1ResponseError, ZendureP1Error)


def test_zendure_error_is_exception() -> None:
    assert issubclass(ZendureP1Error, Exception)


def test_connection_error_can_be_caught_as_base() -> None:
    with pytest.raises(ZendureP1Error):
        raise ZendureP1ConnectionError


def test_timeout_error_can_be_caught_as_base() -> None:
    with pytest.raises(ZendureP1Error):
        raise ZendureP1TimeoutError


def test_response_error_can_be_caught_as_base() -> None:
    with pytest.raises(ZendureP1Error):
        raise ZendureP1ResponseError("Internal Server Error")


def test_response_error_preserves_message() -> None:
    with pytest.raises(ZendureP1ResponseError, match="Internal Server Error"):
        raise ZendureP1ResponseError("Internal Server Error")
