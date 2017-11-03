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
