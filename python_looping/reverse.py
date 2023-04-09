res=[]
num1=eval(input("enter the list"))
for i in range(len(num1)):
    res.append(num1.pop())
print("reverse order is",res)