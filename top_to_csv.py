import click

@click.command()
@click.option('--file', help = 'The file in top.log format to be converted into csv')

def main(file):
    '''
    Converts the selected top.log file into csv format
    '''
    with open(file,'r') as log:
        new = f'{file.split(".")[0]}.csv'
        with open(new, 'w') as output:
            head = '#Date,Time,Users,Load_one,load_two,load_three,Total_tasks,Running_tasks,sleeping_tasks,stopped_tasks,zombie_tasks,CPU_us,CPU_sy,CPU_ni,CPU_id,CPU_wa,CPU_hi,CPU_si,CPU_st,Mem_total,free_mem,used_mem,cache_mem,pid,user,cpu,mem,time,command'
            header = 0
            other = ''
            output.write(f'{head}\n')
            # Cycle through file
            for line in log:
                if len(line) == 1:
                    output.write('')
                elif header != 0:
                    # Do the header conversion here
                    header -= 1
                    thing = convert_header(line, header)
                    output.write(thing)
                    other += thing
                elif line[:3] == 'top':
                    header = 5
                    thing = convert_header(line, header)
                    output.write(thing)
                    other = thing
                else:
                    pid = int(line[:5].replace(' ',''))
                    user = line[6:16].replace(' ','')
                    cpu = float(line[46:52].replace(' ',''))
                    mem = float(line[52:58].replace(' ',''))
                    time = line[59:67].replace(' ', '')
                    command = line[68:]
                    if command.find('trth2raw.exe') != -1 or command.find('rt_loader_daily.exe') != -1:
                        output.write(convert_line(other,pid,user,cpu,mem,time,command))
    print("Finished")

def convert_header(line, pos):
    # Convert the header into csv output
    output = ''
    stuff = line.split(',')
    if pos == 5:
        date = stuff[0]
        time = stuff[1].replace(' ','')
        users = stuff[2][2:]
        loads = [float(stuff[3].split(' ')[-1]),float(stuff[4].replace(' ','')),float(stuff[5].replace(' ',''))]
        output += f'{date},{time},{users},'
        for i in loads:
            output += f'{i},'
    elif pos == 4:
        for i in stuff:
            thing = i.split(' ')[-2]
            output += f'{thing},'
    elif pos == 3:
        for i in stuff:
            thing = i.split(' ')[-2]
            output += f'{thing},'
    elif pos == 2:
        tot = stuff[0].split(' ')[-1].split('+')[0]
        free = stuff[1].split(' ')[-2]
        used = stuff[2].split(' ')[-2]
        cache = stuff[3].split(' ')[-1].split('+')[0]
        output += f'{tot},{free},{used},{cache},,,,,,'
    elif pos == 1:
        return '\n'
    else:
        return ''
    return output


def convert_line(thing,pid, user, cpu, mem, time, com):
    # Convert the line into csv output
    return f'{thing[:len(thing) - 6]}{pid},{user},{cpu},{mem},{time},{com}'

if __name__ == '__main__':
    main()
