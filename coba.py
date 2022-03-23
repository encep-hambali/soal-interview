list1=[]
for i in range(1,51):
    if i%3==0 and i%5==0:
        i="Fronend Backend"
    elif i%3==0:
        i="Frondend"
    elif i%5==0:
        i="Backend"
    list1.append(i)

str1 =""
for i in list1:
    
    str1 = str1+ str(i) +', '

print(str1)


