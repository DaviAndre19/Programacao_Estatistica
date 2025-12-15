import numpy as np
import matplotlib.pyplot as plt

#integral de 0 até 1 de 1/(1+x²), queremos mostrar que essa relação é igual a pi/4
def mc_padrao(n):
  soma=0
  for _ in range(n):
    u = np.random.uniform()
    soma+=1/(1+(u**2))
  media = soma/n
  pi = 4*media
  return pi

teste_pi = mc_padrao(100000)
print(teste_pi)

#y = u ou u²
def covariancia(n):
  soma=0
  for _ in range(n):
    u = np.random.uniform()
    soma+=((1/(1+(u**2))-(np.pi/4))*(u-0.5))
  cov = soma/n
  return cov

covariance = covariancia(10000)
c = (-covariance)/(1/12)
print(c)

def mc_controle(n): #Usando variáveis de controle
  soma = 0
  for _ in range(n):
    u = np.random.uniform()
    soma+=(1/(1+(u**2)))+c*(u-0.5)
  media = soma/n
  return media

teste_controle=mc_controle(100000)
print(teste_controle) 
print(np.pi/4) #Compare e veja que os 2 prints serão próximos um do outro

lista_x = [] #Usando MC Padrão
for _ in range(1000):
  teste = mc_padrao(1000)
  lista_x.append(teste)
lista_controle = [] #Usando variáveis de controle
for _ in range(1000):
  testec= mc_controle(1000)
  lista_controle.append(testec)
var_mc = np.var(lista_x)
var_controle = np.var(lista_controle)

print(var_mc)
print(var_controle) #ao fazer isso você verá que o uso de variáveis de controle reduz a variância absurdamente

def exemplo_21(n): #integral simples de e^(x), aqui se usa Monte Carlo Padrão, queremos mostrar que será igual a e - 1
  soma = 0
  for _ in range(n):
    u = np.random.uniform()
    soma+= np.exp(u)
  return soma/n

media_expo = exemplo_21(10000)
print(media_expo)

lista_controle = [] #Criamos uma lista para gerar variaveis exponenciais e uma lista(uniforme) que será utilizada ao calcularmos a covariancia e a relação Z=X + c*(Y-uy) em que c = -cov(X,Y)/Var(Y)
lista_uniforme = []

for _ in range(10000):
  u = np.random.uniform()
  lista_uniforme.append(u)
  expo = np.exp(u)
  lista_controle.append(expo)
covariancia = np.cov(lista_controle,lista_uniforme)
print(covariancia)

c = (-covariancia[0,1])/(covariancia[1,1])
print(c)

lista_padrao =[] #Uso de MC Padrão
lista_mc_controle = [] #Uso de Variáveis de controle
for _ in range(10000):
  u1 = np.random.uniform()
  z = np.exp(u1) + (c*(u1-0.5))
  lista_mc_controle.append(z)
  lista_padrao.append(np.exp(u1))
plt.hist(lista_padrao)
plt.hist(lista_mc_controle)

