

""" module.py """
""" An example of a Python module """

import sys

if __name__ == "__main__":
    print("Don't do that, I am a module!")
    sys.exit()

import platform as pl
from platform import python_implementation, python_version_tuple

# Underlying platform's data, i.e., hardware, operating system, and interpreter version information
def printPlatformInformation():
    print(pl.platform())
    print(pl.platform(0, 1))
    # Generic name of the processor which runs your OS
    print(pl.machine())
    # Processor name
    print(pl.processor())
    # Generic OS name
    print(pl.system())
    # OS version
    print(pl.version())

def printPythonVersion():
    #Python version
    print(python_implementation())
    for atr in python_version_tuple():
        print(atr, end=",")