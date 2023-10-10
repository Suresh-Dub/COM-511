Str = "Welcome to python"
c = 0

for i in Str:
    if i.isalpha():
        c += 1

print("Number of alphabets in the string:", c)
print(Str[5:12])

Alpha = Str.isalnum()
print("It is Alphanumeric" if Alpha else "It is not Alphanumeric")
