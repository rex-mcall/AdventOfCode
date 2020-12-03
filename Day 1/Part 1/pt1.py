file = open('Day One\Part One\list.txt', 'r')
lines = file.readlines()

for x in lines:
    for y in lines:
        if int(x) + int(y) == 2020:
            print(int(x) * int(y))
