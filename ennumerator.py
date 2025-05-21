l=[1,2,3,4,5,6]
r=enumerate(l)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

# o/p:
# (0, 1)
# (1, 2)
# (2, 3)
# (3, 4)
# (4, 5)
# (5, 6)


# r=enumerate(l,10)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))


# o/p:
# (10, 1)
# (11, 2)
# (12, 3)
# (13, 4)
# (14, 5)
# (15, 6)