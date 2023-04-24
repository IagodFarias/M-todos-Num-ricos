import math

numero = input('digite o numero: ')
numero = float(numero)

frac , intNum = math.modf(numero)  
if numero > 9999.9:         
    M = 999999999.9
    c=100        
elif numero <0.00001:      
    M = 0.000001
    c=100
else:
        c = len(str(intNum)) - 2 
if c == 1:
            if intNum == 0:
              for j in range(0,5,1):
                    Mx = frac*pow(10,j+1)
                    print(f'o valor de Mx é: {Mx}')        
                    if Mx > 1:                      
                        M = round(Mx/pow(10,j),4)
                        print(f'o valor de M é: {M}')
                        print(f'o valor de c é: {c}')
                        c = -j
                        print(f'o valor de c é: {c}')
                        break
                    else:
                        Mx=Mx
    M0 = intNum/pow(10,c)
    M1 = frac/pow(10,c)
    M2= M0+M1
    M = round(M2 ,4)

print(frac, intNum)
print(c)
