class MyException(BaseException):
    def __init__(self,message):
        super().__init__(message)

def checkAge(a):
    if a > 20:
        print("valid age")
    else:
        raise MyException("Invalid age")

try:
    a = int(input("enter age"))
    checkAge(a)
except MyException as me:
    print(me)
