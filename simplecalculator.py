def add(x,y):
    return x+y


def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("select function")
print('1 for add')
print("2 for sub")
print("3 for mul")
print("4 for div")

while True:
    option=input("enter option")
    if option in ('1','2','3','4'):
        try:
            p=float(input('enter first no'))
            q=float(input('enter second no'))
        except ValueError:
            print("invalid inp")
            continue


        if option=='1':
                print(p,'+',q, '=',add(p,q))
        elif option=='2':
                print(p,'-',q,'=',subtract(p,q))

        elif option=='3':
                print(p,'*',q, '=' ,multiply(p,q))
        elif option=='4':
                print(p,'/',q,'=', divide(p,q))






