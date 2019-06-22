# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:54:50 2018

@author: T400
"""

def ds():
    print("D=S：a-bp=c+dp")
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    d=float(input('d='))
    p=(a-c)/(b+d)
    q=a-b*p
    print('均衡價格與數量')
    return p,q

def tax():
    print("Pd=Ps+t")
    a=float(input('需求線截距'))
    b=float(input('需求線斜率(絕對值)'))
    c=float(input('供給線截距'))
    d=float(input('供給線斜率'))
    t=float(input('稅'))
    p1=(a-c)/(b+d)
    ps=(a-c-b*t)/(b+d)
    pd=ps+t
    q2=a-b*pd
    eq=(round(pd,2),round(q2,2))
    q=round(pd-p1,2)
    w=round((pd-p1)/t,2)
    e=round(p1-ps,2)
    r=round((p1-ps)/t,2)
    print('稅後均衡價格與數量：')
    print(eq)
    print('轉嫁給消費者的稅：')
    print((q,w))
    print('轉嫁給生產者的稅：')
    print((e,r))






