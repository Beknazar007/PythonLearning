# a=input()
# b=1
# for i in a:
#     print(a*b)
#     b+=1
# =================================================================================
# a=5
# for i in range(1,10,2):

#     print(a*"-"+str(i)*i+a*"-")
#     a-=1
# =================================================================================
# a=input()
# for i in range(1,len(a)+1):

#     print(a[0:i])
# a=input()
# b=''
# for i in a:
#     b=b+i
#     print(b)
# =================================================================================
# year = int(input("Enter a year: "))
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('This year is a leap year.')
# elif year<=0:
#     print("Invalid input!")

# else:
#     print('This year is not a leap year.')
# =================================================================================
a=int(input())
b=int(input())
if a==b:
    print(a)
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=' ')

elif a<b:
    for i in range (a,b+1):
        print(i,end=" ")
