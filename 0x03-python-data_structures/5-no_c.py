def no_c(my_string):
    new_string = ''
    for chr in my_string:
        if (chr != 'c' and chr != 'C'):
            new_string = new_string + chr
    return new_string

'''
    my_list = list(my_string)
    counter_c = my_list.count('c')
    counter_C = my_list.count('C')

    if counter_c > 0:
        for i in range(counter_c):
            my_list.remove('c')
            
    if counter_C > 0:
        for i in range(counter_C):
            my_list.remove('C')

    new_string = ''.join(my_list)
    return new_string
'''
