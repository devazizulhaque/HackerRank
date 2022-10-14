def fun1(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True
    return False
        
def fun2(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True
    return False

def fun3(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True
    return False

def fun4(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True
    return False
     
def fun5(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True
    return False

if __name__ == '__main__':
    s = input()
    print(fun1(s))
    print(fun2(s))
    print(fun3(s))
    print(fun4(s))
    print(fun5(s))