# Trilha 04: funcoes com parametros e retorno.


def calcular_area_retangulo(base: float, altura: float) -> float:
    return base * altura


def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    return "Obesidade"


def main() -> None:
    area = calcular_area_retangulo(6, 4)
    print(f"Area do retangulo: {area}")

    imc = calcular_imc(120, 1.75)
    classificacao = classificar_imc(imc)
    print(f"IMC: {imc:.1f}")
    print(f"Classificacao: {classificacao}")


if __name__ == "__main__":
    main()
