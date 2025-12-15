import numpy as np
import matplotlib.pyplot as plt


#O PROBLEMA ERA SOBRE COMO SIMULAR A PROBABILIDADE X>10, DADO QUE X SEGUE DIST NORMAL(0,1), FAZEMOS ISSO VIA IMPORTANCE SAMPLING
#X=Normal(0,1)
def exponencial(lam):
  u = np.random.uniform()
  x = (-1/lam)*np.log(1-u)
  return x

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

def bernoulli(p):
  u = np.random.uniform()
  if u<=p:
    return 1
  else:
    return 0

def normal(n=1): #somente um elemento da distribuição normal
  amostra=[]
  for _ in range(n):
    meio = halfnormal()
    ber = bernoulli(0.5)
    if ber == 1:
      amostra.append(meio)
    else:
      amostra.append(-1*(meio))
  return amostra

def normal_density(x,u):
  return np.exp((-(x-u)**2)/2)/((2*np.pi)**0.5)

def indicadora(x,a):
  return x>a

n=10000
soma=0
for j in range(n): #AO SIMULARMOS ESSE CODIGO, ACHAMOS O VALOR DE P(X>10) EM QUE X SEGUE UMA DISTRIBUIÇÃO NORMAL(0,1)
  x = normal(n=1)[0]
  soma+=indicadora2(x+10,10)* normal_density(x+10,0) / normal_density(x+10,10)
print(soma/n)

#ABAIXO, O PROBLEMA MUDA, SERÁ SOBRE COMO SIMULAR A FUNÇÃO 10*e^(-5*(x-5)^4)

def h(x):
  h = (10*(np.exp(-5*((x-5)**4))))
  return h

def f_g(x):
  soma=0
  for _ in range(1000):
    y = normal(n=1)[0]
    g = h(y-5)
    fg = normal_density(x,0)/g
    soma+=fg
  return soma/n

eixo=np.linspace(-10,10,1000) # 1000 pontos entre -10 e 10
plt.plot(eixo,10*normal_density(eixo,0))
plt.plot(eixo,10*normal_density(eixo,5))

