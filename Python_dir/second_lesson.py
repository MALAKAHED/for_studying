string = "  hello world  "

# Escape

print('test double "test"')
print("test single 'test'")

print("""
     hello
    python
   !""")

# indexing

print (string[2:5])
print (string[7])
print (string[:9])
print (string[2:])
print (string[:])
print (string[1::3])

# len () + strip()

print (len(string))
print (string.strip())
print (string.rstrip())
print (string.lstrip())

string = "###@@ hello world @@###"

print (string.strip())
print (string.rstrip("#"))
print (string.lstrip("#"))

# title() + capitalize()

words = "i love use 2d array and 3g technology"

# function title() make the first letter capital + the litter after numbers

print(words.title())

# function capitalize() make the first letter capital

print(words.capitalize())

a, b , c = "1", "11", "111"

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

a = "malak"
b = "MALAK"

print(a.upper())
print(b.lower())
