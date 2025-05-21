def power(p):
    def pow(n):
        return p**n
    return pow
p=power(5)
r=p(3)
print(r)
p1=power(4)
r1=p1(3)
print(r1)