n1=int(input("Enter a value 1:"))
even=[]
odd=[]
def evenOdd(n1):
   if (n1%2==0):
       even.append(n1)
       print("even list",even)
   else:
       odd.append(n1)
       print("odd list",odd)
evenOdd(n1)
# print(even)
# print(odd)