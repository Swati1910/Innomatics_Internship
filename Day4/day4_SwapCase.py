def swap_case(s):
    string = []
    Len = list(s)
    for x in Len:
        y = ''
        if x.islower():
            y+= x.upper()
        elif x.isupper:
            y+= x.lower()
        else:
            string.append(x)
        string.append(y)
    r = ''.join(string)
    return r
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)