a = 2
print(a)

b = 3
print(b)

age = input("Enter upur age: " )
age = int(age)
print('Are you older than 26?', age > 26)

age = input('Enter your age again: ' )

try:
    age = int(age)
    print('How old will you be in 1 year?', age + 1)
except ValueError:
    print('The given age is not valid')
    
 
