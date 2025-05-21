def new_div(d):
    def div(a,b):
        if b==0:
            return 0
        else:
            return d(a,b)
    return div 

@new_div
def division(a,b):
    return a/b
d=division(10,2)
print(d)
d=division(10,0)
print(d)