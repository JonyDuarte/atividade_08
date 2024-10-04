"""Crie um programa que faça o cadastro de vários usuários dentro de uma única lista. Ao final, o programa deverá exibir na tela todos os dados de todos os usuários cadastrados. Os dados do usuário a serem cadastrados serão os seguintes:

- Nome
- Idade
- CPF
- E-mail
- Profissão
- Tipo Sanguíneo
- Peso
- Altura"""


# Lista
usuarios = []

while True:
    # dicionário para armazenamento
    usuario = {}

    usuario["Nome"] = input("Digite o nome do usuário: ")
    usuario["Idade"] = input("Digite a idade do usuário: ")
    usuario["CPF"] = input("Digite o CPF do usuário: ")
    usuario["E-mail"] = input("Digite o e-mail do usuário: ")
    usuario["Profissão"] = input("Digite a profissão do usuário: ")
    usuario["Tipo Sanguíneo"] = input("Digite o tipo sanguíneo do usuário: ")
    usuario["Peso"] = input("Digite o peso do usuário (kg): ")
    usuario["Altura"] = input("Digite a altura do usuário (metros): ")

    # adiciona o usuário a lista
    usuarios.append(usuario)

    # Continuar cadastrando
    continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
    if continuar != "s":
        break

# Saída dos dados dos usuários cadastrados
print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(f"Nome: {usuario['Nome']}")
    print(f"Idade: {usuario['Idade']}")
    print(f"CPF: {usuario['CPF']}")
    print(f"E-mail: {usuario['E-mail']}")
    print(f"Profissão: {usuario['Profissão']}")
    print(f"Tipo Sanguíneo: {usuario['Tipo Sanguíneo']}")
    print(f"Peso: {usuario['Peso']}")
    print(f"Altura: {usuario['Altura']}\n")

