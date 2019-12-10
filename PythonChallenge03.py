def ordinal(num):
    ret = ''
    if num % 10 == 1 and num % 100 != 11:
        ret = str(num) + 'st'
    elif num % 10 == 2 and num % 100 != 12:
        ret = str(num) + 'nd'
    elif num % 10 == 3 and num % 100 != 13:
        ret = str(num) + 'rd'
    else:
        ret = str(num) + 'th'
        
    return ret