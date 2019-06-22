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

def seqgame():
    player1=int(input("先動玩家有幾種策略？"))
    player2=int(input("後動玩家有幾種策略？"))
    先動=1
    後動=1
    gain1=[]
    gain2=[]
    gain3=[]
    while 1==1:
        print("當  先動  玩家使出 %d 號策略時，"%先動)
        x=float(input("後動玩家使出 %d 號策略時的利得為：" %後動))
        gain1.append(x)
        後動+=1
        if 後動==player2+1:
            a=find_max(gain1)
            if type(a)==list:
                for i in range(len(a)):
                    print("!!!當先動玩家使出 %d 號策略，"%先動)
                    y=float(input("而後動玩家使出 %d 號策略時，先動玩家的利得為：" %(i+1)))
                    gain2.append(y)
                gain3.append(find_max(gain2))
                先動+=1
                後動=1
                gain1=[]
            else:
                print("!!!當先動玩家使出 %d 號策略，"%先動)
                y=float(input("而後動玩家使出 "+str(a)+" 號策略時，先動玩家的利得為："))
                gain3.append(y)
                先動+=1
                後動=1
                gain1=[]
                if 先動==player1+1:
                    break
    print("先動玩家應該使用"+str(find_max(gain3))+"號策略！")
