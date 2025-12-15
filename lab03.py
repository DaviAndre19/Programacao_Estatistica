import numpy as np
import matplotlib.pyplot as plt

def exponencial_inversa(lam):
  u = np.random.uniform()
  assert lam>0, "Lambda n é maior que 0"
  x = (1/(-lam))*(np.log(1-u))

  return x

amostra_exponencial=[] #simulando a distribuição e colocando em uma lista
for _ in range(1000):
  k = exponencial_inversa(2)
  amostra_exponencial.append(float(k))
print(amostra_exponencial)

plt.hist(amostra_exponencial) #mostrando em um histograma

padrao = [] # simulando a distribuição com a função padrão do numpy
for _ in range(1000):
  padrao1 = np.random.exponential(1/2)
  padrao.append(padrao1)
print(padrao)

plt.hist(padrao) #mostrando em um histograma

plt.hist(amostra_exponencial, label = "Exponencial por inversa", color ="blue")
plt.hist(padrao, label = 'Exponencial do Python', color = "red")
plt.legend()
plt.show() # comparando ambas em um grafico

def exponencial_teorica(x, lam=1): #função da exponencial teorica 
  return np.exp(-lam*x)*lam

amostrak=[] #criando uma lista como amostra da distribuição acima
for _ in range(1000):
  meio3 = exponencial_inversa(2)
  amostrak.append(float(meio3))
print(amostrak)

x = np.linspace(0,5,1000) #cria mil valores de 0 até 5 e coloca em um histograma, ao lado da densidade padrão do gráfico(density=True)
plt.plot(x, exponencial_teorica(x))
plt.hist(amostrak, density=True)

def geometrica(p):
  u = np.random.uniform()
  x=np.floor((np.log(1-u)/np.log(1-p)))+1
  return x
def exponencial_geo(n,lam): #simulação da exponencial por meio de geometricas
  t=geometrica(lam/n)
  x1= t/n
  return x1

def exponencial_poisson(u): #simulação de uma distribuição poisson via distribuição exponencial
  tempo = 0
  contagem = 0
  while tempo<1:
    tempo+=exponencial_inversa(u)
    contagem+=1
  return contagem - 1
  
amostra_poisson =[] # criando uma amostra com a função que criei
for _ in range(10**4):
  poisson = exponencial_poisson(4)
  amostra_poisson.append(poisson)
print(amostra_poisson)

amostra2_poisson=[] #criando outra amostra com a função própria do numpy
for _ in range(10**4):
  poisson2 = np.random.poisson(4)
  amostra2_poisson.append(poisson2)
print(amostra2_poisson)

plt.hist(amostra_poisson, label = 'Amostra criada', color = "red") #comparando ambos os gráficos
plt.hist(amostra2_poisson, label = "Poisson do Python", color = "blue")
plt.legend()
plt.show()

#Usando np.mean e np.var em ambas as amostras, é perceptível ver que os valores estarão extremamente próximos
