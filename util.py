
#get key from value 
def get_key(_dict, val): 
    for k, v in _dict.items():
        if val == v:
            return k

