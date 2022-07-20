from sqlalchemy import false


def prime(a):
    for i in range(2,a):
        if(a%i==0):
           print(False)
    print(True)
