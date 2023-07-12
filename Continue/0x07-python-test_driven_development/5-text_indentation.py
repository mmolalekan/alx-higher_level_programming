#!/usr/bin/python3
def text_indentation(text):
    ''' prints a text with 2 new lines
    after each of these characters: ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        skip_space = True
        for i in text:
            if i == '.' or i == '?' or i == ':':
                print("{}\n".format(i))
                skip_space = True
            elif i == ' ' and skip_space:
                continue
            else:
                print(i, end='')
                skip_space = False
