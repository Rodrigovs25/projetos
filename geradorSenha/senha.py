import random
import string

def gerar_senha(n):
    # Conjunto de caracteres possíveis na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha escolhendo n caracteres aleatórios
    senha = ''.join(random.choice(caracteres) for _ in range(n))
    return senha

# Lê o número de caracteres da senha
n = int(input("Digite a quantidade de caracteres da senha: "))
senha_gerada = gerar_senha(n)
print("Senha gerada:", senha_gerada)
