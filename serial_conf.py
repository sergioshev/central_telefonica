# $Id: serial_conf.py,v 1.4 2012-03-07 12:26:06 aosorio Exp $ 
# Aca van las configuraciones del puerto serie
#

import serial
port = '/dev/ttyS0'

"""
The parameter baudrate can be one of the standard values: 50, 75, 110, 134,
150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200. 
These are well supported on all platforms. Standard values above 115200 such as:
230400, 460800, 500000, 576000, 921600, 1000000, 1152000, 1500000, 2000000, 
2500000, 3000000, 3500000, 4000000 also work on many platforms.
"""
baudrate = 1200

"""
bytesize - Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
"""

bytesize = serial.EIGHTBITS

"""
parity - Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, 
PARITY_ODD PARITY_MARK, PARITY_SPACE
"""

parity = serial.PARITY_EVEN

"""
stopbits - Number of stop bits. Possible values: STOPBITS_ONE, 
STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
"""

stopbits = serial.STOPBITS_ONE

"""
timeout - Set a read timeout value.
timeout = None: wait forever
timeout = 0: non-blocking mode (return immediately on read)
timeout = x: set timeout to x seconds (float allowed)
"""

timeout = None


