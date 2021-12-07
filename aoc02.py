f = open("aoc02.txt", "r")

# ---Part 1---
forward_distance = 0
depth = 0
for i in f:
    if "forward" in i:
        forward_distance+=int(i.split(" ")[1])
    elif "up" in i:
        depth-=int(i.split(" ")[1])
    else:
        depth+=int(i.split(" ")[1])

print(forward_distance * depth)

# ---Part 2---
aim = 0
forward_distance = 0
depth = 0
for i in f:
    if "forward" in i:
        f_value = int(i.split(" ")[1])
        forward_distance+=f_value
        depth+=f_value * aim
    elif "up" in i:
        d_value1 = int(i.split(" ")[1])
        aim-=d_value1
    else:
        d_value2 = int(i.split(" ")[1])
        aim+=d_value2
    

print(forward_distance * depth)