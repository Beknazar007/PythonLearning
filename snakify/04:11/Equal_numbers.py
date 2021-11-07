# Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
a = int(input())
b = int(input())
c = int(input())
if  a > b and  c == b or b > a and  c == a or c > b and b == a or a < b and  c == b or b < a and  c == a or c < b and b == a:
    print(2)
elif   c == a == b :
    print(3)
else:
    print(0)