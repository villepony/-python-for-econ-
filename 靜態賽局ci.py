# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:46:03 2018

@author: T400
"""
def find_max(q):
    a=[]
    for i in range(0,len(q)):
        if q[i]!=max(q):
            continue
        else:
            a.append(i+1)
    if len(a)==1:
        return a[0]
    else:
        return a

def game_row():
    row=1
    col=1
    r=int(input("橫軸玩家有幾種策略？"))
    c=int(input("縱軸玩家有幾種策略？"))
    gain=[]
    a=dict()
    while 1==1:
        print("當  縱軸  玩家使出 %d 號策略時，"%col)
        x=float(input("橫軸玩家使出 %d 號策略時的利得為：" %row))
        gain.append(x)
        row+=1
        if row==r+1:
            a[col]=find_max(gain)
            print("!!!!!最佳回應策略："+str(find_max(gain))+"號!!!!!")
            gain=[]
            col+=1
            row=1
            if col==c+1:
                break
    return a

def game_col():
    row=1
    col=1
    r=int(input("橫軸玩家有幾種策略？"))
    c=int(input("縱軸玩家有幾種策略？"))
    gain=[]
    a=dict()
    while 1==1:
        print("當  橫軸  玩家使出 %d 號策略時，"%row)
        x=float(input("縱軸玩家使出 %d 號策略時的利得為：" %col))
        gain.append(x)
        col+=1
        if col==c+1:
            a[row]=find_max(gain)
            print("!!!!!最佳回應策略："+str(find_max(gain))+"號!!!!!")
            gain=[]
            row+=1
            col=1
            if row==r+1:
                break
    return a

def stgame():
    row=1
    col=1
    r=int(input("橫軸玩家有幾種策略？"))
    c=int(input("縱軸玩家有幾種策略？"))
    gain=[]
    a=dict()
    while 1==1:
        print("當  縱軸  玩家使出 %d 號策略時，"%col)
        x=float(input("橫軸玩家使出 %d 號策略時的利得為：" %row))
        gain.append(x)
        row+=1
        if row==r+1:
            a[col]=find_max(gain)
            print("!!!!!最佳回應策略："+str(find_max(gain))+"號!!!!!")
            gain=[]
            col+=1
            row=1
            if col==c+1:
                break
    row=1
    col=1
    gain=[]
    b=dict()
    while 1==1:
        print("當  橫軸  玩家使出 %d 號策略時，"%row)
        y=float(input("縱軸玩家使出 %d 號策略時的利得為：" %col))
        gain.append(y)
        col+=1
        if col==c+1:
            b[row]=find_max(gain)
            print("!!!!!最佳回應策略："+str(find_max(gain))+"號!!!!!")
            gain=[]
            row+=1
            col=1
            if row==r+1:
                break
    dominantr="橫軸玩家有優勢策略："+str(a[1])
    dominantc="縱軸玩家有優勢策略："+str(b[1])
    for s in range(1,len(a)):
        if a[s]==a[s+1]:
            continue
        else:
            dominantr="橫軸玩家沒有優勢策略"
            break
    for s in range(1,len(b)):
        if b[s]==b[s+1]:
            continue
        else:
            dominantc="縱軸玩家沒有優勢策略"
            break
    nashe=""
    print("{縱軸玩家使出的策略：橫軸玩家的最佳回應策略}")
    print(a)
    print("{橫軸玩家使出的策略：縱軸玩家的最佳回應策略}")
    print(b)
    print(dominantr)
    print(dominantc)
    return nashe
