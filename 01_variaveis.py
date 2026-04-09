# Trilha 01: variaveis, tipos e operacoes basicas.


def main() -> None:
    # Variaveis guardam valores para usarmos depois.
    nome = "Ronny"
    idade = 30
    altura = 1.75
    estudando_python = True

    print("Exemplo de variaveis:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")
    print(f"Estudando Python? {estudando_python}")

    # Tambem podemos fazer calculos com variaveis numericas.
    ano_atual = 2026
    ano_nascimento = ano_atual - idade
    print(f"Ano aproximado de nascimento: {ano_nascimento}")


if __name__ == "__main__":
    main()
