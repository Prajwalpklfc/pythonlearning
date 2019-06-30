from view import view
from insert import insert
print("1.insert 2.view")
a=int(input())
if a==1:
    print("enter your name")
    name=input()
    print("enter your email")
    email=input()
    n=insert(name,email)
    print("inserted succesfully \nyour id is "+str(n))
elif a==2:
    print("enter id")
    id=input()
    view(id)


