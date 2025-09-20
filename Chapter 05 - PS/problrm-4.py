# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
'''len will be 2 bcoz 20 and 20.0 is same in set and will be written only once'''

print(s)
print(len(s))  # 2
