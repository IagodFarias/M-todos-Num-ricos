import math
  #F(10, 6, −3, 3)
def flutuante(numero):
    frac , intNum = math.modf(numero)   # função math.modf retorna a parte fracionária e a parte inteirado 
                                        #número decimal recebido como entrada A variável frac armazena a 
                                        #parte fracionária, enquanto intNum armazena a parte inteira do número
    if numero > 299.9:         #define os casos de overflow
        M = 22222
        c=100        
    elif numero <0.001:       #define os casos de underflow
        M = 0.00001
        c=100
    else:
        c = len(str(intNum))-3     #Calcula a quantidade de dígitos na parte inteira, é subtraido de 2
                                    # pq queremos tirar o zero e o ponto
        if c == 1:
            if intNum == 0:
                for j in range(0,6,1):
                    Mx = frac*pow(10,j+1)           #Mx ==  mantissa de x
                    if Mx > 1:                      #Calcula o valor de Mx, que é a parte fracionária do núm
                                                    #multiplicada por 10 elevado a j+1.
                        M = round(Mx/pow(10,j),6)
                        c = -j
                        break
                    else:
                        Mx=Mx
        M0=intNum/pow(10,c)
        M1=frac/pow(10,c)
        M2=M0+M1
        M=round(M2 ,6)
            
    return M, c #M é a mantissa (números signficativos)
                # c é o expoente    

xs = input('digite o numero: ')
x = float(xs)

Mantissa , Expoente = flutuante(x)

if Mantissa == 999.9:
    print("Overflow")
elif Mantissa == 0.001:
    print("Underflow")
else:
    print("F(10,6,-3,3): " + str(float(Mantissa)) + "e" + str(int(Expoente)))
