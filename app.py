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
usuarios = [
    {
# Coleta de dados do usuário
        atributos [0]: input("Nome: "),
        atributos [1]: input("Idade: "),
        atributos [2]: input("CPF: "),
        atributos [3]: input("E-mail: "),
        atributos [4]: input("Profissão: "),
        atributos [5]: input("Tipo Sanguíneo: "),
        atributos [6]: input("Peso (kg): "),
        atributos [7]: input("Altura (m): ")
    }
]

usuario = {}
for atributo in atributos:
    usuario[atributo] = (f"Informe o valor do campo{atributo}: ")
usuarios.append(usuario)

for usuario in usuarios:
    print("")
    for atributo in atributos:

