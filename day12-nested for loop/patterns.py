
'''row =1
for i in range(1,4):
    for j in range(i):
        print('*',end=' ')
    print()

'''
'''row =int(input("ENter any numbers : "))
for i in range(row,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
'''
'''
row =4
for i in range(row,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()'''

count=1
for i in range(1,4):
    for j in range(count):
        print(count,end=' ')
        count=count+1
    print()


count=0
for i in range(1,4):
    for j in range(i):
        count=count+1
        print(count,end=' ')
    print()

