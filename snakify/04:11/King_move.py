# Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if  a % 2 == 0 and b % 2 != 0 and a == c and b - 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and a == c and b + 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and b == d and a - 1 == c :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and b == d and a + 1 == c :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and a - 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and a + 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and a + 1 == c and b + 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 != 0 and a - 1 == c and b + 1 == d :
    print("YES")

#  a % 2 != 0 and b % 2 != 0 
elif  a % 2 != 0 and b % 2 != 0 and a == c and b - 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and a == c and b + 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and b == d and a - 1 == c :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and b == d and a + 1 == c :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and a - 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and a + 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and a + 1 == c and b + 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 != 0 and a - 1 == c and b + 1 == d :
    print("YES")
# a % 2 != 0 and b % 2 == 0
elif  a % 2 != 0 and b % 2 == 0 and a == c and b - 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and a == c and b + 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and b == d and a - 1 == c :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and b == d and a + 1 == c :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and a - 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and a + 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and a + 1 == c and b + 1 == d :
    print("YES")
elif  a % 2 != 0 and b % 2 == 0 and a - 1 == c and b + 1 == d :
    print("YES")

# a % 2 == 0 and b % 2 == 0
elif  a % 2 == 0 and b % 2 == 0 and a == c and b - 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and a == c and b + 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and b == d and a - 1 == c :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and b == d and a + 1 == c :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and a - 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and a + 1 == c and b - 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and a + 1 == c and b + 1 == d :
    print("YES")
elif  a % 2 == 0 and b % 2 == 0 and a - 1 == c and b + 1 == d :
    print("YES")


else:
    print("NO")
# easy way
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')