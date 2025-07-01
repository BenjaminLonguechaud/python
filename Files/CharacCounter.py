
from os import strerror

def printHistogram(histogram):
    for key, value in histogram.items():
        print(key, ' -> ', value)

def writeHistogram(histogram, exportFile):
    fileOutput = open(exportFile, 'w')
    for key, value in histogram.items():
        fileOutput.write(str(key) + ' -> ' + str(value) + '\n')
    fileOutput.close()

def fileHistogram(filePath):
    try:
        stream = open(filePath, "rt")
    except Exception as exc:
        print("Cannot open the file:", strerror(exc.errno))
    
    histogram = {}

    try:
        charac = stream.read(1)
        while charac != "":
            if charac != " " and charac != "\n":
                if charac in histogram:
                    histogram[charac] += 1
                else:
                    histogram[charac] = 1
            charac = stream.read(1)
        stream.close()

        # Or dict(sorted(x.items(), key=lambda item: item[1]))
        sorted_histogram = {k: v for k, v in sorted(histogram.items(), key=lambda item: item[1])}

    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))

    return sorted_histogram

filePath = "D:/Python/Training/Data/example.txt"
histogram = fileHistogram(filePath)
printHistogram(histogram)
exportFile = filePath.replace(".txt", ".hist.txt")
writeHistogram(histogram, exportFile)