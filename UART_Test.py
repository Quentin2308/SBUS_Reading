from periphery import Serial

# Open /dev/ttyUSB0 with baudrate 9600, and defaults of 8N1, no flow control

serial = Serial("/dev/ttyUSB0", baudrate=9600)
print("\nREAD BAUDRATE: 9600\n")
buf = serial.read(23, 2)
print("STOP READING\n")
print("read {:d} bytes: _{:s}_".format(len(buf), buf))
serial.close()


serial = Serial("/dev/ttyUSB0", baudrate=9600, stopbits=2, parity="odd")
print("\nREAD BAUDRATE, stopbits=2, parity=odd: 9600\n")
buf = serial.read(23, 2)
print("STOP READING\n")
print("p=odd| read {:d} bytes: _{:s}_".format(len(buf), buf))
serial.close()


serial = Serial("/dev/ttyUSB0", baudrate=9600, stopbits=2, parity="even")
print("\nREAD BAUDRATE, stopbits=2, parity=even: 9600\n")
buf = serial.read(23, 2)
print("STOP READING\n")
print("p=even| read {:d} bytes: _{:s}_".format(len(buf), buf))
serial.close()

print("---------------------------")