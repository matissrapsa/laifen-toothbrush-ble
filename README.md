# Laifen Toothbrush Bluetooth Control
Reverse-engineering Laifen toothbrush BLE (Bluetooth Low Energy) commands with end goal of creating Home Assistant integration.

## Overview
Laifen toothbrushes use Bluetooth Low Energy (BLE) for communication. This repository documents how to read commands from the toothbrush, including:

## 0xFF02 Characteristics breakdown, the whole settings are stored in a single HEX string
Properties: NOTIFY, READ, WRITE, WRITE NO RESPONSE Value: (Ox) AA-0A-02-15-03-05-05-05-04-06-06-06-06-06-0B-06-06-00-63-01-00-78-01-00-00-A3

- AA - 
- 0A - 
- 02 - 
- 15 - 
- 03 - Current mode selected (00 for mode 1, 01 for mode 2, 02 for mode 3, 03 for mode 4) mode 4 only available if high frequency mode is enabled
- 05 - Mode 1 Vibration strenght (01 to 0A)
- 05 - Mode 1 Oscillation range (01 to 0A)
- 05 - Mode 1 Oscillation speed (01 to 0A)
- 04 - Mode 2 Vibration strenght (01 to 0A)
- 06 - Mode 2 Oscillation range (01 to 0A)
- 06 - Mode 2 Oscillation speed (01 to 0A)
- 06 - Mode 3 Vibration strenght (01 to 0A)
- 06 - Mode 3 Oscillation range (01 to 0A)
- 06 - Mode 3 Oscillation speed (01 to 0A)
- 0B - Mode 4 Vibration strenght (0B to 14)
- 06 - Mode 4 Oscillation range (01 to 0A)
- 06 - Mode 4 Oscillation speed (01 to 0A)
- 00 - Airplane mode On or off (01, 00)
- 63 - Battery percentage (01 to 64)
- 01 - 30 sec reminder On or off (01, 00)
- 00 - Overflow for timer if set to 5 min then this will be 01 and next byte 2C
- 78 - Brushing timer 78=2min, 96=2,5min
- 01 - High freqency mode, mode 4 enabled On or off (01, 00)
- 00 - Power control On or off (01, 00)
- 00 - Emergency shutdown On or off (01, 00)
- A3 - Checksum or padding

## Writing data
- chanel 0x0028 write 0x0001 to enable chanel 0x0027
- chanel 0x0027 data can be written
- AA0F010101A4 Turn On
- AA0F010100A5 Turn Off
- AA04010400020505A9 Select mode 1 (with settings 02, 05, 05)
- AA04010401040606AE Select mode 2 (with settings 04, 06, 06)
- AA04010402070707AE Select mode 3 (with settings 07, 07, 07)
- AA04010403140A0ABC Select mode 4 (with max settings 14, 0A, 0A)
- AA0E010101A5 Enable mode 4 / High frequency
- AA0E010100A4 Disable mode 4 / High frequency
- AA0B010100A1 Disable 30 sec reminder
- AA0B010101A0 Enable 30 sec reminder
- AA07010100AD Disable Aeroplane mode
- AA07010101AC Enable Aeroplane mode
- AA14010100BE Emergency mode Off
- AA14010101BF Emergency mode On
- AA06010101AD Go limp before calibration
- AA06010103AF Calibration mode
- Timer modes
- AA050102012C81 5 min
- AA050102010EA3 4,5 min
- AA05010200f05C 4 min
- AA05010200d27E 3,5 min
- AA05010200B418 3 min
- AA05010200963A 2,5 min
- AA0501020078D4 2 min
- AA050102005AF6 1,5 min
- AA050102003C90 1 min

## Chanel's
- handle = 0x0029, uuid = 00002901-0000-1000-8000-00805f9b34fb
- handle = 0x002c, uuid = 00002901-0000-1000-8000-00805f9b34fb
- handle = 0x0028, uuid = 00002902-0000-1000-8000-00805f9b34fb
- handle = 0x0027, uuid = 0000ff02-0000-1000-8000-00805f9b34fb
- handle = 0x0001, uuid = 00002800-0000-1000-8000-00805f9b34fb
- handle = 0x000a, uuid = 00002a05-0000-1000-8000-00805f9b34fb
- handle = 0x000b, uuid = 00002902-0000-1000-8000-00805f9b34fb
- handle = 0x000c, uuid = 00002800-0000-1000-8000-00805f9b34fb
- handle = 0x001e, uuid = 00002a50-0000-1000-8000-00805f9b34fb
- handle = 0x001f, uuid = 00002800-0000-1000-8000-00805f9b34fb
- handle = 0x0023, uuid = 5833ff03-9b8b-5191-6142-22a4536ef123
- handle = 0x0024, uuid = 00002902-0000-1000-8000-00805f9b34fb
- handle = 0x0025, uuid = 00002800-0000-1000-8000-00805f9b34fb
- handle = 0x002b, uuid = 0000ff10-0000-1000-8000-00805f9b34fb

