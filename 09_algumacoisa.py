# Trilha 08: classe e objeto.


class Aluno:
    def __init__(self, nome: str, nota: float) -> None:
        self.nome = nome
        self.nota = nota

    def verificar_status(self) -> str:
        if self.nota >= 7:
            return "Aprovado"
        return "Reprovado"


def main() -> None:
    aluno = Aluno("Ronny", 8.5)

    print(f"Nome: {aluno.nome}")
    print(f"Nota: {aluno.nota}")
    print(f"Status: {aluno.verificar_status()}")


if __name__ == "__main__":
    main()
