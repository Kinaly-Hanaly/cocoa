for i in range(1,101):
    line = str(i)
    if ( i%3 == 0):
        line += " fizz"
    if ( i%5 == 0):
        line += " buzz"
    print(line)

