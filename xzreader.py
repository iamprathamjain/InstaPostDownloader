import os
import lzma
import json

def open_xz_file(filename):
    with lzma.open(filename, 'rb') as f:
        data = f.read()
    return data

x=(open_xz_file('reels/2023-07-06_18-57-45_UTC.json.xz'))

# print(type(x))


string_data = x.decode('utf-8')
dict_data = json.loads(string_data)
print(dict_data.keys())
l=(list(dict_data.get('node').keys()))
ll=(list(dict_data.get('instaloader').keys()))
# print(l)
for i in l:
    print(i,':',dict_data.get('node').get(i))
    print()

# for i in ll:
#     print(i,':',dict_data.get('instaloader').get(i))
#     print()

