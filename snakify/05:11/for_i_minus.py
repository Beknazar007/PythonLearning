

for i in range(3) :
    for k in range(10):
        print(str(k)*3, end="")
    print()
    
# 000111222333444555666777888999
# 000111222333444555666777888999
# 000111222333444555666777888999

a=-1
b=""
for i in range(3) :
    while a<9:
        a+=1
        b=b+str(a)*3
    print(b)