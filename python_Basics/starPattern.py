# s = int(input("Enter rows: "))

s = 5

for i in range(s+1):
    for j in range(i):
        print("*", end =" ")
    print()


for i in range(1, s + 1):
    for j in range(s - i):
        print(" ", end="")
        
    for k in range(1, 2*i):
         print("*", end="")
    print()



for i in range(1, s + 1):
    for j in range(s - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print()

print()

for i in range(s,0,-1):
    for j in range(s-i):
        print(" ", end="")
    
    for k in range(2*i-1):
        print("*", end="")
    print()

for i in range(s,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()