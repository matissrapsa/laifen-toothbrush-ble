# Laifen Toothbrush Bluetooth Control
Reverse-engineering Laifen toothbrush BLE (Bluetooth Low Energy) commands with end goal of creating Home Assistant integration.

## Overview
Laifen toothbrushes use Bluetooth Low Energy (BLE) for communication. This repository documents how to send commands to control the toothbrush, including:
- Turning ON/OFF
- Adjusting settings for each mode
- Changing brushing modes
- Toggling settings

## Device Details
- **Model:** LFTB01-P-6805
- **BLE UUIDs:**
  - **Service UUID:** `0000ff01-0000-1000-8000-00805f9b34fb`
  - **Control Characteristic UUID:** `0000ff02-0000-1000-8000-00805f9b34fb`
- **Supports:** `READ, WRITE, NOTIFY`

## 0xFF02 Characteristics breakdown
Properties: NOTIFY, READ, WRITE, WRITE NO RESPONSE Value: (Ox) AA-0A-02-15-03-05-05-05-04-06-06-06-06-06-0B-06-06-00-63-01-00-78-01-00-00-A3

AA - 
0A - 
02 - 
15 - 
03 - Current mode selected (00 for mode 1, 03 for mode 4)
05 - Mode 1 Vibration strenght
05 - Mode 1 Oscillation range (01 to 0A)
05 - Mode 1 Oscillation speed (01 to 0A)
04 - Mode 2 Vibration strenght
06 - Mode 2 Oscillation range (01 to 0A)
06 - Mode 2 Oscillation speed (01 to 0A)
06 - Mode 3 Vibration strenght
06 - Mode 3 Oscillation range (01 to 0A)
06 - Mode 3 Oscillation speed (01 to 0A)
0B - Mode 4 Vibration strenght (01 to 14)
06 - Mode 4 Oscillation range (01 to 0A)
06 - Mode 4 Oscillation speed (01 to 0A)
00 - 
63 - Maybe battery percentage ?? 00-64
01 - 
00 - 
78 - 
01 - Power control On or off (00, 01)
00 - 
00 - 
A3 - Changes sometimes with the power state
