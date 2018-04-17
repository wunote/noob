import shutil
with open('wu.txt', 'r') as f1:
    with open('wu2.txt', 'w') as new:
        for line in f1.readlines():
            if 'te' not in line:
                new.write(line)

shutil.move('wu2.txt', 'wu.txt') 
