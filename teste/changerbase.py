
#calculadora de decimal pra binário

digito = int(input("digite um número: "))
base = 2
q = digito / base
print(f"{q}")

while True:
    if q != 0:   
        q = q // base
        bin = q % base
    else:
        bin = 1
        break
    print(f"{bin:.0f}")    
    #print(f"{q}")    