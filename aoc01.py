f = open("aoc01.txt", "r")

# ---Part 1---
total = 0
sonar_list = []
for x in f:
    sonar_list.append(int(x))

for i in range(len(sonar_list)-1):
    if sonar_list[i] < sonar_list[i+1]:
        total += 1
print(total)

# ---Part 2---
total2 = 0
for i in range(len(sonar_list)-3):
    window1 = sonar_list[i] + sonar_list[i+1] + sonar_list[i+2]
    window2 = sonar_list[i+1] + sonar_list[i+2] + sonar_list[i+3]
    if window2 > window1:
        total2+=1
print(total2)