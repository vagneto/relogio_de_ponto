#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

class Ponto:
    '''
    Classe que contem métodos necessários para registro de ponto laboral.
    '''
    
    def __init__(self, hora, minutos, segundos):
        '''
        Método construtor que inicializa os atributos: hora, minutos e segundos
        '''
        
        self.h = hora
        self.m = minutos
        self.s = segundos
        
    def __add__(self, other):
        
        ho = self.h + other.h
        mi = self.m + other.m
        se = self.s + other.s
        
        if se >= 60:
            mi += 1
            se = se - 60
            
        if mi >= 60:
            ho += 1
            mi = mi - 60
            
        return Ponto(ho, mi, se)
    
    def __sub__(self, other):
        
        ho = self.h - other.h
        mi = self.m - other.m
        se = self.s - other.s
        
        if se >= 60:
            mi += 1
            se = se - 60
            
        if mi >= 60:
            ho += 1
            mi = mi - 60
            
        return Ponto(ho, mi, se)
    
    def __gt__(self, other):
        
        if self.h > other.h:
            return True
            
        elif self.h == other.h and self.m > other.m:
            return True
        
        elif self.h == other.h and self.m == other.m and self.s > other.s:
            return True
        
        else:
            return False
        
    def __repr__(self):
        
        return f'{self.h:02d}:{self.m:02d}:{self.s:02d}'
########################################################

def ler_hora():
    '''
    Método para receber a hora digitada
    '''

    ok = False
    valor = 0
    while True:
        hora = input('Digite a hora: ')
        if hora.isnumeric():
            valor = int(hora)
            ok = True
        else:
            print('\nDigite apenas números inteiros: ')
        if ok:
            break

    valido = False
    hora_valida = 0
    while True:
        if int(valor) < 0 or int(valor) > 24:
            valor = input('Digite uma hora válida: ')
        else:
            valido = True
            hora_valida = int(valor)

        if valido:
            break

    return hora_valida
########################################################    

def ler_minutos():
    '''
    Método para receber os minutos digitados
    '''

    ok = False
    valor = 0
    while True:
        minutos = input('Digite os minutos: ')
        if minutos.isnumeric():
            valor = int(minutos)
            ok = True
        else:
            print('\nDigite apenas números inteiros: ')
        if ok:
            break

    valido = False
    minutos_validos = 0
    while True:
        if int(valor) < 0 or int(valor) > 59:
            valor = input('Digite um minuto válido: ')
        else:
            valido = True
            minutos_validos = int(valor)

        if valido:
            break

    return minutos_validos
#######################################################

def ler_segundos():
    '''
    Método para receber os segundos digitados
    '''

    ok = False
    valor = 0
    while True:
        segundos = input('Digite os segundos: ')
        if segundos.isnumeric():
            valor = int(segundos)
            ok = True
        else:
            print('\nDigite apenas números inteiros: ')
        if ok:
            break

    valido = False
    segundos_validos = 0
    while True:
        if int(valor) < 0 or int(valor) > 59:
            valor = input('Digite um número de segundos válidos: ')
        else:
            valido = True
            segundos_validos = int(valor)

        if valido:
            break

    return segundos_validos

uma_hora = Ponto(1, 0, 0)
dez_horas = Ponto(10, 0, 0)

print('\033[34m'+'############################'+'\033[0;0m')
print('\033[34m'+'######Relógio de Ponto######'+'\033[0;0m')
print('\033[34m'+'############################'+'\033[0;0m')
time.sleep(0.5)
print()

ok = False
inicio1 = None
saida1 = None
inicio2 = None
saida2 = None

while True:
    opcao = input('Digite 1 para inídio do dia, 2 para saída para o almoço, 3 para volta do almoço, 4 para fim do dia e 0 para cancelar: ')
    if opcao == '1':
        inicio1 = Ponto(ler_hora(), ler_minutos(), ler_segundos())
        print('\033[32m'+f'O início do seu dia foi em {inicio1}'+'\033[0;0m\n')
                    
    elif opcao == '2':
        while True:
            if inicio1 == None:
                print('\033[31m'+'Você ainda não registrou sua entrada. Reinicie o processo!'+'\033[0;0m\n')
                break
            else:
                saida1 = Ponto(ler_hora(), ler_minutos(), ler_segundos())
                print('\033[32m'+f'A saída do seu almoço foi em {saida1}'+'\033[0;0m\n')
                break
                
    elif opcao == '3':
        while True:
            if inicio1 == None or saida1 == None:
                print('\033[31m'+'Você ainda não registrou sua entrada ou saída para o almoço. Reinicie o processo!'+'\033[0;0m\n')
                break
            else:
                inicio2 = Ponto(ler_hora(), ler_minutos(), ler_segundos())
                if inicio2 - saida1 < uma_hora:
                    print('\033[31m'+f'Você não pode retornar agora pois ainda não completou uma hora de almoço. Você saiu às {saida1}'+'\033[0;0m\n')
                    break
                else:
                    print('\033[32m'+f'A volta do seu almoço foi em {inicio2}'+'\033[0;0m\n')
                    break
                
    elif opcao == '4':
        while True:
            if inicio1 == None or saida1 == None or inicio2 == None:
                print('\033[31m'+'Você ainda não registrou sua entrada ou saída para o almoço ou retorno do almoço. Reinicie o processo!'+'\033[0;0m\n')
                break
            else:
                saida2 = Ponto(ler_hora(), ler_minutos(), ler_segundos())
                print('\033[32m'+f'O fim do seu dia foi em {saida1}'+'\033[0;0m\n')
                jornada = ((saida2 - inicio2) + (saida1 - inicio1))
                print('\033[32m'+f'Sua jornada de trabalho foi de {jornada}'+'\033[0;0m\n')
                ok = True
                if jornada > dez_horas:
                    print('\033[31m'+'\033[1M'+'NA PRÓXIMA VEZ QUE ULTRAPASSAR DEZ HORAS DE TRABALHOS DIÁRIOS, PODE PEGAR SUAS COISAS E PASSAR NO RH'+'\033[1;1m\n')
                break
                
    elif opcao == '0':
        print('Você cancelou.')
        break
    
    if ok:
        break
        
## Encontrei as cores em wiki.python.org.br/CoresNoTerminal


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




