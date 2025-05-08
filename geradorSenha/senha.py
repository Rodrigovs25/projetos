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
        return string.ascii_lowercase
    elif tipo == 2:
        return string.ascii_uppercase
    elif tipo == 3:
        return string.digits
    elif tipo == 4:
        return string.ascii_uppercase + string.digits
    elif tipo == 5:
        return string.ascii_lowercase + string.digits
    elif tipo == 6:
        return string.ascii_letters + string.digits
    elif tipo == 7:
        return string.ascii_letters + string.digits + string.punctuation
    else:
        print("Opção inválida. Gerando senha com letras minúsculas.")
        return string.ascii_lowercase

def gerarSenha(n, tipo):
    lista_de_caracteres = []

    # Adiciona n caracteres aleatórios à lista
    for i in range(n):
        lista_de_caracteres.append(random.choice(selecionarTipo(tipo)))

    # Junta todos os caracteres da lista em uma string (a senha final)
    senha = ''.join(lista_de_caracteres)
    return senha

def main():
    n = lerNumero()
    printMenu()
    tipo = lerTipo()
    senha = gerarSenha(n, tipo)

    print("\nSenha gerada:", senha)


main()
