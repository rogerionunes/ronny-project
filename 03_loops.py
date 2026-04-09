# Trilha 03: repeticao com for e while.


def main() -> None:
    print("Tabuada do 5 com for:")
    for numero in range(0, 11):
        resultado = 5 * numero
        print(f"5 x {numero} = {resultado}")

    print("\nContagem com while:")
    contador = 1
    while contador <= 5:
        print(f"Contador: {contador}")
        contador += 1


if __name__ == "__main__":
    main()
