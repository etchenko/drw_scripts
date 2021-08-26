def main(file):
    '''
    Converts iotop.log files into csv format
    '''
    with open(file,'r') as log:
        new = f'{file.split(".")[0]}.csv'
        with open(new, 'w') as output:
            # Write the header of the csv file
            head = 'TIME,TID,PRIO,USER,DISK_READ,DISK_WRITE,SWAPIN,IO,COMMAND'
            output.write(f'{head}\n')
            for line in log:
                if line[4:8] == 'TIME':
                    'nothing'
                elif line[9:14] == 'Total' or line[9:15] == 'Actual':
                    # Convert the totals into csv line
                    time = line[0:8]
                    type = line[9:15].replace(' ','')
                    disk_read = line[28:41].replace(' ','')
                    disk_write = line[64:77].replace(' ','')
                    output.write(convert_tot(time,type,disk_read,disk_write))
                else:
                    # Convert the line into csv
                    time = line[0:8]
                    tid = line[9:14].replace(' ','')
                    prio = line[15:19]
                    user = line[20:28].replace(' ','')
                    disk_read = line[28:40].replace(' ','')
                    disk_write = line[40:52].replace(' ','')
                    swapin = line[52:58].replace(' ','')
                    io = line[60:66].replace(' ','')
                    command = line[69:]
                    output.write(convert_all(time,tid,prio,user,disk_read,disk_write,swapin,io,command))
    print("Finished")

def convert_tot(time,type,read,write):
    # Converts totals
    return f'{time},{type},,,{read},{write},,,\n'


def convert_all(time,tid,prio,user,disk_read,disk_write,swapin,io,command):
    # Converts regular lines
    return f'{time},{tid},{prio},{user},{disk_read},{disk_write},{swapin},{io},{command}'

if __name__ == '__main__':
    main('iotop.log')
