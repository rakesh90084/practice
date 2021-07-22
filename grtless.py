n1=int(input("Enter a value 1:"))
n2=int(input("Enter a value 2:"))
a=[]
b=[]
def grtLess(n1,n2):
   if n1>n2:
       a.append(n1)
       b.append(n2)
   else:
       b.append(n1)
       a.append(n2)
   
grtLess(n1,n2)
print(a)
print(b)
