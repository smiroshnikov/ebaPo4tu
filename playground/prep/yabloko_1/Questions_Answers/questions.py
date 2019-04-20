# Patrt 1
import sys

s = "abs__sd__sdqaea__weqw__"


# Question remove _ frpm s

def rm(s):
    res = []
    for letter in s:
        if letter != "_":
            res.append(letter)
    return str(res)


new_s = rm(s)


# print(new_s)

# Question
# Can you this without helper variable

# Question 3  words = ['hey', 'hey', 'hey','name','momo','momo']
# given list and integer k =1 result will be 'hey'
# given list and integer k =2 result will be 'momo'
# given list and integer k =3  result will be 'name'
# solve sms

# important lesson - string in python are immutable
# Question 2
# write CSV parser,then explain if its O(n) then improve - use dicts


def gimme_dict_occur(words_list, k):
    counted_words = {}
    for word in words_list:
        counted_words[word] = w.count(word)
    sorted_counted_words = sorted(counted_words.items(), key=lambda kv: kv[1])
    try:
        sorted_counted_words.reverse()
        return sorted_counted_words[k - 1][0]

    except IndexError as e:
        print(f"OMG wrong Index {e}")
        return None


w = ['hey', 'hey', 'hey', 'hey', 'my', 'name', 'name', 'momo', 'momo', 'name']
print(gimme_dict_occur(w, 1))  # --> hey
print(gimme_dict_occur(w, 2))  # --> name
print(gimme_dict_occur(w, 3))  # --> my
print(gimme_dict_occur(w, 33))  # None

"""
k = 1 --> return d[last]
k = 2 --> return d[last-1]
k=  3 --> return d[last-2]

"""


