
from os import strerror

# array containing (amorphous) bytes.
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

try:
    bf = open('D:/Python/Training/Data/file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
readdata = bytearray(10)
try:
    bf = open('D:/Python/Training/Data/file.bin', 'rb')
    bf.readinto(readdata)
    # or read all the contents of the file into the memory into immutable object
    bf.seek(0)
    readdata = bytearray(bf.read())
    bf.close()
    for b in readdata:
        print(hex(b), end=" ")
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

def copy():
    input = open('D:/Python/Training/Data/example.txt', 'r')
    output = open('D:/Python/Training/Data/exampleCopy.txt', 'w')
    for charac in input:
        output.write(charac)
    input.close()
    output.close()

copy()
