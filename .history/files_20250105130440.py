file = open('./countries.txt', 'r')
print('Is file readable: ', file.readable())
for line in file:
    print(line.replace('\n', ''))
file.close()