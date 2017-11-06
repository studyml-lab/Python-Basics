
# Maps / Dict : key value pairs:

m1 = {'length':10, 'width':20}
type(m1)
isinstance(m1,dict) 
print(m1)
len(m1)

m1.keys()
m1.items()

m1.get('length')
m1.get('length1')
type(m1.get('length1'))

m1['length1']   # will through error
m1['length'] = 15
m1['height']= 25
m1.pop('height')
m1.pop('width')


for key in m1.keys():
    print(key, m1.get(key))

