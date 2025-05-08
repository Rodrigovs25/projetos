# 🔐 Gerador de Senhas em Python

Este é um programa simples de gerador de senhas escrito em Python. Ele permite ao usuário:

- Definir o número de caracteres da senha.
- Escolher o tipo de caracteres que a senha deve conter.

## 📋 Menu de opções

Após informar o número de caracteres, o usuário pode escolher entre os seguintes tipos de senha:

1. Apenas letras minúsculas
2. Apenas letras maiúsculas
3. Apenas números 
4. Letras maiúsculas + números  
5. Letras minúsculas + números
6. Letras maiúsculas + Letras minúsculas + números
7. Completo (maiúsculas, minúsculas, números, símbolos)

## 🧠 Como funciona

O programa utiliza a biblioteca `random` para gerar caracteres aleatórios com base nas opções selecionadas. Também utiliza a biblioteca `string` para obter conjuntos padrão de caracteres como letras e números.

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo, por exemplo `gerador_senha.py`.
3. Execute no terminal:

```bash
python3 gerador_senha.py
