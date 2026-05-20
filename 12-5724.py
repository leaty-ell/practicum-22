t= 0
for n in range(10, 100):
    a='1'+n*'0'
    while '10' in a:
        if '10' in a:
            a=a.replace('10', '001',1)
        if '1' in a:
            a=a.replace('1', '01',1)
    m=len(a)
    p = 0
    for k in range(2, int(m**0.5)+1) :
        if m%k==0:
            p+=1
    if p==0:
        t += 1
print(t)
