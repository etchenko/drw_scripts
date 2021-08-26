import difflib

# The grep files you wish to parse
files = ["HISTLDR1-20210821.grep", "HISTLDR2-20210821.grep", "HISTLDR3-20210821.grep", "HISTLDR4-20210821.grep"]
warnings = {"Attempt" : {}, "message" : {}, "Failed" : {}, "Other" : {}}


def main():
    '''
    Returns the amount of times each error occures in a given venue on a given date.

    This script requires that you input the first word (space separated) of the error in order to
    differentiate them (You can use the grep_error_types.py script to find each type of error).
    '''
    samples = {}
    for key in warnings:
        samples[key] = ""
    for i in files:
        run_file(i, samples)
    with open(f'warning-list.txt','w') as summary:
        for key in warnings:
            for i in (dict := warnings[key]):
                summary.write(f'"{" ".join(samples[key].split(" ")[2:])[:15]}" {i} {dict[i]}\n')


def run_file(name, samples):
    with open(name, 'r') as file:
        count = 0
        for line in file:
            count += 1
            if count % 10000 == 0:
                print(f'Parsed {count} lines')
            type = line.split(" ")[2]
            venue = "-".join(line.split(" ")[0].split("-")[1:3])
            if type in warnings:
                add_error(type, venue, warnings, line, samples)

            else:
                add_error("Other", venue, warnings, line, samples)

def add_error(type, venue, warnings, line, samples):
    if venue in (dict := warnings[type]):
        dict[venue] += 1
    else:
        dict[venue] = 1
                
    # Set sample
    if samples[type] == "":
         samples[type] = line


if __name__ == '__main__':
    main()
