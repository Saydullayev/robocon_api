def get_number(s: str) -> int:
    p = 0
    for i in s:
        if i in '0123456789':
            p = p * 10 + int(i)
    return p

def get_number_array(s: str) -> list:
    arr = []
    p = ''
    for i in s:
        if i == ' ':
            x =get_number(p)
            if x > 0:
                arr.append(x)
            p = ''
        p += i
    arr.append(get_number(p))
    return arr