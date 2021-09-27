num = int(input('Digite um valor para ver sua tabuada; '))
for count in range(10):
    print('%d x %d = %d' % (num, count+1, num*(count+1)))
