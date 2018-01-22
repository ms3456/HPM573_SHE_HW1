# create different types of variables
x = 17

y1 = x
print(y1)
print(type(y1))

y2 = float(x)
print(y2)
print(type(y2))

y3 = str(x)
print(y3)
print(type(y3))

y4 = bool(x<20)
print(y4)
print(type(y4))

text = 'The value of x is ' + y3 + '.'
print(text)