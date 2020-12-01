file = open('list.txt', 'r')
lines = file.readlines()

for x in lines:
    for y in lines:
        for z in lines:
            if int(x) + int(y) + int(z) == 2020:
                print(int(x) * int(y) * int(z))
