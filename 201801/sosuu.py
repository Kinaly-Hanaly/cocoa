MAX = 10000

for i in range(1,MAX):
    j = 2
    while ( j<i ):
        if ( i%j == 0 ):
            break
        else:
            j += 1
    if ( i==j ):
        print(i)

