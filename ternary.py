# x = firstValue if condition else secondValue
# If condition is True then firstValue will be considered else secondValue will be considered.

a, b = 10, 20
x = 30 if a<b else 40
print(x)

a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))
min = a if a<b and a<c else b if b<c else c
print(min)