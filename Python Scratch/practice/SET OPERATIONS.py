import array as MyRay

a = MyRay.array('i', [1, 2, 3, 4])
b = MyRay.array('i', [4, 8, 10, 2])


def union(a, b):
    result = []
    for x in a + b:
        found = 0
        for y in result:
            found = found + (x == y)
        result = result + ([x] * (found == 0))
    return result


def intersection(a, b):
    result = []
    for x in a:
        for y in b:
            if x == y:
                found = 0
                for z in result:
                    found = found + (x == z)
                result = result + ([x] * (found == 0))
    return result


def difference(a, b):
    result = []
    for x in a:
        found = 0
        for y in b:
            found = found + (x == y)
        result = result + ([x] * (found == 0))
    return result


def symmetric_difference(a, b):
    result = []

    for x in a:
        found = 0
        for y in b:
            found = found + (x == y)
        result = result + ([x] * (found == 0))

    for x in b:
        found = 0
        for y in a:
            found = found + (x == y)
        result = result + ([x] * (found == 0))

    return result


print("Union:", union(a, b))
print("Intersection:", intersection(a, b))
print("Difference (a - b):", difference(a, b))
print("Symmetric Difference:", symmetric_difference(a, b))
