
def get_key_from_val(_dict, val): 
    for k, v in _dict.items():
        if val == v:
            return k


def get_val_from_key(_dict, key):
    for k, v in _dict.items():
        if key == k:
            return v
