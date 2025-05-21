import random
def otp():
    for i in range(4):
        n=random.randint(100000,999999)
        yield n
o=otp()
for p in o:
    print(p)