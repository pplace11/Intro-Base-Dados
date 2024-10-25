#x,y = 10, 8
#if x==y:
#    print('x tem valor de y')
#elif x%2:
#    print('x é par')
#elif x==10:
#    print('x tem valor de 10')
#else:
#    print('x nao é y')

#nota=[14.5, 10.0, 5.7]

#for el in nota:
#    if el >= 10:
#       print(f'O aluno passou com notas: {el}')
#    else:
#        print(f'O aluno nao passou')

def validate_pin():
    #Definir tetativas e pin de cartao
    pin, tentativa = 1234, 0

    #Rumo logico
    while tentativa<3:
        _pin=int(input('Indica o seu pin: '))
        if pin == _pin:
            res = 'Codigo Aceito'
            break
        else:
            res = 'Codigo Errado'
            tentativa += 1
        return res
    else:
        res = f'Número de tentativas excedidas, {tentativa}'
    return res
resultado =  validate_pin()
print(validate_pin())