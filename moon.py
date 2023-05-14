import math

iui = 36525
iuir = iui*iui

def mi_L(T_c):
    a= 1336.85522467/iui
    b=0.00000313/iuir
    return 0.60643382 + (a-b*T_c)*T_c
def an_l(T_c):
    b=0.00002565/iuir
    a=1325.55240982/iui
    return 0.37489701 + (a+b*T_c)*T_c
def el_d(T_c):
    b=0.00000397/iuir
    a=1236.85308708/iui
    return 0.82736186 + (a-b*T_c)*T_c
def angle_moon(T_c):
    a = mi_L(T_c)
    l = an_l(T_c)*2*math.pi
    d = el_d(T_c)*2*math.pi
    a += math.sin(l)*0.017469135802469136 #22640s
    a -= math.sin(l - 2*d)*0.0035385802469135802 # 4586s
    a += math.sin(2*d)*0.0018287037037037037 # 2379
    a += math.sin(2*l)*0.0005933641975308641 # 769
    return a%1



def circle(revers,scale,canvas_moon):
    i=0
    arr = []
    rr = 95
    rrr = rr
    if(revers):
        rrr = (-rrr)
    rrr = scale * rrr
    pi = math.pi*2
    xx = (math.sin(pi * i) *(rrr) )+ rr+30
    yy = (math.cos(pi * i) *rr) + rr+30
    while i <= 0.5:
        i += 0.03
        xx2 = (math.sin(pi * i) * (rrr))+rr+30
        yy2 = (math.cos(pi * i) * rr)+rr+30
        arr.append(canvas_moon.create_line(xx,yy,xx2,yy2,fill="#ffffff"))
        xx = (math.sin(pi*i)*(rrr))+rr+30
        yy = (math.cos(pi*i)*rr)+rr+30
    return arr

def phase_m(phase,canvas_moon):
    if(0>math.cos(phase)):
        arr1 = circle(False, math.sin(phase),canvas_moon)
        arr2 = circle(False, 1,canvas_moon)
    else:
        arr1 = circle(True, math.sin(phase),canvas_moon)
        arr2 = circle(True, 1,canvas_moon)
    return (arr1 , arr2)