import re
import subprocess

server = "pisani.challs.olicyber.it"
port = 10500
pos = "00000000-0000-4000-0000-000000000000.maze.localhost."
dirs = ['right', 'up', 'left', 'down']
journey = []
i=0
count= 0
ok= True
sent=0
journey.append([pos, i])
trace = 0
while ok:
    p = subprocess.run([f"dig -p{str(port)} @{server} {dirs[i]}.{pos}"], shell=True, capture_output=True)
    answer = p.stdout.decode()
    flag = subprocess.run([f"dig -t txt -p{str(port)} @{server} {pos}"], shell=True, capture_output=True)
    flag2 = subprocess.run([f"dig -p{str(port)} @{server} {pos}"], shell=True, capture_output=True)
    print(flag.stdout.decode())
    print((flag2.stdout.decode()))
    #print("This is dir", dirs[i], " for pos", pos)
    next_pos = re.search(r"CNAME.+\.maze\.localhost\.", answer)
    if next_pos:
        next_pos = next_pos.group()[6:]
        #print("This is next_pos returned", next_pos)
        #print("This is journey\n\n", journey)
        if next_pos not in [x[0] for x in journey]:
            journey[trace][1] = i
            journey.append([next_pos, 0])
            trace+=1
            pos = next_pos
            i=0
            count+=1
            sent=0
        elif i<3:
            sent=1
            i+=1
        else:
            print(pos)
            pos, i = journey[trace-1]
            journey.pop(-1)
            trace-=1
            i+=1
            sent=1
            while i == 4:
                pos, i = journey[trace-1]
                journey.pop(-1)
                trace-=1
                i+=1
    elif i<3:
        i+=1
    elif i==3 and sent==1:
        print(pos)
        pos, i = journey[trace-1]
        journey.pop(-1)
        trace-=1
        i+=1
        sent=1
        while i == 4:
            pos, i = journey[trace-1]
            journey.pop(-1)
            trace-=1
            i+=1
    else:
        ok=False
        print("This is count", count)
        print(answer)
        print("This is journey", journey)
print("PROCESS DONE\n\n\n", journey)
