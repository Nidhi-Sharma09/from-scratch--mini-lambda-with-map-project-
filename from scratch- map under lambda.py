'''========= MAP() PRACTICE =========

1. Square Numbers
2. Cube Numbers
3. Double Numbers
4. Add 10
5. Uppercase Names
6. Count Characters
7. Celsius to Fahrenheit
8. Bonus Marks
9. Exit'''

#1. Square Numbers:
num=[1,2,3,4,5,6,7]
sqr= list(map(lambda x: x*x, num))
print(sqr)
#output: [1, 4, 9, 16, 25, 36, 49]

#2. Cube Numbers:
num=[1,2,3,4,5,6,7]
cube= list(map(lambda x: x**3, num))
print(cube)
#output: [1, 8, 27, 64, 125, 216, 343]

#3. Double Numbers:
num=[1,2,3,4,5,6,7]
double=list(map(lambda x: x*2, num))
print(double)
#output:[2, 4, 6, 8, 10, 12, 14]

#4. Add 10:
num=[1,2,3,4,5,6,7]
add_ten=list(map(lambda x: x + 10, num))
print(add_ten)
#output: [11, 12, 13, 14, 15, 16, 17]

#5. Uppercase Names:
user = input("Enter names: ").split()
cap = list(map(lambda x: x.capitalize(), user))
print(cap)
#output: ['Nini']

#6. Count Characters:
user = input("Enter words: ").split()
count = list(map(lambda x: len(x), user))
print(count)
#output:[7] (i types youtube)

#7. Celsius to Fahrenheit:
temps = list(map(float, input("Enter temperatures in celsius: ").split()))
fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps))
print(fahrenheit)
#output: [136.4] (i typed 58)

#8. Bonus Marks:
marks=[50,62,57,88,79]
bonus_marks=list(map(lambda x: x + 5, marks))
print(bonus_marks)
#output: [55, 67, 62, 93, 84] (students are getting extra 5 marks)

