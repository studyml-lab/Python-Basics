# Strings

s1 = "San Francisco is in USA"
print(type(s1))

isinstance(s1, str)
isinstance(s1, int)

s2 = s1.upper()
print(s2)

# accessing string contect:
s1[2]
s1[1:5]
s1[4:]

# Modifying string content:
s1[0] = 'A'     # will through an error
s1 + ' There Summer holidays are in August'
print(s1)
s1 = s1 + ' There Summer holidays are in August'
print(s1)

s1 = s1.replace('August','September')
print(s1)

s1.capitalize()
s1.split(sep='is')

# what did we learn:
    
# strings are collection of char
# indexes / slice based access