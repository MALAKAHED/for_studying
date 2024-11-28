# this is a comment 
# i started to learn python 

print("hello python!")
print("i love python")

print(type(10))
print(type(10.3))
print(type([1 ,1 , 2])) 
print (type("hello"))
print(type((1,2,3,5)))
print(type({"one" : 1 , "tow" : 2}))
print(type(2 == 2))
MyVariable = "my value"
print(MyVariable)
MyVariable = 10
print(MyVariable)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


for number in range (4):
    print ("hi", "(", number + 1, ")")
    
    for number in range (10):
    print("I Love You", number + 1)
    
    #def increment (number , by):
#    return number + by

#print (increment(2 , by=1))

for i in range(ord('a'), ord('z') +1 ):\
print('{:c}'.format(i), end='')

age = 12
messege = "ok" if age >= 18 else "not ok"
print(messege)

a = True 
b = True
c = False

if a and b and not c:
    print("hello")
    
    
age = 22
if 18 <= age < 65:
    print("ok")


x = input("x: ")


y = x + 1

