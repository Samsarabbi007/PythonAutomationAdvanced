
# Compare this snippet from basics/Initial_Elements/ArithmeticOperator.py:
x=1
y=2
def swap(x,y):
    temp = x
    x = y
    y = temp
    return x,y
print("with temp_variable x:",x)
print("with temp_variable y:",y)

# This is a simple program to swap two variables without using a third variable.

x=1
y=2

def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y
x, y = swap(x, y)
print("Without temp_Variable x:", x)
print("Without temp_Variable y:", y)


x=1
y=2
x,y=y,x
print("Without temp_Variable x:", x)
print("Without temp_Variable y:", y)


