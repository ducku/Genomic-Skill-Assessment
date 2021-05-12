import re #regex
import sys #command line argument

# dictionary containing possible unit conversions
prefix = {
    "B": 1.1,
    "K": 1000.1,
    "KB": 1000.1,
    "M": 1000.2,
    "MB": 1000.2,
    "G": 1000.3,
    "GB": 1000.3,
    "T": 1000.4,
    "TB": 1000.4,
    "P": 1000.5,
    "PB": 1000.5,
    "E": 1000.6,
    "EB": 1000.6,
    "Z": 1000.7,
    "ZB": 1000.7,
    "Y": 1000.8,
    "YB": 1000.8,
    "KI": 1024.1,
    "KIB": 1024.1,
    "MI": 1024.2,
    "MIB": 1024.2,
    "GI": 1024.3,
    "GIB": 1024.3,
    "TI": 1024.4,
    "TIB": 1024.4,
    "PI": 1024.5,
    "PIB": 1024.5,
    "EI": 1024.6,
    "EIB": 1024.6,
    "ZI": 1024.7,
    "ZIB": 1024.7,
    "YI": 1024.8,
    "YIB": 1024.8,
    
}

# returns tuple containing int and string
def seperate_int_string(string):
    # string passed in is invalid
    if string.isnumeric() or not string[0].isdigit():
        return (0, "error")

    # regex to split string and int
    regex = re.compile("([0-9]+)([a-zA-Z]+)")

    tup = regex.match(string).groups()
    return tup

def get_byte(string_input):
    # tuple storing int and string
    tup = seperate_int_string(string_input)

    value = int(tup[0])
    unit_prefix = tup[1].upper()

    # split string on the decimal, resulting in the base and the power
    arr = str(prefix.get(unit_prefix)).split(".")
    base = int(arr[0])
    power = int(arr[1])
    return (value * base ** power)

def main():
    string_input = sys.argv[1]
    print(get_byte(string_input))

if __name__ == "__main__":
    main()
