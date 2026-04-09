# Trilha 06: leitura e escrita de arquivos.

from pathlib import Path


def main() -> None:
    caminho = Path("anotacoes.txt")

    # Escreve texto no arquivo.
    with caminho.open("w", encoding="utf-8") as arquivo:
        arquivo.write("Estudando Python\n")
        arquivo.write("Aprendendo arquivos\n")

    # Le o conteudo salvo.
    with caminho.open("r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    print("Conteudo do arquivo:")
    print(conteudo)


if __name__ == "__main__":
    main()
