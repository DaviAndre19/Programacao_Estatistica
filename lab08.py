#ESTUDO DE MONTE CARLO COM VARIÁVEIS ANTITÉTICAS

#abaixo, como simular uma integral de 1 até 2 de e^x, tanto pelo método padrão quanto pelo uso de variáveis antitéticas


import numpy as np
import matplotlib.pyplot as plt


def mc_padrao(n):
  soma=0
  for _ in range(n):
    x = np.random.uniform(1,2)
    soma+=np.exp(x)
  return soma/n

def antitetica(n):
    soma=0
    for _ in range(n):
      x = np.random.uniform(0,1)
      y=x
      ya=1-x
      soma+=(np.exp(y+1)+np.exp((ya+1)))/2
    return soma/n

#simulando criando 2 listas e aplicando os 2 métodos

lista1=[]
for _ in range(100):
  k = mc_padrao(1000)
  lista1.append(k)
print(lista1)

lista2=[]
for _ in range(100):
  l=antitetica(1000)
  lista2.append(l)
print(lista2)

#use np.var em ambas as listas e vc verá que o uso de variáveis antitéticas diminui a variância

plt.hist(lista1)
plt.hist(lista2) #histograma comparando ambos os métodos, a lista 2(em que se usa variáveis antitéticas) está mais próxima da média

#Exercício sobre como calcular a integral de e^(-x²) em que X~Exp(1)

def exponencial(lam):
  u = np.random.uniform()
  k=(-1/lam)*np.log(1-u)
  return k

def exp_mcpadrao(n): #simulando via Monte Carlo Padrão
  soma=0
  for _ in range(n):
    e = exponencial(1)
    soma+=np.exp(-(e**2))
  return soma/n

def exp_antit(n): #Usando variáveis antitéticas
  soma=0
  for _ in range(n):
    u = np.random.uniform()
    x = np.log(u)
    xa=np.log(1-u)
    soma+=(np.exp(-(x**2))+np.exp(-(xa**2)))/2
  return soma/n

lista3=[] #se coloca amostras via MC Padrão
lista4=[] #se coloca amostras via variáveis antitéticas
for _ in range(1000):
  a3=exp_mcpadrao(100)
  a4=exp_antit(100)
  lista3.append(a3)
  lista4.append(a4)
print(lista3)
print(lista4)

#Use np.var em ambas as listas e verifique que a lista 4 possuiu uma variância menor

plt.hist(lista3)
plt.hist(lista4) # ao plotar os histogramas, percebemos que essa lista estará com uma variância menor, poderemos ver visualmente

#Simulando uma Normal(2,1)
#Código abaixo sobre como simular N(0,1)
def bernoulli(p):
  u = np.random.uniform()
  if u<=p:
    return 1
  else:
    return 0

def f(x):
  f = np.exp(-x**2 /2) / (2*3.1415)**.5
  return f
def g(x):
  g = np.exp(-x)
  return g

def halfnormal():
  y = exponencial(1)
  u = np.random.uniform()
  c = (2*(2.72)/3.14)**0.5
  funcao = f(y)/(g(y)*c)
  if u>funcao:
    return halfnormal()
  else:
    return y

def normal(n=1):
  amostra=[]
  for _ in range(n):
    meio = halfnormal()
    ber = bernoulli(0.5)
    if ber == 1:
      amostra.append(meio)
    else:
      amostra.append(-1*(meio))
  return amostra

def normal_antitetica(n):
  soma = 0
  for _ in range(n):
    z = normal(n=1)[0]
    y1=1+((2**0.5)*z)
    y2=1+((2**0.5)*(-z))
    soma+= ((np.exp(-(y1**2)+1) + np.exp(-(y2**2)+1))/2)
  return soma/n

def normal_mc(n): #montecarlo Padrão, note que ocorreu a "despadronização", lembre se que Z=(X-u)/sigma -> X=Z*sigma + u
  soma = 0
  for _ in range(n):
    k = normal(n=1)[0]
    j = (k*(2**0.5))+1
    soma+=np.exp(-(j**2)+1)
  return soma/n

from joblib import Parallel, delayed #professor passou esse comando em sala de aula
amostra_padrao = Parallel(n_jobs=-1)(delayed(normal_mc)(1000) for i in range(1000))
amostra_antitetica = Parallel(n_jobs=-1)(delayed(normal_antitetica)(1000) for i in range(1000))

print(amostra_padrao)
print(amostra_antitetica)

#Coloque np.var(amostra_padrao) e np.var(amostra_antitetica) e verá que o uso de variáveis antitéticas terá uma variância menor
plt.hist(amostra_padrao) #azul
plt.hist(amostra_antitetica) #plote o histograma e veja que isso realmente ocorre
