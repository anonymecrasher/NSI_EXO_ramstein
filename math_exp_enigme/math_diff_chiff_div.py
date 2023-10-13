for i in range(10):
    for o in range(10):
        temp2 = str(i) + str(o)
        if i != o and int(temp2)% 2 == 0:
            for p in range(10):
                print(p,'p')
                temp3 = temp2 + str(p)
                if p != o and p != i and int(temp3)% 3 == 0:
                    for q in range(10):
                        print(q,'q')
                        temp4 = temp3 + str(q)
                        if q != p and q != o and q != i and int(temp4) % 4 == 0:
                            for s in range(10):
                                print(s,'s')
                                temp5 = temp4+ str(s)
                                if s != p and s != o and s != i and s != q and int(temp5)% 5 == 0:
                                    for d in range(10):
                                        print(d,'d')
                                        temp6 = temp5 + str(d)
                                        if d != s and d != p and d != o and d != i and d != q and int(temp6)% 6 == 0:
                                            for f in range(10):
                                                print(f,'f')
                                                temp7 = temp6 + str(f)
                                                if f != d and f != s and f != p and f != o and f != i and f != q and int(temp7)% 7 == 0:
                                                    for g in range(10):
                                                        print(g,'g')
                                                        temp8 = temp7 + str(g)
                                                        if g != f and g != d and g != s and g != p and g != o and g != i and g != q and int(temp8)% 8 == 0:
                                                            for h in range(10):
                                                                print(h,'h')
                                                                temp9 = temp8 + str(h)
                                                                if h!= g and h != f and h != d and h != s and h != p and h != o and h != i and h != q and int(temp9)% 9 == 0:
                                                                    for j in range(10):
                                                                        print(j,'j')
                                                                        temp10 = temp9 + str(j)
                                                                        if j!=h and j!= g and j != f and j != d and j != s and j != p and j != o and j != i and j != q and int(temp10)% 10 == 0:
                                                                            print(temp10)
                        
