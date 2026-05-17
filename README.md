# zendure-p1

Async Python library for communicating with Zendure P1 Smart Meter.

## Installation

```bash
pip install zendure-p1
```

## Usage

```python
import asyncio
from zendure_p1 import ZendureP1Client

async def main():
    async with ZendureP1Client("192.168.1.100") as client:
        report = await client.get_report()
        print(f"Total power: {report.total_power} W")
        print(f"Phase A: {report.a_apparent_power} VA")
        print(f"Phase B: {report.b_apparent_power} VA")
        print(f"Phase C: {report.c_apparent_power} VA")

asyncio.run(main())
```

### Error handling

```python
from zendure_p1 import ZendureP1Client
from zendure_p1.exceptions import (
    ZendureP1ConnectionError,
    ZendureP1TimeoutError,
    ZendureP1ResponseError,
)

async with ZendureP1Client("192.168.1.100", timeout=5.0) as client:
    try:
        report = await client.get_report()
    except ZendureP1ConnectionError:
        print("Could not connect to the device")
    except ZendureP1TimeoutError:
        print("Request timed out")
    except ZendureP1ResponseError as e:
        print(f"Device returned an error: {e}")
```

## Model

### `Report`

Returned by `client.get_report()`.

| Field | Type | Description |
|---|---|---|
| `timestamp` | `int` | Unix timestamp of the measurement |
| `device_id` | `str` | Unique device identifier |
| `a_apparent_power` | `int` | Apparent power on phase A in VA |
| `b_apparent_power` | `int` | Apparent power on phase B in VA |
| `c_apparent_power` | `int` | Apparent power on phase C in VA |
| `total_power` | `int` | Total active power across all phases in W |

## License

MIT
