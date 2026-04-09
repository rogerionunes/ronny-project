# Trilha 02: condicoes com if, elif e else.


def verificar_aprovacao(media: float) -> str:
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    return "Reprovado"


def main() -> None:
    media = 6.2
    resultado = verificar_aprovacao(media)

    print(f"Media do aluno: {media:.1f}")
    print(f"Resultado: {resultado}")

    numero = 8
    if numero % 2 == 0:
        print(f"{numero} e par")
    else:
        print(f"{numero} e impar")


if __name__ == "__main__":
    main()
