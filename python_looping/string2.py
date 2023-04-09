str=input("enter the string")
for i in range(1,len(str)+1):
    if i%2==0:
        str=str[0:i-1]+"z"+str[i:]
print(str)