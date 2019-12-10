def dict_flatten(target, separator):
    reVal = {}
    for k,v in target.items():
        if isinstance(v,dict):
            for key,val in v.items():
                reVal[k + separator + key] = val
            reVal = dict_flatten(reVal,separator)
        else:
            reVal[k] = v

    return reVal


if __name__ == '__main__':
    print(dict_flatten({"one": {"two": {"three": {"four": {"five": "six"}}}}}, '__'))