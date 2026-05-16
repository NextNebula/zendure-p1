from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Report:
    timestamp: int
    device_id: str
    a_apparent_power: int
    b_apparent_power: int
    c_apparent_power: int
    total_power: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Report":
        return cls(
            timestamp=data["timestamp"],
            device_id=data["deviceId"],
            a_apparent_power=data["a_aprt_power"],
            b_apparent_power=data["b_aprt_power"],
            c_apparent_power=data["c_aprt_power"],
            total_power=data["total_power"],
        )
