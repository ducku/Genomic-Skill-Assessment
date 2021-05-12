import json
import getopt
import sys
import ntpath #used to strip directory from filepath string name

from convert_size import get_byte
from convert_size import prefix
from convert_size import seperate_int_string

options = "f"

long_options = "files"

arguments = sys.argv[1:]

# values contain file names
options, values =  getopt.getopt(arguments, options, long_options)

# loop through all given json files
for file_name in values:
    # open file
    f = open(file_name)

    dictionary = json.load(f)

    # strip directory in string and replace input with output
    out_file_name = ntpath.basename(file_name.replace("input", "output"))

    # loop through each task
    for task in dictionary:
        task_items = dictionary[task].items()
        # loop through each item in task
        for item in task_items:
            # check if the item value has a byte prefix on it
            value, string = seperate_int_string(str(item[1]))
            if string.upper() in prefix:
                # convert size
                dictionary[task][item[0]] = get_byte(str(item[1]))

    # write dictionary to new json file
    with open(out_file_name, 'w') as outfile:
        json.dump(dictionary, outfile, indent=4)


    print(out_file_name)

    f.close()
