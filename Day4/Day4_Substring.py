def count_substring(string, sub_string):
    c =0
    for i in range(0,len(string)):
        if(string.startswith(sub_string,i)):
            c+=1 
        
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)