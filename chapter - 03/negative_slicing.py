name = "deepakverma"
slice1 = name[0:4]
slice2 = name[-11:-7]

print(slice1)
print(slice2)    # both line give same output # this is -ve slicing

mid1 = name[6:11]
mid2 = name[-5:]
print(mid1)   # positive slicing
print(mid2)   # negative slicing

# new ways
print(name[:])  # by default it print whole string
print(name[6:]) # after : it will print till last
print(name[:6])





