# `def` cria uma funcao em Python.
# Aqui estamos criando uma funcao chamada `main`.
# O `-> None` quer dizer que essa funcao nao devolve nenhum valor.
def main() -> None:
    # `print(...)` mostra um texto na tela.
    # Neste caso, ele escreve "Hello, world!" no terminal.
    print("Hello, world!")

# `__name__` e uma variavel especial do Python.
# Quando executamos este arquivo diretamente com `python3 main.py`,
# o valor dela vira "__main__".
# Esse `if` serve para dizer:
# "se este arquivo foi executado diretamente, rode a funcao main()".
if __name__ == "__main__":
    # Aqui estamos chamando a funcao `main`.
    # Isso faz o Python entrar na funcao e executar o `print`.
    main()
