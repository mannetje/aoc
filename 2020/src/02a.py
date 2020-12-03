import re

with open('../input/02/input.txt', 'r') as input_text:
    ok = 0
    for pwd_info in input_text:
        m=re.search('(\d+)-(\d+) (\w): (\w+)', pwd_info)
        min = int(m.groups()[0])
        max = int(m.groups()[1])
        char = m.groups()[2]
        pwd = m.groups()[3]

        amount = pwd.count(char)
        if amount >= min and amount <= max:
            ok = ok + 1
    print (ok)

