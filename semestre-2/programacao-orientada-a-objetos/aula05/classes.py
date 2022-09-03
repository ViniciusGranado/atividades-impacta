class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

    def identidade(self):
        return (f'Sou o livro {self.nome} e estou salvo no endereco'
                f' de memoria {id(self)}')


livro_1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien")
print("Livro 1: ", vars(livro_1))
print(livro_1.nome)
print(livro_1.autor)
print(livro_1.identidade())
