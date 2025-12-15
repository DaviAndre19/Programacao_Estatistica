import numpy as np
import matplotlib.pyplot as plt
import time

def bernoulli(p):
  u = np.random.uniform()
  if u<=p:
    return 1
  else:
    return 0

x = bernoulli(0.3)
print(x)

def gerador_bernoulli(n,p):
  lista=[]
  y=0
  while y<n:
    w = bernoulli(p)
    lista.append(w)
    y+=1
  return lista
ber=gerador_bernoulli(1000,0.3)
print(ber)
media = sum(ber)/len(ber)
print(media)

bin = np.random.binomial(1000,0.3)
print(bin)
media_binomial=bin/1000
print(media_binomial)

plt.hist(ber)

for i,k in enumerate(ber):
  print(i,k)

def gerador_uniforme(m,p):
  u = []
  g_ber = gerador_bernoulli(m,p)
  for index, k in enumerate(g_ber):
    valor = k/(2**(index+1))
    u.append(valor)
  return sum(u)
unif=gerador_uniforme(1000,0.5)
print(unif)

listaunif=[]
for _ in range(1000):
  value=gerador_uniforme(20,0.5)
  listaunif.append(value)
print(listaunif)

plt.hist(listaunif)

start=time.time()

def gerador_binomial(n, p):
    lista=[]
    for _ in range(n):
      x=bernoulli(p)
      lista.append(x)
    return sum(lista)

lista_binomial=[]
for _ in range(100000):
  y=gerador_binomial(20,0.5)
  lista_binomial.append(y)
print(lista_binomial)
end=time.time()
print(end-start)

start=time.time()
def inversa_recursiva(n, p):
    u=np.random.uniform()
    pi=(1-p)**n
    f=pi
    def recursao(i, pi, f):
        if u <= f:
            return i
        pi1 = ((n - i) / (i + 1)) * (p / (1 - p)) * pi
        f1 = f + pi1
        return recursao(i + 1, pi1, f1)
    return recursao(0, pi, f)


lista_inv=[]
for i in range(100000):
  inv = inversa_recursiva(20,0.5)
  lista_inv.append(inv)
print(lista_inv)
end=time.time()

print(end-start)

lista_inversa = []
for _ in range(100):
  x = inversa_recursiva(2000,0.25)
  lista_inversa.append(x)
print(lista_inversa)

media = sum(lista_inversa)/len(lista_inversa)
print(media)

plt.hist(lista_binomial)

plt.hist(lista_inversa)

plt.hist(lista_binomial)
plt.hist(lista_inversa)
