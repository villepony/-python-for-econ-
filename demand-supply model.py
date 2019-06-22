def ds():
    print("D=S：a-bp=c+dp")
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    d=float(input('d='))
    p=(a-c)/(b+d)
    q=a-b*p
    print('equilibrium price and quantity')
    return p,q

def tax():
    print("Pd=Ps+t")
    a=float(input('intercept of the demand line'))
    b=float(input('slope of the demand line(absolute value)'))
    c=float(input('intercept of the supply line'))
    d=float(input('slope of the supply line'))
    t=float(input('tax'))
    p1=(a-c)/(b+d)
    ps=(a-c-b*t)/(b+d)
    pd=ps+t
    q2=a-b*pd
    eq=(round(pd,2),round(q2,2))
    q=round(pd-p1,2)
    w=round((pd-p1)/t,2)
    e=round(p1-ps,2)
    r=round((p1-ps)/t,2)
    print('equilibrium price and quantity after tax:')
    print(eq)
    print('Taxes beared by consumer:')
    print((q,w))
    print('Taxes beared by producer:')
    print((e,r))
