#DRW FILES

##GREP ERROR TYPES

This script parses through a grep file (using the command line argument '--file'), and writes into the output file samples of all of the different types of errors and warning that it can find. The classification of what is considered a unique error is done by the difflib.get_close_matches() function

##ERROR SUMMARY

This script prints out the amount of time each type of a unique error is encountered in a venue at a given date. In order to run this script, you must specify the file names in the first array of the script, and the first word (space separated) of each type of error found in the grep_error_types.py script. It will then write the output to the warning-list.txt file.

##FIND TIME

This script finds the earliest starttime and latest endtime in a MARKETPRICE-Report file. Specify the file using the '--path' command line argument, and the '--print_row' argument can be used in order to print out the entire row of the discovered timestampts rather than just the line number.

##IOTOP TO CSV

This script converts an iotop.log file into csv format. The file is specified at the bottom of the script.


