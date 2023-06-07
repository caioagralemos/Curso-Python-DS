def group_anagrams(a):
    my_dict = {}
    values = []
    for obj in a:
        soma = 0
        for char in obj:
            soma = soma + ord(char)
        if soma in my_dict:
            my_dict[soma].append(obj)
        else:
            my_dict[soma] = []
            my_dict[soma].append(obj)
    for element in my_dict:
        values.append(my_dict[element])
    return values

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""