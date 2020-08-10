def twoNumberSum(array,targetSum):
    for i in range(0,len(array)-1):
        number1=array[i]
        print("i is ",array[i]);
        for j in range(i+1,len(array)):
            print("j is ", array[j]);
            number2=array[j]
            if(number1+number2==targetSum):
                return sorted([number1,number2])
    return []

array,targetSum=list(map(int,input().split()[:5])),int(
    input())
print(twoNumberSum(array,targetSum))
