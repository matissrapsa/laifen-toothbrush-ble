import asyncio
import logging
from homeassistant.components.sensor import SensorEntity
from bleak import BleakClient

_LOGGER = logging.getLogger(__name__)

# Bluetooth UUIDs
NOTIFY_UUID = "0000ff02-0000-1000-8000-00805f9b34fb"
ENABLE_NOTIFY_UUID = "00002902-0000-1000-8000-00805f9b34fb"
ENABLE_NOTIFY_VALUE = bytearray([0x01, 0x00])

class LaifenToothbrushSensor(SensorEntity):
    """Representation of the Laifen Toothbrush."""

    def __init__(self, device_address):
        self._device_address = device_address
        self._client = None
        self._state = None
        self._attributes = {}

    async def async_added_to_hass(self):
        """Run when entity is added to HA."""
        await self.connect_to_device()

    async def connect_to_device(self):
        """Connect to the toothbrush via BLE."""
        try:
            self._client = BleakClient(self._device_address)
            await self._client.connect()

            # Enable notifications
            await self._client.write_gatt_char(ENABLE_NOTIFY_UUID, ENABLE_NOTIFY_VALUE)

            # Subscribe to notifications
            await self._client.start_notify(NOTIFY_UUID, self.notification_handler)

        except Exception as e:
            _LOGGER.error(f"Failed to connect: {e}")

    def notification_handler(self, sender, data):
        """Handle notifications from the toothbrush."""
        _LOGGER.info(f"Received data: {data.hex()}")

        if data[:4] == bytearray([0xAA, 0x0A, 0x02, 0x15]):
            self.parse_toothbrush_data(data)

    def parse_toothbrush_data(self, data):
        """Parse the received notification data."""
        brushing_timer = (data[20] << 8) | data[21]  # Correctly derive from two bytes

        self._attributes = {
            "mode": data[4],  
            "mode_1_vibration_strength": data[5],
            "mode_1_oscillation_range": data[6],
            "mode_1_oscillation_speed": data[7],
            "mode_2_vibration_strength": data[8],
            "mode_2_oscillation_range": data[9],
            "mode_2_oscillation_speed": data[10],
            "mode_3_vibration_strength": data[11],
            "mode_3_oscillation_range": data[12],
            "mode_3_oscillation_speed": data[13],
            "mode_4_vibration_strength": data[14],  
            "mode_4_oscillation_range": data[15],
            "mode_4_oscillation_speed": data[16],
            "airplane_mode": data[17],
            "battery_percentage": data[18],
            "30_sec_reminder": data[19],
            "brushing_timer_seconds": brushing_timer,  # Correctly derived from data[20] and data[21]
            "high_frequency_mode": data[22],
            "power_control": data[23],
            "emergency_shutdown": data[24],
            "checksum": data[25],
        }
        self._state = self._attributes["battery_percentage"]
        self.async_write_ha_state()

    @property
    def name(self):
        return "Laifen Toothbrush"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes
