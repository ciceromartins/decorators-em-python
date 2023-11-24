import time

def meuDecorator(funcao):
  def minhaFuncao(*args, **kwargs):
    inicio = time.time()
    resultado = funcao(*args, **kwargs)
    fim = time.time()
    print(f"A função {funcao.__name__} foi executada em {fim - inicio} segundos.")
    return resultado
  return minhaFuncao

@meuDecorator
def contaAteUmMilhao():
  for numero in range(1000000):
    numero += 1
    print(numero)

@meuDecorator
def contaAteDoisMilhoes():
  for numero in range(2000000):
    numero += 1
    print(numero)

contaAteDoisMilhoes()
