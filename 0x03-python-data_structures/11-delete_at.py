def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    del my_list[idx]
    return my_list

    '''
    this did not work because the new "my_list" generated is
    different from my_list passed as an argument
    for i in range(0, idx):
        new_list.append(my_list[i])
    for i in range(idx + 1, len(my_list)):
        new_list.append(my_list[i])
    my_list = [x for x in new_list]
    return my_list
    '''
