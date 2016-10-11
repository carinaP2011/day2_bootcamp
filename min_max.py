def find_min_max(arg):
    maximum = max(arg)
    minimum = min(arg)

    if maximum==minimum:
        return len(arg)
    else:
        return [minimum,maximum]


mylist=(4,4,4,4,4,4)

print(find_min_max(mylist))
