def min_formed_with_digits(n):
    if n==0:
        return 0;
    v=[0,0,0,0,0,0,0,0,0,0]
    m=0
    while n!=0:
        v[n%10]+=1
        n//=10
    cif=1
    while(v[cif]==0):
        cif+=1
    m=cif
    v[m]-=1
    for i in range(len(v)):
        for j in range(v[i]):
            m=m*10+i
    return m

if __name__ == '__main__':
    n=input("input a number:")
    print("The minimal natural number formed with the same digits:")
    print(min_formed_with_digits(int(n)))