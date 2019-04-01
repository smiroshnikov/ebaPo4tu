def is_anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    if len(s1) != len(s2):
        return False

    for letter in range(0, len(s1)):
        if s1[letter] != s2[letter]:
            return False
    else:
        return True


print(is_anagram("borbus", "subroe"))
print(is_anagram("borbus", "subros"))
