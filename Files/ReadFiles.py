
import sys
from os import strerror

try:
    stream = open("D:\\TMP", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", strerror(exc.errno))

print(sys.stdin.name)
print(sys.stdout.name)
print(sys.stderr.mode)


try:
    stream = open("D:/Python/Training/Data/example.txt", "rt")
    charac = stream.read(1)
    while charac != "":
        print(charac, end='')
        charac = stream.read(1)

    stream.seek(0)
    file = stream.read()
    for charac in file:
        print(charac, end='')
    
    stream.seek(0)
    line = stream.readline()
    while line != "":
        for charac in line:
            print(charac, end='')
        line = stream.readline()

    stream.seek(0)
    lines = stream.readlines(1)
    for line in lines:
        for charac in line:
            print(charac, end='')

    stream.close()

    for lines in open("D:/Python/Training/Data/example.txt", "rt"):
        for charac in lines:
            print(charac, end='')

except Exception as exc:
    print("Cannot open the file:", strerror(exc.errno))