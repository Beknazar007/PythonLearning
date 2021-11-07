# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if  a % 2 != 0 and b % 2 != 0 and c % 2 == 0 and d % 2 == 0 or a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0 or c % 2 == 0 and d % 2 == 0 and  b % 2 == 0 and a % 2 == 0 or a % 2 != 0 and c % 2 != 0 and b % 2 == 0 and d % 2 == 0 or a % 2 == 0 and b % 2 != 0 and c % 2 != 0 and d % 2 == 0 or c % 2 != 0 and d % 2 != 0 and a % 2 == 0 and b % 2 == 0 or a % 2 == 0 and b % 2 != 0 and c % 2 == 0 and d % 2 != 0 or a % 2 != 0 and b % 2 == 0 and c % 2 == 0 and d % 2 != 0:
    print("YES")

else:
    print("NO")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')