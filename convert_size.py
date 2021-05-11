import re #regex
import sys #command line argument


string_input = sys.argv[1]

# regular expression to seperate first int from first string
regex = re.compile("([0-9]+)([a-zA-Z]+)")

# tuple storing int and string
tup = regex.match(string_input).groups()

value = int(tup[0])
unit_prefix = tup[1].upper()

#dictionary containing possible unit conversions
prefix = {
    "B": 1.1,
    "KB": 1000.1,
    "MB": 1000.2,
    "GB": 1000.3,
    "TB": 1000.4,
    "PB": 1000.5,
    "EB": 1000.6,
    "ZB": 1000.7,
    "YB": 1000.8,
    "KIB": 1024.1,
    "MIB": 1024.2,
    "GIB": 1024.3,
    "TIB": 1024.4,
    "PIB": 1024.5,
    "EIB": 1024.6,
    "ZIB": 1024.7,
    "YIB": 1024.8,
}

# split string on the decimal, resulting in the base and the power
arr = str(prefix.get(unit_prefix)).split(".")
base = int (arr[0])
power = int(arr[1])

print(value * base ** power)
