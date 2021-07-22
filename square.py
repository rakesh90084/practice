n1=int(input("enter the no :"))
n2=int(input("enter the no :"))
n3=int(input("enter the no :"))
list1=[n1,n2,n3]
def square(a):
    return a**2 
print(list(map(square,list1)))    
