res=[]
list1=eval(input("enter the list"))
list2=eval(input("enter the list"))
for i in range(len(list1)):
    res.append(list1[i]+list2[i])
print(res)