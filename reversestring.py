res=""
s=input("enter the string")
for i in range(len(s)-1,-1,-1):
    res=res+s[i]
print(f'reverse of {s} is {res}')
    
