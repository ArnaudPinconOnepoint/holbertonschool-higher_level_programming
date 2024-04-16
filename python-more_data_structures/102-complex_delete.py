def complex_delete(a_dictionary, value):
    to_remove = []
    for i in a_dictionary.keys():
        if a_dictionary.get(i) == value:
            to_remove.append(i)
    for j in to_remove:
        a_dictionary.pop(j)
