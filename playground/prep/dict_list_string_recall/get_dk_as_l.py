def get_dictkeys_as_list(d):
    only_keys_list = []
    for k, v in d.items():
        only_keys_list.append(k)
    return only_keys_list


d = {1: 2, 'a': 233, 'f': hex(23), "kk": 'ff'}
print(get_dictkeys_as_list(d))
