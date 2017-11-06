#tuple: immutable list

tuple1 = (1, 8, 27, 64, 125, 216, 64)
type(tuple1)
tuple1[0]
tuple1[-1]
tuple1[0:3]
tuple1[2] = 100  # will through an error

len(tuple1)
tuple1.count(64)

for x in tuple1:
    print(x ** 2)
    
list1 = list(tuple1)

type(list1)


shape2 = (10, 20, (40,50), True)
len(shape2)
shape2[2]
shape2[2][1]

