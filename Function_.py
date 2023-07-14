### In this file I will practice function

def hello(name):   # Defining the function
    return(f"Hello,{name}")   # name => Parameter {local}

# example  = hello("Ishaan")   # calling the function

#                             # "Ishaan" passing the argumet   

# print(type(example))


def none():
    return

# print(print(none()))


def f(t):
    return t

def maFonction(a):

    i = 25 + a

    i = f(i)

    return i

# c = maFonction(3)

def a():
    print("a() start")
    b()
    print("a() returns")

def b():
    print("b() start")
    c()
    print("b() returns")

def c():
    print("c() start")
    print("c() returns")




def f():
    name = "Ishaan"
    print("Ishaan")


def spam():
    global eggs

    eggs = "spam"  #Global eggs


def bacon():
    eggs = "bacon"  #local eggs

def ham():
    print(eggs)  #This eggs refer to global eggs = "spam"

eggs = 42 #This is global


x = 12

def f1(a,b=x):
    
    print(a,b)

x = 15

def f():
    global a

    print(a)

    a = "hello"

    print(a)

a = "world"



def f1(a,b = []):
    b.append(a)
    return b

# print(f1(2,[3,4]))


def f(p,q,r):
    global s
    p,q,r,s = 10,20,30,40
    print(p,q,r,s)

p,q,r,s = 1,2,3,4

def f(x):
    print("outer")
    def f1(a):
        print("inner")
        print(a,x)

f1(1)


x = 5
def f1():
    global x
    x = 4

def f2(a,b):
    global x
    return a+b+x



x = 100
def f1():
    global x
    x = 90

def f2():
    global x
    x = 80

y,z = 1,2

def f():
    global x
    x = y+z

