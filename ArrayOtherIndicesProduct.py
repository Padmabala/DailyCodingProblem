

def product(nums):
    pre=[];
    for n in nums:
        if(pre):
            pre.append(pre[-1]*n)
        else:
            pre.append(n)
    print(pre)
    suff=[];
    i=n-1
    while(i>=0):
        if(suff):
            suff.append(suff[-1]*nums[i])
        else:
            suff.append(nums[i])
        i-=1
    suff=list(reversed(suff))
    print(suff)

    prd=[]
    for i in range(n):
        if(i==0):
            prd.append(suff[i+1])
        elif(i==n-1):
            prd.append(pre[i-1])
        else:
            prd.append(pre[i-1]*suff[i+1])
    print(prd)

n=int(input("Enter the size of the array: "))
lst=list(map(int,input("Enter the elements: ").split()[:n]))
product(lst);