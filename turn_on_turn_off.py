import asyncio
from bleak import BleakClient

# Replace this with your toothbrush MAC address
TOOTHBRUSH_MAC = "C0:00:00:01:68:05"

# UUIDs
CHARACTERISTIC_UUID = "0000ff02-0000-1000-8000-00805f9b34fb"  # Main control handle
NOTIFY_DESCRIPTOR_UUID = "00002902-0000-1000-8000-00805f9b34fb"  # Descriptor for notifications

# Commands
ENABLE_NOTIFICATIONS = bytearray([0x01, 0x00])
CMD_ON = bytearray.fromhex("AA0F010101A4")
CMD_OFF = bytearray.fromhex("AA0F010100A5")


async def connect_and_control():
    """Connects to the Laifen toothbrush and sends BLE commands."""
    async with BleakClient(TOOTHBRUSH_MAC) as client:
        print("Connected to toothbrush!")

        # Get all services to find the correct descriptor
        for service in client.services:
            for char in service.characteristics:
                if char.uuid == CHARACTERISTIC_UUID:
                    for desc in char.descriptors:
                        print(f"Found Descriptor: {desc.uuid}")
                        if desc.uuid == NOTIFY_DESCRIPTOR_UUID:
                            print("Enabling notifications...")
                            await client.write_gatt_descriptor(desc.handle, ENABLE_NOTIFICATIONS)
                            await asyncio.sleep(2)

        # Step 2: Send ON command to `0x0027` (HANDLE_CONTROL)
        print("Turning toothbrush ON...")
        await client.write_gatt_char(CHARACTERISTIC_UUID, CMD_ON)
        await asyncio.sleep(2)

        # Step 3: Send OFF command to `0x0027` (HANDLE_CONTROL)
        print("Turning toothbrush OFF...")
        await client.write_gatt_char(CHARACTERISTIC_UUID, CMD_OFF)
        await asyncio.sleep(2)

        print("Done!")


# Run the asyncio function
asyncio.run(connect_and_control())
