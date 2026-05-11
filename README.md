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
        print(f"Phase A: {report.a_apparent_power} W")
        print(f"Phase B: {report.b_apparent_power} W")
        print(f"Phase C: {report.c_apparent_power} W")

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

Returned by `client.get_report()`. All power values are in watts.

| Field | Type | Description |
|---|---|---|
| `timestamp` | `int` | Unix timestamp of the measurement |
| `a_apparent_power` | `int` | Apparent power on phase A |
| `b_apparent_power` | `int` | Apparent power on phase B |
| `c_apparent_power` | `int` | Apparent power on phase C |
| `total_power` | `int` | Total power across all phases |

## License

MIT
