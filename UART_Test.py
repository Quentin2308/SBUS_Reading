from periphery import Serial
import bitarray as ba
import bitarray.util as bau
import time

# Open /dev/ttyUSB0 with baudrate 9600, and defaults of 8N1, no flow control
#PIN 10
#in bits

_PACKET_LENGTH = 298
_UART_FRAME_LENGTH = 12

#used to check packets for validity
_UART_FRAME_CONFORMANCE_BITMASK = ba.bitarray('100000000011')

#used to check failsafe status
_FAILSAFE_STATUS_BITMASK = ba.bitarray('000000001100')
def sanity_check_packet(packet):
    # checks for data coherency for UART frames
    # sbus is an *inverted* protocol

    # Returns 3 value tuple:
    # 1 - Packet good? - True/False
    # 2 - Error - None if no error, error message if packet is bad
    # 3 - Data - None if no error, bad packet data if packet is bad

    ret_val = (True, None, None)

    # SBus starts with an opening byte (0x0F), which we ignore
    # UART frames are 12 bits (see packet diagram above)
    # 22-bytes of data + 1 end byte with failsafe data
    i = 0
    for packet_bits_ptr in range(0, _UART_FRAME_LENGTH + 23 * _UART_FRAME_LENGTH, _UART_FRAME_LENGTH):

        # extract current UART frame
        cur_UART_frame = packet[packet_bits_ptr:packet_bits_ptr + _UART_FRAME_LENGTH]
        print(i, cur_UART_frame)
        i += 1
        continue
        # this "and" operation will result in 100000000000 in binary for correct frame - 2048 decimal
        if bau.ba2int(_UART_FRAME_CONFORMANCE_BITMASK & cur_UART_frame) != 2048:
            return (
            False, f'UART start or stop bits bad (frame #{packet_bits_ptr / _UART_FRAME_LENGTH + 1})', cur_UART_frame)

        # parity bit in UART
        if bau.parity(cur_UART_frame[1:9]) == cur_UART_frame[9]:
            # due to inversion, parity checks fail when parity is equal
            return (False, f'Parity check failure (frame #{packet_bits_ptr / _UART_FRAME_LENGTH + 1})', cur_UART_frame)

    return ret_val

print("---------------------------")

import gpiod
from datetime import timedelta

CONSUMER = "led-demo"
chip = gpiod.Chip("0", gpiod.Chip.OPEN_BY_NUMBER)

sbus = chip.get_line(22)  # pin 07
while True:
    if sbus.event_wait([10[,]]):
        # event_read() is blocking function.
        event = button.event_read()
        if event.event_type == line_event.RISING_EDGE:
            print("rising: ", event.timestamp)
        else:
            print("falling: ", event.timestamp)
    else:
        print("timeout(10s)")

print("---------------------------")
