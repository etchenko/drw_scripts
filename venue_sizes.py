import boto3
import datetime

bucket_name = 'onetick-uat-ro-mfba384xucaypxeczb9ch5hqykprcuse2a-s3alias'
venue_sizes = {}


def main():
    '''
    This script cycles through the AWS S3 bucket and returns the total size of all of
    the data present for each venue. It is then printed to the console, which can be piped to a file.
    '''
    client = boto3.client('s3', region_name='us-east-2')
    s3_result = client.list_objects_v2(Bucket=bucket_name)

    # Get initial results
    for item in s3_result['Contents']:
        if(item_is_data(item)):
            add_size(item)


    # Continue cycling through the data
    while s3_result['IsTruncated']:
        continuation_key = s3_result['NextContinuationToken']
        s3_result = client.list_objects_v2(Bucket=bucket_name, ContinuationToken=continuation_key)
        for item in s3_result['Contents']:
            if(item_is_data(item)):
                add_size(item)

    # Return the sizes
    for key in venue_sizes:
        print(f'{key} {sizeof(venue_sizes[key])}')
            
def item_is_data(item):
    # Check whether the item is actually data
    key = item['Key']
    if 'MARKETPRICE-Data' in key:
        return True
    return False


def add_size(item):
    # Add the data size to the dictionary
    key = item['Key']
    venue = key.split('/')[0]
    if venue in venue_sizes:
        venue_sizes[venue] += item['Size']
    else:
        print(venue)
        venue_sizes[venue] = item['Size']

def sizeof(num, suffix='B'):
    # Convert to human readable size
    return '%.3f GB' % (num / (1024.0 * 1024.0 * 1024.0))

if __name__ == '__main__':
    main()