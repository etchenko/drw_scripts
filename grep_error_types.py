import difflib
import click

@click.command()
@click.option('--file', help = 'The .grep file you want to parse')

def main(file):
    '''
    Returns a sample of each of the different types of warnings and errors in a grep file (May run for a long time in large file)
    '''
    list = []
    with open(file, 'r') as input:
        count = 0
        for line in input:
            count += 1
            if count % 1000 == 0:
                print(f'Parsed {count} lines')
            content = " ".join(line.split(" ")[1:])
            matches = difflib.get_close_matches(content, list, 1)
            if matches:
                "nothing"
            else:
                list.append(content)
    with open("error_list.txt", 'w') as output:
        for i in list:
            output.write(i)

if __name__ == '__main__':
    main()
