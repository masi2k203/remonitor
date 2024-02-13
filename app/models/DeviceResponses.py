from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: str
    nickname: str
    superuser: bool

class NewestEventsValue(BaseModel):
    created_at: str 
    val: float

class DeviceResponse(BaseModel):
    # Device Id
    id: str
    # Serial Number
    serial_number: str
    # firmware version
    firmware_version: str
    # name
    name: str

    # Bluetooth MAC Address
    bt_mac_address: str
    # MAC Address
    mac_address: str

    # created at
    created_at: str
    # updated at
    updated_at: str

    # temperature offset
    temperature_offset: float
    # humidity offset
    humidity_offset: float

    # users
    users: Optional[list[User]]

    # newest_events
    newest_events: dict[str, NewestEventsValue]

    # online
    online: bool

    @property
    def temperature(self) -> float:
        """A property that returns the temperature

        It gets the temperature from the newest_events dictionary with the key "te",
        and adds the temperature_offset attribute to it,
        and returns the final temperature.

        Returns:
            float: The temperature

        Raises:
            ValueError: If the newest_events dictionary does not have the key "te"
        """
        base_temperature = self.newest_events.get("te")

        if base_temperature is None:
            raise ValueError("Temperature is no set.")

        return base_temperature.val + self.temperature_offset

    @property
    def humidity(self) -> float:
        """A property that returns the humidity

        It gets the humidity from the newest_events dictionary with the key "hu",
        and adds the humidity_offset attribute to it,
        and returns the final humidity.

        Returns:
            float: The humidity

        Raises:
            ValueError: If the newest_events dictionary does not have the key "hu"
        """
        base_humidity = self.newest_events.get("hu")

        if base_humidity is None:
            raise ValueError("Humidity is no set.")

        return base_humidity.val + self.humidity_offset

    @property
    def luminance(self) -> float:
        """A property that returns the luminance

        It gets the luminance from the newest_events dictionary with the key "il",
        and returns the final luminance.

        Returns:
            float: The luminance

        Raises:
            ValueError: If the newest_events dictionary does not have the key "il"
        """
        base_luminance = self.newest_events.get("il")

        if base_luminance is None:
            raise ValueError("Luminance is no set.")

        return base_luminance.val

    @property
    def temperature_timestamp(self) -> datetime:
        """A property that returns the timestamp of the temperature data

        It gets the timestamp from the newest_events dictionary with the key "te",
        and returns the final timestamp in UTC.

        Returns:
            datetime: The timestamp of the temperature data

        Raises:
            ValueError: If the newest_events dictionary does not have the key "te"
        """
        base_temperature = self.newest_events.get("te")

        if base_temperature is None:
            raise ValueError("Temperature is no set.")

        return base_temperature.created_at

    @property
    def humidity_timestamp(self) -> datetime:
        """A property that returns the timestamp of the humidity data

        It gets the timestamp from the newest_events dictionary with the key "hu",
        and returns the final timestamp in UTC.

        Returns:
            datetime: The timestamp of the humidity data

        Raises:
            ValueError: If the newest_events dictionary does not have the key "hu"
        """
        base_humidity = self.newest_events.get("hu")

        if base_humidity is None:
            raise ValueError("Humidity is no set.")

        return base_humidity.created_at

    @property
    def luminance_timestamp(self) -> datetime:
        """A property that returns the timestamp of the luminance data

        It gets the timestamp from the newest_events dictionary with the key "il",
        and returns the final timestamp in UTC.

        Returns:
            datetime: The timestamp of the luminance data

        Raises:
            ValueError: If the newest_events dictionary does not have the key "il"
        """
        base_luminance = self.newest_events.get("il")

        if base_luminance is None:
            raise ValueError("Luminance is no set.")

        return base_luminance.created_at



# sample
data = [
    {
        "name": "リビング",
        "id": "1ab038b5-78b1-4b07-a5e5-a7100acc2544",
        "created_at": "2024-02-12T11:02:41Z",
        "updated_at": "2024-02-13T12:47:21Z",
        "mac_address": "58:bf:25:fd:10:60",
        "bt_mac_address": "58:bf:25:fd:10:62",
        "serial_number": "1W322070001824",
        "firmware_version": "Remo/1.14.2",
        "temperature_offset": 0,
        "humidity_offset": 0,
        "users": [
            {
                "id": "9c6bba49-a77b-472b-bc42-3c1e2cdfe708",
                "nickname": "島田基希",
                "superuser": True
            }
        ],
        "newest_events": {
            "hu": {
                "val": 45,
                "created_at": "2024-02-13T13:14:46Z"
            },
            "il": {
                "val": 200,
                "created_at": "2024-02-13T13:18:50Z"
            },
            "mo": {
                "val": 1,
                "created_at": "2024-02-13T13:19:14Z"
            },
            "te": {
                "val": 18.7,
                "created_at": "2024-02-13T13:39:48Z"
            }
        },
        "online": True
    }
]

a = DeviceResponse(**data[0])
print(f"日時: {a.temperature_timestamp} 温度: {a.temperature}")
print(f"日時: {a.humidity_timestamp} 湿度: {a.humidity}")
print(f"日時: {a.luminance_timestamp} 照度レベル: {a.luminance}")