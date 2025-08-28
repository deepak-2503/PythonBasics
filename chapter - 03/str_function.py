str = "rohit verma"
num = "34728472874"
space =" "
print(str.endswith("ma"))
print(str.endswith("verma"))
print(str.endswith("maa"))

print(str.startswith("r"))
print(str.startswith("roh"))
print(str.startswith("rr"))

print(str.upper())    # all in uppercase
print(str.lower())  # all alph in lowercase
print(str.capitalize())  # capital onlt first letter
print(str.title())  # capital first letter of all word


print(str.isalpha())  # check all char are alphabet or not (whitespace is not considered as aplhabet)
print(num.isnumeric())  # check all char are number
print(space.isspace())  # check only whitesapce


