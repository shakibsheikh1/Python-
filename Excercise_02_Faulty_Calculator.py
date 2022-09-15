#  faulty calculator
print("Enter which operator you want to use")
a=input()
print("Enter your two values")
b=int(input())
c=int(input())

if a=='*':
    if b==45 and c==3 :
        print("the ans is 555")
    else :
        print("the ans is :",b*c)
elif a=='+':
    if b==56 and c==9:
        print("the ans is 77")
    else:
        print("the ans is :",b+c)
elif a=='/':
    if b==56 and c==6:
        print("the ans is 4")
    else:
        print("the ans is :", b/c)