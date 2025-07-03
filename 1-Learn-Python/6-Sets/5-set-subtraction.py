def find_missing_ids(first_ids, second_ids):
    s1 = set()
    s2 = set()

    for i in first_ids:
        if i not in s1:
            s1.add(i)
    for i in second_ids:
        if i not in s2:
            s2.add(i)

    return s1-s2
