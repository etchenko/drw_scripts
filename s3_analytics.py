import boto3
import click
import datetime


bucket_name = 'internal-shared-dropbox-omd-910929753202'

def main():
    '''
    Get monthly sizes for all of the files in every venue in a given bucket, and then writes it to the
    file 'size_analysis_output.txt'
    '''
    list = ('CME','CBT','CMX','GEM','IMM','IOM','NYM')
    # Set up connection with s3 client
    client = boto3.client('s3', region_name="us-east-2")
    output = ""
    # Get list of all objects in internal-shared Bucket with Prefix of venue
    for venue in list:
        response = client.list_objects_v2(Bucket=bucket, Prefix=f'{venue}/')

        # Get a count of the size of all of the files for every month for every Venue
        sizes = [0]*12
        count = 0
        sum_size = 0
        # For each object fetched, calculate:
        for bucket_object in response.get('Contents', []):
            key = bucket_object['Key']
            print(key)
            year = key.find('2021')
            if year != -1 and key.find('Data') != -1:
                size = bucket_object['Size']
                # Total number of objects
                month = key[year + 5:year + 7]
                sizes[int(month) - 1] += size
                count += 1
                # Total size of objects
                sum_size += size
        # print total number, min, max, total size, and average size of fetched objects
        if count > 0:
           # output += f'\nVenue: {venue}\nFile count: {count}\nTotal size: {sizeof(sum_size)}\n'
            for i in range(len(sizes)):
                month = datetime.date(1900,i + 1, 1).strftime('%b')
                output += f'{venue} {month} {sizeof(sizes[i])}\n'
        else:
            output += f'No objects with prefix: {venue} found in bucket\n'

    with open('size_analysis_output.txt','w') as file:
        file.write(output)

def sizeof(num, suffix='B'):
    return '%.3f GB' % (num / (1024.0 * 1024.0 * 1024.0))

if __name__ == '__main__':
    main()
