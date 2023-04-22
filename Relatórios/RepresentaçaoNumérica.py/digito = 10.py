digito = inp
base = 2
q = digito / base

while True:
    if q != 0:   
        q = q // base
        bin = q % base
        print(f"{bin:.0f}")
    else: break
    
