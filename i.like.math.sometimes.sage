def orig(P,N):
    x=P[0]
    y=P[1]
    a=(8*(N+3)-x+y)/(2*(N+3)*(4-x))
    b=(8*(N+3)-x-y)/(2*(N+3)*(4-x))
    c=(-4*(N+3)-(N+2)*x)/((N+3)*(4-x))
    da=denominator(a)
    db=denominator(b)
    dc=denominator(c)
    l=lcm(da,lcm(db,dc))
    return [a*l,b*l,c*l]

ee = EllipticCurve([0,517,0,416,0])
P = ee(-416,4160)

for i in range(1,1000):
    u = orig(P*i,10)
    (a,b,c)=(u[0],u[1],u[2])
    if a > 0 and b > 0 and c > 0:
        print(a)
        print(b)
        print(c)
        break
