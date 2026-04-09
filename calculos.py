# Exemplo de calculos simples em Python.


def main() -> None:
    numero1 = 10
    numero2 = 5

    # Soma
    soma = numero1 + numero2
    print(f"Soma: {numero1} + {numero2} = {soma}")

    # Subtracao
    subtracao = numero1 - numero2
    print(f"Subtracao: {numero1} - {numero2} = {subtracao}")

    # Multiplicacao
    multiplicacao = numero1 * numero2
    print(f"Multiplicacao: {numero1} * {numero2} = {multiplicacao}")

    # Divisao
    divisao = numero1 / numero2
    print(f"Divisao: {numero1} / {numero2} = {divisao}")

    # Potencia
    potencia = numero1 ** numero2
    print(f"Potencia: {numero1} ** {numero2} = {potencia}")

    # Resto da divisao
    resto = numero1 % numero2
    print(f"Resto: {numero1} % {numero2} = {resto}")


if __name__ == "__main__":
    main()
