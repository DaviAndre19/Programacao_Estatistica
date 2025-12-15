import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def poisson_recursivo(lam):
  u=np.random.uniform(0,1)
  i=0
  p=np.exp(-lam)
  f=p
  while u>f:
    i+=1
    p=(lam/i)*p
    f+=p
  return i
amostra1=[]
for j in range(1000):
  k=poisson_recursivo(1)
  amostra1.append(k)
print(amostra1)

def bernoulli(p):
  u = np.random.uniform(0,1)
  if u<=p:
    return 1
  else:
    return 0

def binomial_recursiva(n, p):
    u=np.random.uniform()
    pi=(1-p)**n
    f=pi
    def recursao(i, pi, f):
        if u <= f:
            return i
        else:
          pi1 = ((n - i)/(i + 1))*(p /(1 - p))*pi
          f1= f + pi1
          return recursao(i + 1, pi1, f1)
    return recursao(0, pi, f)

nova_poisson = poisson_recursivo(10) # Comparando a poisson recursiva e a binomial recursiva, os valores ficarão próximos um do outro
binomial = binomial_recursiva(1000,0.01)

print(nova_poisson)
print(binomial)

amostra_x=[]
for _ in range(1000):
  k=binomial_recursiva(1000,0.01)
  amostra_x.append(k)
print(amostra_x)

amostra_y=[]
for _ in range(1000):
  k=poisson_recursivo(10)
  amostra_y.append(k)
print(amostra_y)

plt.hist(amostra_x)
plt.hist(amostra_y)

def geo_ingenua(p):
    ber=bernoulli(p)
    x=0
    while ber !=1:
      ber = bernoulli(p)
      x+=1
    return x

def geo_inversa(p):
  u = np.random.uniform(0,1)
  x=np.floor((np.log(1-u))/(np.log(1-p)))+1

  return x
start = time.time()

ingenua=[]

for _ in range(10**4):
  k=geo_ingenua(0.001)
  ingenua.append(k)
print(ingenua)

end = time.time()

print(f"Tempo: {end-start}")

inicio=time.time()

inversa = []
for _ in range(10**4):
  y=geo_inversa(0.001)
  inversa.append(y)
print(inversa)
final=time.time()

print(f"Tempo: {final-inicio}")

geo_numpy = np.random.geometric(p=0.001, size=10**4)
print(geo_numpy)

plt.hist(geo_numpy,label = "Função do Numpy", color ="blue")
plt.hist(ingenua, label = "Geo Ingenua", color = "red")
plt.hist(inversa, label = "Geo Inversa", color = "green")

plt.legend()
plt.show()

def bernoulli(p):
  u = np.random.uniform()
  if u<=p:
    return 1
  else:
    return 0
def gerador_bernoulli(n,p):
  lista=[]
  y=0
  while y<n:
    w = bernoulli(p)
    lista.append(w)
    y+=1
  return lista

def Neg_Bin_bern(r,p): #gerando binomial negativa via bernoulli
  suc=0
  ensaios=0
  while r>suc:
    k=bernoulli(p)
    ensaios+=1
    if k==1:
      suc+=1
  return ensaios

def Neg_Bin_geo(r,p):
  x=0
  for _ in range(r):
    xi=geo_inversa(p)
    x+=xi
  return x

def Neg_Bin_Rec(r,p): #binomial negativa via recursão
  u=np.random.uniform(0,1)

  def recursao(n,pr,F):
    if u<=F:
      return n
    else:
      pr=pr*(((1-p)*n)/(n-r+1))
      n+=1
      F+=pr
    return recursao(n,pr,F)
  return recursao(r,p**r,p**r)

start=time.time() #relação de otimização, comparando o tempo
lista1=[]
for _ in range(10**5):
  valor = Neg_Bin_bern(5,0.3)
  lista1.append(valor)
print(lista1)
end=time.time()
print(f"Tempo: {end-start}")

start=time.time()
lista2=[]
for _ in range(10**5):
  valor = Neg_Bin_geo(5,0.3)
  lista2.append(valor)
print(lista2)
end=time.time()
print(f"Tempo: {end-start}")

start=time.time()
lista3=[]
for _ in range(10**5):
  valor = Neg_Bin_Rec(5,0.3)
  lista3.append(valor)
print(lista3)
end=time.time()
print(f"Tempo: {end-start}")

#Em geral, o metodo recursivo será melhor, com a exceção para caso r seja um valor muito elevado, pois haverá um número alto de recursões

def yates(lista):
  copia_lista=lista.copy()
  N=len(copia_lista)
  for i in range(N):
    u = np.random.uniform()
    k = int(np.floor(((u*(N-i+1)))+i))-1
    copia_lista[i], copia_lista[k] = copia_lista[k], copia_lista[i]
  return copia_lista

def hipergeometrica(lista,n, valor):
  amostra = yates(lista)
  amostra = amostra[:n]
  return amostra.count(valor)
