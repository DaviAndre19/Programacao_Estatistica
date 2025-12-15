import numpy as np
import matplotlib.pyplot as plt
#SIMULAÇÃO DA DISTRIBUIÇÃO NORMAL VIA MÉTODO DE ACEITAÇÃO-REJEIÇÃO
def exponencial(lam):
  u=np.random.uniform()
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

def normal():
  amostra=[]
  for _ in range(10**3):
    meio = halfnormal()
    ber = bernoulli(0.5)
    if ber == 1:
      amostra.append(meio)
    else:
      amostra.append(-1*(meio))
  return amostra

amostra1=normal() #plotando o gráfico da distribuição Normal(0,1)
print(amostra1)
plt.hist(amostra1)
plt.show()

#USANDO NP.MEAN E NP.VAR NA AMOSTRA, OS VALORES ESTARÃO PRÓXIMOS DE 0 E 1, RESPECTIVAMENTE

#SIMULANDO A FUNÇÃO 0.5*Sen(x), com x>0 e menor que pi, via método de aceitação-rejeição

def f(x):
  f = 0.5*np.sin(x)
  return f
  
def g(x):
  g = 1/3.1415
  return g

def amostragem(contador=1):
  cont = contador
  u = np.random.uniform()
  y = np.random.uniform(0,3.1415)
  funcao = f(y)/(g(y)*(3.1415/2))
  if u>funcao:
    return amostragem(contador = cont + 1)
  else:
    return y, cont

def amostragem_while():
  cont = 0
  u = 1
  quot = 0
  while u>quot:
    u = np.random.uniform()
    y = np.random.uniform(0,3.1415)
    quot = f(y)/(g(y)*(3.1415/2))
    cont += 1
  return y, cont

lista_amostra=[]
list_cont = []
for _ in range(10**4):
  kk, cont = amostragem_while()
  lista_amostra.append(kk)
  list_cont.append(cont)
print(lista_amostra)
print(list_cont)

plt.hist(lista_amostra, density=True) #Histograma da função, em conjunto da função densidade da mesma
plt.show()

