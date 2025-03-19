'''row=int(input('enter number: = '))
for i  in range (1, row+1):
    num=i 
    for j in range(1,i+1):
        print(num,end=" ")
        num+=(row-j)
    print()'''





'''row=int(input("Enter Row"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()'''


# row=int(input("Enter Row"))
# for i in range(row,0,-1):
#     for k in range(row-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

'''
row=int(input("Enter Row"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end="  ")
    for j in range(i):
        print("*",end=" ")
    print()

'''


# diamond 
'''

row=int(input("Enter Row"))
for i in range(1,row+1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(row-1,0,-1):
    for k in range(row-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

'''



# hill incremnetal 1357
'''
row=int(input("Enter Row : "))
for i in range(1,row+1):
    for k in range(row-i):
        print(end="  ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()'''

'''
n=int(input("Enter Row : "))
for i in range(n):
    for j in range(n):
        if i==j:
            print('1',end=" ")
        else:
            print('0',end=" ")
    print()
'''



n=int(input("Enter Row : "))
count=0
for i in range(1,7):
    if i%2==0:
        if j%2==0:
         print('count',end=" ")
        count=count+1
    else:
         print('*',end=" ")
    for j in range(1,6):
        if j%2==0:
            else:
            print(count,end="")
           
    print()





