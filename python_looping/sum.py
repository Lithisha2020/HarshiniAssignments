#Get the sum of two arrays…actually the sum of all their elements.
#P.S. Each array includes only integer numbers. Output is a number too.
list1=eval(input("enter the list"))
sum1=sum(list1)
list2=eval(input("enter the list"))
sum2=sum(list2)
res=sum1+sum2
print("sum of",list1,"and",list2,"is",res)