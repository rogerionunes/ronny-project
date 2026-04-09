# Trilha 07: tratamento de erros com try e except.


def dividir(numero1: float, numero2: float) -> float:
    return numero1 / numero2


def main() -> None:
    try:
        resultado = dividir(10, 0)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Nao e possivel dividir por zero.")
    finally:
        print("Fim do exemplo de tratamento de erro.")


if __name__ == "__main__":
    main()
