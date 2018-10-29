class MyException(BaseException):
    def __init__(self, message):
        super().__init__(message)

def checkAge(age):
    if age > 20:
        print("Valid age")
    else:
        raise MyException("Invalid Age")

def checkCno(cno):
    if len(cno)== 10:
        print("Valid Contact No")
    else:
        raise MyException("Invalid Contact No")

try:
    a = int(input("enter age"))
    checkAge(a)
    cno = input("enter contact No")
    checkCno(cno)
except ValueError:
    print("Invalid input")
except MyException as me:
    print(me)