
from os import strerror

def printHistogram(histogram):
    for key, value in histogram.items():
        print(key, '\t', value)

def readFile(filePath):
    histogram = {}
    try:
        for lines in open(filePath, "rt"):
            words = lines.split()
            name = str(words[0]) + ' ' + str(words[1])
            if name in histogram:
                    histogram[name] += float(words[2])
            else:
                histogram[name] = float(words[2])
    except Exception as exc:
        print("Cannot open the file:", strerror(exc.errno))
    except IOError as exc:
        print("I/O error occurred:", strerror(exc.errno))

    sorted_histogram = {k: v for k, v in sorted(histogram.items(), key=lambda item: item[0])}

    return sorted_histogram

filePath = "D:/Python/Training/Data/StudentsResults.txt"
histogram = readFile(filePath)
printHistogram(histogram)
