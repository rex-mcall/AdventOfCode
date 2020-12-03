file = open('Day 2\passwords.txt', 'r')
lines = file.readlines()

validPasswords = 0

for x in lines:
    index1 = x.index('-')
    index2 = x.index(' ')
    num1 = 0
    num2 = 0
    charToCount = x[index2 + 1]
    charCount = 0
    for y in range(0,index1):
        num1 *= 10
        num1 += int(x[y])
    for z in range(index1 +1, index2):
        num2 *= 10
        num2 += int(x[z])
    for a in x:
        if a == charToCount:
            charCount += 1
    if charCount > num1 and charCount < num2:
        validPasswords +=1
