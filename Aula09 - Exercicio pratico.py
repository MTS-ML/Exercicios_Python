from typing import Optional


class Pessoa:

    def __init__(self, nome: str, idade: int, sexo: str):
        self.__nome: str = nome
        self.__idade: int = idade
        self.__sexo: str = sexo

    def get_nome(self) -> Optional[str]:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, idade: int):
        self.__idade = idade

    def get_sexo(self) -> str:
        return self.__sexo

    def set_sexo(self, sexo: str):
        self.__sexo = sexo

    #  MÉTODO
    def fazer_aniversario(self):
        self.set_idade(self.get_idade() + 1)


#  --------- INTERFACE ------------
class InterfacePublicacao:

    def abrir(self):
        pass

    def fechar(self):
        pass

    def folhear(self, pagina):
        pass

    def avancar_pagina(self):
        pass

    def voltar_pagina(self):
        pass


class Livro(InterfacePublicacao):

    def __init__(self, titulo: str, autor: str, total_paginas: int, leitor: Pessoa):
        self.__titulo: str = titulo
        self.__autor: str = autor
        self.__total_paginas: int = total_paginas
        self.__pagina_atual: int = 0
        self.__aberto: bool = False
        self.__leitor: Optional[Pessoa] = leitor

    # Métodos Getter
    def get_titulo(self) -> Optional[str]:
        return self.__titulo

    def set_titulo(self, titulo: Optional[str]):
        self.__titulo = titulo

    def get_autor(self) -> Optional[str]:
        return self.__autor

    def set_autor(self, autor: Optional[str]):
        self.__autor = autor

    def get_total_paginas(self) -> Optional[int]:
        return self.__total_paginas

    def set_total_paginas(self, total_paginas: Optional[int]):
        self.__total_paginas = total_paginas

    def get_pagina_atual(self) -> Optional[int]:
        if self.__pagina_atual > self.get_total_paginas():
            print(f'ERRO! Livro possui {self.get_total_paginas()} páginas')
        else:
            return self.__pagina_atual

    def set_pagina_atual(self, pagina_atual: Optional[int]):
        if self.__pagina_atual > self.get_total_paginas():
            print(f'ERRO! Livro possui {self.get_total_paginas()} páginas!')
        else:
            self.__pagina_atual = pagina_atual

    def get_aberto(self) -> Optional[bool]:
        return self.__aberto

    def set_aberto(self, aberto: Optional[bool]):
        self.__aberto = aberto

    def get_leitor(self) -> Optional[Pessoa]:
        return self.__leitor

    def set_leitor(self, leitor: Optional[Pessoa]):
        self.__leitor = leitor

    def detalhes(self):
        print(f'{"-" * 31}\n'
              f'Livro: {self.get_titulo()}\n'
              f'Autor: {self.get_autor()}\n'
              f'Total de páginas: {self.get_total_paginas()}\n'
              f'Página atual: {self.get_pagina_atual()}\n'
              f'Está aberto? {self.get_aberto()}\n'
              f'Leitor: {self.get_leitor().get_nome()}\n')

    def abrir(self):
        self.set_aberto(True)

    def fechar(self):
        self.set_aberto(False)

    def folhear(self, pagina: int):
        if not self.get_aberto():
            print('ERRO! Livro está fechado')
        elif self.__pagina_atual > self.get_total_paginas():
            print(f'ERRO! Livro possui {self.get_total_paginas()}')
        else:
            self.set_pagina_atual(pagina)

    def avancar_pagina(self):
        if self.get_aberto():
            self.set_pagina_atual(self.get_pagina_atual() + 1)
        else:
            print('ERRO! Livro fechado')

    def voltar_pagina(self):
        self.set_pagina_atual(self.get_pagina_atual() - 1)


if __name__ == '__main__':

    pessoa1 = Pessoa('Mateus', 28, 'M')
    pessoa2 = Pessoa('Maria', 25, 'F')

    livro1 = Livro('POO', 'Curso em Vídeo', 600, pessoa1)
    livro2 = Livro('Clean Code', 'Autor X', 850, pessoa1)

    livro1.abrir()
    livro1.folhear(599)
    livro1.avancar_pagina()
    livro1.detalhes()

    livro2.abrir()
    livro2.folhear(200)
    livro2.avancar_pagina()
    livro2.folhear(851)
    livro2.detalhes()
