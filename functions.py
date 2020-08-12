def add(x,y):
    c=x+y
    print(c)

add(3,4)

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

res = add_sub(7,4)
print(res)

def update(x):
    x = 8
    print("x" , x)

update(10)
a= 10
update(a)
print("a", a)

def update(lst):
    lst[1] =3
    print("lst ", lst)

lst = [4,6,8]
update(lst)
print("original",lst)