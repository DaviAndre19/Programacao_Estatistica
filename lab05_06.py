#Este laboratório tinha como objetivo simular exemplos do material do Professor Thiago Rodrigo Ramos (Métodos Computacionais) via Monte Carlo Padrão
import numpy as np

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

def normal(n=1): #simula somente um elemento da distribuição Normal(0,1)
  amostra=[]
  for _ in range(n):
    meio = halfnormal()
    ber = bernoulli(0.5)
    if ber == 1:
      amostra.append(meio)
    else:
      amostra.append(-1*(meio))
  return amostra

#integral de 0 até 1 de e^(-x²)
def integral_e(n):
  soma=0
  for _ in range(n):
    u = np.random.uniform()
    euler=np.exp(-((u)**2))
    soma+=euler
  media = soma/n

  return media

def pi(n):
  soma = 0
  for _ in range(n):
    x = np.random.uniform()
    y = np.random.uniform()
    if (x**2)+(y**2)<=1:
      soma+=1
  return (4*soma)/n

def med_var(n): #media e variancia de uma distribuição uniforme(0,1)
  amostra=[]
  media=0
  for _ in range(n):
    y = np.random.uniform()
    amostra.append(y)
    media+=y
  media = media/n
  var=0
  for j in range(n):
    var+=((amostra[j]-media)**2)
  var=var/(n-1)

  return media, var

def ex_13(n): #exponencial de -(x²+y²)
  integral=0
  for _ in range(n):
    x = np.random.uniform()
    y=np.random.uniform()
    integral += np.exp(-((x**2)+(y**2)))
  integral = integral/n
  return integral

def ex_14(n): #exponencial de e^(-(x))
  media=0
  for _ in range(n):
    x = exponencial(1)
    media+=np.exp(-(x))
  media = media/n
  return media

def ex_15(n): #integral de 0 até infinito de (e^(-x))/(1+x)
  media = 0
  for _ in range(n):
    x = exponencial(1)
    media+=1/(1+x)
  media = media/n
  return media

def ex_16(n): #integral de 0 até infinito de sen(x)/x 
  media = 0
  for _ in range(n):
    x = exponencial(1)
    media+=(np.sin(x))/(x*(np.exp(-(x))))
  media = media/n
  return media

def ic_seno(n): #intervalo de confiança de 95% de confiança de f(x) = sen(x)/(x*(e^(-x)))
  amostra=[]
  media=0
  var=0
  for _ in range(n):
    x = exponencial(1)
    amostra.append(x)
    media+=(np.sin(x))/((x)*(np.exp(-(x))))
  media = media/n
  for j in range(n-1):
    var+=(amostra[j]-media)**2
  var = var/(n)
  ic_sup=media+(1.96*((var**0.5)/(n**0.5)))
  ic_inf=media-(1.96*((var**0.5)/(n**0.5)))

  return ic_inf,ic_sup
