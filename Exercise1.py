
def contains_purple(*items):
    for i in items:
        if i == 'purple':
            return True
    return  False

print(contains_purple(25, "motyka", 45, [], "purple")) # True