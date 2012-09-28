a = range(12)

if(len(a)%2 == 1): ##odd
    print "%i %i, %i %i" %(1, a[0], (len(a)/2) + 2, a[len(a)/2 + 1])
    for i in range(1, len(a)/2):
        print "%i %i, %i %i" %(i+1, a[i], i+(len(a)/2) + 2, a[i+(len(a)/2) + 1])
    print "%i %i" %((len(a)/2) + 1, a[(len(a)/2)])
else:
    print "%i %i, %i %i" %(1, a[0], (len(a)/2) + 1, a[len(a)/2])
    for i in range(1, len(a)/2):
        print "%i %i, %i %i" %(i+1, a[i], i+(len(a)/2) + 1, a[i+(len(a)/2)])
