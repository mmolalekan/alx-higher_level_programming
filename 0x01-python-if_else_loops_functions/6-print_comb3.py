#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j and f'{i}{j}' != '89':
            print('{}{}'.format(i, j), end=', ')
print('{}'.format(89))
