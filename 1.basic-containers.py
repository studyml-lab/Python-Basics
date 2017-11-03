#python is dynamically typed language. the type of the variable is 
#inferred based on the value assigned to a variable at that time

# int type
a = 10
print(type(a))
isinstance(a,int)
print(a)


#float type
f = 24.7
print(type(f))
isinstance(f,float)
isinstance(f,int)
print(f)

#bool type
z = True
print(type(z))
isinstance(z,bool)
print(z)

#cast float to int
c1 = int(f)
print(c1)

#None is special value in python
p3 = None
type(p3)

#complex type
c = 2  + 1j
print(type(c))

#cast complext to int which is invalid
c2 = int(c)
