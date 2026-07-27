# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# for i in range (1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# for i in range (6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

for i in range (5):
    for j in range(5-i):
        print("*", end="")
    print()