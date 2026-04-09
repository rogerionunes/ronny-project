# Exemplo de funcoes um pouco mais completas em Python.

def somar(a: float, b: float) -> float:
    # Recebe dois numeros e devolve a soma.
    return a + b


def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    # Soma as tres notas e divide por 3.
    return (nota1 + nota2 + nota3) / 3


def verificar_aprovacao(media: float) -> str:
    # Usa uma condicao para decidir o resultado.
    if media >= 7:
        return "Aprovado"
    return "Reprovado"


def exibir_resultado(nome: str, media: float, status: str) -> None:
    # Mostra um resumo final na tela.
    print(f"Aluno: {nome}")
    # `:.3f` diz ao Python para mostrar apenas 1 casa decimal.
    print(f"Media: {media:.1f}")
    print(f"Status: {status}")


def main() -> None:
    resultado_soma = somar(8, 4)
    print(f"Resultado da soma: {resultado_soma}")

    media = calcular_media(7.5, 8.0, 6.5)

    status = verificar_aprovacao(media)

    exibir_resultado("Ronny", media, status)


if __name__ == "__main__":
    main()
