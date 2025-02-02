(pygatt_env) pi@raspberrypi:~ $ gatttool -b C0:00:00:01:68:05 -I
[C0:00:00:01:68:05][LE]> connect
Attempting to connect to C0:00:00:01:68:05
Connection successful
[C0:00:00:01:68:05][LE]> char-write-req 0x0028 0100
Notification handle = 0x0027 value: aa 01 02 13 02 00 09 03 58 58 58 54 00 01 42 00 00 59 04 04
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
Characteristic value was written successfully
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
[C0:00:00:01:68:05][LE]> char-write-req 0x0027 AA0F010101A4
Notification handle = 0x0027 value: aa 0f 02 01 00 a6
Characteristic value was written successfully
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
[C0:00:00:01:68:05][LE]> char-write-req 0x0027 AA0F010100A5
Notification handle = 0x0027 value: aa 0f 02 01 00 a6
Characteristic value was written successfully
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
Notification handle = 0x0027 value: aa 0a 02 15 02 02 05 05 04 06 06 07 07 07 14 0a 0a 00 48 01
