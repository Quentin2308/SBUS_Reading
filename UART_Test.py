from periphery import Serial

# Open /dev/ttyUSB0 with baudrate 9600, and defaults of 8N1, no flow control
#PIN 10

serial = Serial("/dev/ttyS0", baudrate=9600)
print("\nREAD BAUDRATE: 9600\n")
buf = serial.read(23, 2)
print("STOP READING\n")
listBuf = list(buf)
print(listBuf)
serial.close()


serial = Serial("/dev/ttyS0", baudrate=9600, stopbits=2, parity="odd")
print("\nREAD BAUDRATE, stopbits=2, parity=odd: 9600\n")
buf = serial.read(23, 2)
print("STOP READING\n")
listBuf = list(buf)
print(listBuf)
serial.close()


serial = Serial("/dev/ttyS0", baudrate=9600, stopbits=2, parity="even")
print("\nREAD BAUDRATE, stopbits=2, parity=even: 9600\n")
buf = serial.read(23, 2)
print("STOP READING\n")
listBuf = list(buf)
print(listBuf)
serial.close()

print("---------------------------")