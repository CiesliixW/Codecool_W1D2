def my_min(a,b):
    if a>b:
        return b
    if b>a:
        return a


def my_max(a,b):
    if a<b:
        return b
    if b<a:
        return a

def my_avg(a,b):
    return int((a+b)/2)


print(my_min(2,6))
print(my_max(2,6))
print(my_avg(2,6))


