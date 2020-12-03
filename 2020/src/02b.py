import re

with open('../input/02/input.txt', 'r') as input_text:
    ok = 0
    for pwd_info in input_text:
        m=re.search('(\d+)-(\d+) (\w): (\w+)', pwd_info)
        pos1 = int(m.groups()[0])-1
        pos2 = int(m.groups()[1])-1
        char = m.groups()[2]
        pwd = m.groups()[3]

        ok  = ok + (bool(pos1 < len(pwd) and pwd[pos1] == char) ^ bool(pos2 < len(pwd) and pwd[pos2] == char))
    print (ok)

