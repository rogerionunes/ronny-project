# Trilha 05: listas e dicionarios.


def main() -> None:
    # Lista: guarda varios valores em ordem.
    frutas = ["banana", "maca", "uva"]
    frutas.append("laranja")
    frutas.remove("banana")

    print("Lista de frutas:")
    for fruta in frutas:
        print(f"- {fruta}")

    # Dicionario: guarda pares de chave e valor.
    aluno = {
        "nome": "Ronny",
        "idade": 30,
        "curso": "Python",
    }

    print("\nDados do aluno:")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Curso: {aluno['curso']}")


if __name__ == "__main__":
    main()
