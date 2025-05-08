import random
import string

def lerNumero():
    print("=== Gerador de Senha ===")
    n = int(input("Digite a quantidade de caracteres da senha: "))
    return n

def printMenu():
    print("\nEscolha o tipo de senha:")
    print("1 - Letras minúsculas")
    print("2 - Letras maiúsculas")
    print("3 - Números")
    print("4 - Letras maiúsculas + números")
    print("5 - Letras minúsculas + números")
    print("6 - Letras maiúsculas + Letras minúsculas + números")
    print("7 - Completo (maiúsculas, minúsculas, números, símbolos)")

def lerTipo():
    tipo = int(input("Opção: "))
    return tipo

def selecionarTipo(tipo):
    if tipo == 1:
        caracteres = string.ascii_lowercase
    elif tipo == 2:
        caracteres = string.ascii_uppercase
    elif tipo == 3:
        caracteres = string.digits
    elif tipo == 4:
        caracteres = string.ascii_uppercase + string.digits
    elif tipo == 5:
        caracteres = string.ascii_lowercase + string.digits
    elif tipo == 6:
        caracteres = string.ascii_letters + string.digits
    elif tipo == 7:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Opção inválida. Gerando senha com letras minúsculas.")
        caracteres = string.ascii_lowercase

    return caracteres

def gerarSenha(n, tipo):
    caracteres = selecionarTipo(tipo)
    senha = ''.join(random.choice(caracteres) for _ in range(n))
    return senha

# Menu
def main():
    n = lerNumero()
    printMenu()
    tipo = lerTipo()
    senha = gerarSenha(n, tipo)

    print("\nSenha gerada:", senha)

if __name__ == "__main__":
    main()
