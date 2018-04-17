src = raw_input('Please into a string:')

strs = 0
ints = 0
space = 0
other = 0

for char in src:
    if char.isalpha():
        strs+=1
    elif char.isdigit():
        ints+=1
    elif char.isspace():
        space+=1
    else:
        other+=1

print("strs=%s ints=%s space=%s other=%s" %(strs, ints, space, other))
