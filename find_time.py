import os
from csv import reader
from datetime import date, datetime, timedelta
import re
import click

@click.command()
@click.option('--path', help = 'The path to the file you want to extract the timestamps from')
@click.option('--print_row', is_flag=True, default=False,help='Print the entire line rather than just the timestamp')

def find_time(path, print_row):
    '''
    Finds the earliest start_time and latest end_time in a Report file
    '''


    with open(path, 'r') as file:
        # Initialize variables
        start, end = None
        start_i, end_i = 0
        start_row, end_row = ""
        csv_reader = reader(file)
        header = next(csv_reader)

        # Read file
        if header != None:
            for i, row in enumerate(csv_reader):
                dates = (row[3], row[4])
                try:
                    # Find the extreme timestamps
                    date_start = datetime.strptime(row[2][:-4], '%Y-%m-%dT%H:%M:%S.%f')
                    date_end = datetime.strptime(row[3][:-4], '%Y-%m-%dT%H:%M:%S.%f')
                    if start is None:
                        start, end = date_start, date_end
                        start_row, end_row = row
                    if date_start < start:
                        start = date_start
                        start_i = i
                        start_row = row
                    if date_end > end:
                        end = date_end
                        end_i = i
                        end_row = row
                except:
                    print("Failed")
    
    # Print results
    if print_row:
        print(f'Start timestamp: {start_row}')
        print(f'End timestamp: {end_row}')
    else:
     print(f'Start time: {start}, line = {start_i}')
     print(f'End time: {end}, line = {end_i}')


if __name__ == '__main__':
    find_time()
