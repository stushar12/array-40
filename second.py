a=int(input("Enter start point "))
b=int(input("Enter end point "))

for i in range(a,b+1):
    dict={}
    num=i
    flag=0
    while(num):
        dig=num%10
        if dig not in dict:
            dict[dig]=dig
            flag=1
        else:
            flag=0
            break
        num=num//10
    if(flag):
        print(i,end=" ")