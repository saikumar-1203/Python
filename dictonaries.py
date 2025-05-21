d={1:"A",2:"B"}
d[3]="C"
print(d)
print(d.keys())
print(d.values())
d.pop(1)
print(d)
d.update({1:"A"})
print(d)
print(d.items())
x=d.get(1)
print(x)


