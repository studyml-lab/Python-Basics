#list is an indexed container that holds heterogeneous elements
list1 = [10, 30, 20, 40]
type(list1)
print(list1)


#sliced access to elements of list
list1[0]
list1[-1]
list1[0:2]
list1[0:]
list1[:3]
list1[0::2]
list1[0] = 100

#modifying the contents of list
list3 = []
print(list3)
list3.append(10)
list3.append(20)
list3.insert(3,70)
list3.append(True)
list3.append(list1)

#sort the elements of list1
list1.sort()
print(list1)

len(list1)



list3 = [list1, 60, ['San Franciso',20,True]]
len(list3)



#iterate through the list elements
for x in list1:
    print(x)
    
    
#create a --range-- with elements in the range of 1 to 10 with step size of 1
range1 = range(1,10,1)
type(range1)

list5 = list(range1)




# --------------Some more practice --------------------------------------

list1 = [10, 30, 20, 40, 50]
list1.count(10)
list1.append(60)
print(list1)
list1.extend([70,80])
list1.sort()
list1.insert(1,15)
list1.clear()
type(list1)
len(list1)



list1 = [1,2,3,4,5,6,7,8,9,10]
list1[2]
list1[2] = 27

list1 = [1,3,5,7,9,11]

for e1 in list1:
    print(e1)

list2 = []
for index,element in enumerate(list1):
    print(index,element)
    list2.append(list1[index]**3)

print(list2)