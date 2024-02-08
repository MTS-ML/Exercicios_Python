from abc import ABC, abstractmethod


class Interface(ABC):

    @abstractmethod
    def play(self):
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')

    @abstractmethod
    def pause(self):
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')

    @abstractmethod
    def like(self):
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')


class Video(Interface):

    def __init__(self, titulo: str):
        self.__titulo: str = titulo
        self.__avaliacao: int = 0
        self.__views: int = 0
        self.__curtidas: int = 0
        self.__reproduzindo: bool = False

    # MÉTODO TOSTRING
    def __str__(self):
        return (f'Título: {self.get_titulo()}, Avaliação: {self.get_avaliacao()}\n'
                f'Views: {self.get_views()}, Curtidas: {self.get_curtidas()}, Reproduzindo: {self.get_reproduzindo()}')

    def get_titulo(self) -> str:
        return self.__titulo

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_avaliacao(self) -> int:
        return self.__avaliacao

    def set_avaliacao(self, avaliacao: int):
        nova = (self.get_avaliacao() + avaliacao) / self.get_views()
        self.__avaliacao = nova

    def get_views(self) -> int:
        return self.__views

    def set_views(self, views: int):
        self.__views = views

    def get_curtidas(self) -> int:
        return self.__curtidas

    def set_curtidas(self, curtidas: int):
        self.__curtidas = curtidas

    def get_reproduzindo(self) -> bool:
        return self.__reproduzindo

    def set_reproduzindo(self, reproduzindo: bool):
        self.__reproduzindo = reproduzindo

    #  MÉTODOS
    def play(self):
        self.set_reproduzindo(True)

    def pause(self):
        self.set_reproduzindo(False)

    def like(self):
        self.set_curtidas(self.get_curtidas() + 1)


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int, sexo: str):
        self._nome: str = nome
        self._idade: int = idade
        self.sexo: str = sexo
        self._experiencia: int = 0

    #  MÉTODO TOSTRING
    def __str__(self):
        return f'Nome: {self.get_nome()}, Idade: {self.get_idade()}, Sexo: {self.get_sexo()}, Experiência: {self.get_experiencia()}'

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_idade(self) -> int:
        return self._idade

    def set_idade(self, idade: int):
        self._idade = idade

    def get_sexo(self) -> str:
        return self.sexo

    def set_sexo(self, sexo: str):
        self.sexo = sexo

    def get_experiencia(self) -> int:
        return self._experiencia

    def set_experiencia(self, experiencia: int):
        self._experiencia = experiencia

    def ganhar_experiencia(self):
        pass


class Gafanhoto(Pessoa):

    def __init__(self, nome: str, idade: int, sexo: str, login: str):
        super().__init__(nome, idade, sexo)
        self.__login: str = login
        self.__total_assistido: int = 0

    #  MÉTODO TOSTRING
    def __str__(self):
        return f'{super().__str__()}\nLogin: {self.get_login()}, ' \
               f'Total Assistido: {self.get_total_assistido()}\n'

    def get_login(self) -> str:
        return self.__login

    def set_login(self, login: str):
        self.__login = login

    def get_total_assistido(self) -> int:
        return self.__total_assistido

    def set_total_assistido(self, total_assistido: int):
        self.__total_assistido = total_assistido

    def viu_mais_um(self):
        pass


class Visualizacao:

    def __init__(self, espectador: Gafanhoto, filme: Video):
        self.__espectador: Gafanhoto = espectador
        self.__filme: Video = filme
        self.__espectador.set_total_assistido(self.__espectador.get_total_assistido() + 1)
        self.__filme.set_views(self.__filme.get_views() + 1)

    # MÉTODO TOSTRING
    def __str__(self):
        return f'Espectador - {self.get_espectador()}\nFilme: {self.get_filme()}'

    def get_espectador(self) -> Gafanhoto:
        return self.__espectador

    def set_espectador(self, espectador: Gafanhoto):
        self.__espectador = espectador

    def get_filme(self) -> Video:
        return self.__filme

    def set_filme(self, filme: Video):
        self.__filme = filme

    def avaliar(self, nota_padrao=5, nota=None, porcentagem=None):
        if nota is not None:
            self.__filme.set_avaliacao(nota)
        elif porcentagem is not None:
            if porcentagem <= 20:
                total = 3
            elif porcentagem <= 50:
                total = 5
            elif porcentagem <= 90:
                total = 8
            else:
                total = 10
            self.__filme.set_avaliacao(total)
        else:
            self.__filme.set_avaliacao(nota_padrao)


if __name__ == '__main__':

    video1 = Video('Aula 1 de POO')
    video2 = Video('Aula 12 de PHP')
    video3 = Video('Aula 10 de HTML5')

    gafanhoto1 = Gafanhoto('Jubileu', 22, 'M', 'juba')
    gafanhoto2 = Gafanhoto('Creuza', 12, 'F', 'creu')

    visualizacao1 = Visualizacao(gafanhoto1, video1)  # JUBILEU ASSISTIU VIDEO DE POO
    visualizacao1.avaliar()
    print(visualizacao1.__str__())
    print()
    visualizacao2 = Visualizacao(gafanhoto1, video2)  # JUBILEU ASSISTIU VIDEO DE PHP
    visualizacao2.avaliar(None, None, 91)
    print(visualizacao2.__str__())
    print()
