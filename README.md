# Laifen Toothbrush Bluetooth Control
Reverse-engineering Laifen toothbrush BLE (Bluetooth Low Energy) commands with end goal of creating Home Assistant integration.

## Overview
Laifen toothbrushes use Bluetooth Low Energy (BLE) for communication. This repository documents how to read commands from the toothbrush, including:

## Device Details
- **Model:** LFTB01-P-6805
- **BLE UUIDs:**
  - **Service UUID:** `0000ff01-0000-1000-8000-00805f9b34fb`
  - **Control Characteristic UUID:** `0000ff02-0000-1000-8000-00805f9b34fb`
- **Supports:** `READ, WRITE, NOTIFY`

## 0xFF02 Characteristics breakdown, the whole settings are stored in a single HEX string
Properties: NOTIFY, READ, WRITE, WRITE NO RESPONSE Value: (Ox) AA-0A-02-15-03-05-05-05-04-06-06-06-06-06-0B-06-06-00-63-01-00-78-01-00-00-A3

- AA - 
- 0A - 
- 02 - 
- 15 - 
- 03 - Current mode selected (00 for mode 1, 01 for mode 2, 02 for mode 3, 03 for mode 4) mode 4 only available if high frequency mode is enabled
- 05 - Mode 1 Vibration strenght
- 05 - Mode 1 Oscillation range (01 to 0A)
- 05 - Mode 1 Oscillation speed (01 to 0A)
- 04 - Mode 2 Vibration strenght
- 06 - Mode 2 Oscillation range (01 to 0A)
- 06 - Mode 2 Oscillation speed (01 to 0A)
- 06 - Mode 3 Vibration strenght
- 06 - Mode 3 Oscillation range (01 to 0A)
- 06 - Mode 3 Oscillation speed (01 to 0A)
- 0B - Mode 4 Vibration strenght (01 to 14)
- 06 - Mode 4 Oscillation range (01 to 0A)
- 06 - Mode 4 Oscillation speed (01 to 0A)
- 00 - Airplane mode On or off (01, 00)
- 63 - Maybe battery percentage another toothbrush had it at 36 (00-64)
- 01 - 30 sec reminder On or off (01, 00)
- 00 - 
- 78 - Brushing timer 78=2min, 96=2,5min
- 01 - High freqency mode, mode 4 enabled On or off (01, 00)
- 00 - Power control On or off (01, 00)
- 00 - Emergency shutdown On or off (01, 00)
- A3 - Checksum or padding

## Data collected using nRF Connect app and 2 diferent toothbrushes
