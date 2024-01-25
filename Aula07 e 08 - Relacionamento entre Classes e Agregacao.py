from typing import Optional


class Lutador:
    def __init__(self, nome: str, nacionalidade: str, idade: int, altura: float, peso: float,
                 vitorias: int, derrotas: int, empates: int):
        self.__nome: str = nome
        self.__nacionalidade: str = nacionalidade
        self.__idade: int = idade
        self.__altura: float = altura
        self.__peso: float = peso
        self.__categoria: Optional[str] = None
        self.__vitorias: int = vitorias
        self.__derrotas: int = derrotas
        self.__empates: int = empates
        # CATEGORIA NÃO ESTAVA SENDO CHAMADA ANTES DE ADICIONAR
        self.__set_categoria()

    #  MÉTODOS ASSESSORES
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade: int):
        self.__idade = idade

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura: float):
        self.__altura = altura

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso: float):
        self.__peso = peso
        self.__set_categoria()

    def get_categoria(self):
        return self.__categoria

    def __set_categoria(self):
        if self.get_peso() < 52.2:
            self.__categoria = 'Inválido'
        elif self.get_peso() <= 70.3:
            self.__categoria = 'leve'
        elif self.get_peso() <= 83.9:
            self.__categoria = 'médio'
        elif self.get_peso() <= 120.2:
            self.__categoria = 'pesado'
        else:
            self.__categoria = 'Inválido'

    def get_vitorias(self):
        return self.__vitorias

    def set_vitorias(self, vitorias: int):
        self.__vitorias = vitorias

    def get_derrotas(self):
        return self.__derrotas

    def set_derrotas(self, derrotas: int):
        self.__derrotas = derrotas

    def get_empates(self):
        return self.__empates

    def set_empates(self, empates: int):
        self.__empates = empates

    # MÉTODOS
    def apresentar(self):
        print(f'Lutador: {self.get_nome()}\n'
              f'Origem: {self.get_nacionalidade()}\n'              
              f'Idade: {self.get_idade()} anos\n'
              f'Altura: {self.get_altura()}m\n'
              f'Peso: {self.get_peso()}kg\n')

    def status(self):
        print(f'{self.get_nome()} é um peso {self.get_categoria()}\n'              
              f'Vitórias: {self.get_vitorias()}\n'
              f'Derrotas: {self.get_derrotas()}\n'
              f'Empates: {self.get_empates()}\n')

    def ganhar_luta(self):
        self.set_vitorias(self.get_vitorias() + 1)

    def perder_luta(self):
        self.set_derrotas(self.get_derrotas() + 1)

    def empatar_luta(self):
        self.set_empates(self.get_empates() + 1)


#  ------EXERCÍCIO DA AULA 08-------
class Luta:

    def __init__(self):
        self.__desafiado: Optional[Lutador] = None
        self.__desafiante: Optional[Lutador] = None
        self.__rounds: Optional[int] = None
        self.__aprovada: Optional[bool] = None

    def get_desafiado(self):
        return self.__desafiado

    def set_desafiado(self, lutador: Lutador):
        self.__desafiado = lutador

    def get_desafiante(self):
        return self.__desafiante

    def set_desafiante(self, desafiante: Lutador):
        self.__desafiante = desafiante

    def get_rounds(self):
        return self.get_rounds()

    def set_rounds(self, rounds: int):
        self.__rounds = rounds

    def get_aprovada(self):
        return self.__aprovada

    def set_aprovada(self, aprovada):
        self.__aprovada = aprovada

    #  MÉTODOS
    def marcar_luta(self, lutadorx: Lutador, lutadory: Lutador):
        if lutadorx.get_categoria() == lutadory.get_categoria() and lutadorx != lutadory:
            self.set_aprovada(True)
            self.set_desafiado(lutadorx)
            self.set_desafiante(lutadory)
        else:
            self.set_aprovada(False)
            self.set_desafiado(Optional[None])
            self.set_desafiante(Optional[None])

    def lutar(self):
        from random import randint
        if self.get_aprovada():
            print('--- DESAFIADO ---')
            self.get_desafiado().status()
            print('--- DESAFIANTE --- ')
            self.get_desafiante().status()

            resultado = randint(0, 2)
            if resultado == 0:
                print('Luta empatou')
                self.get_desafiado().empatar_luta()
                self.get_desafiante().empatar_luta()
            elif resultado == 1:  # DESAFIADO GANHOU
                print(f'{self.get_desafiado().get_nome()} VENCEU!')
                self.get_desafiado().ganhar_luta()
                self.get_desafiante().perder_luta()
            else:  # DESAFIANTE GANHOU
                print(f'{self.get_desafiante().get_nome()} VENCEU!')
                self.get_desafiante().ganhar_luta()
                self.get_desafiado().perder_luta()
        else:
            print('Luta não pode ocorrer')


if __name__ == '__main__':

    lutador1 = Lutador('Pretty Boy', 'França', 31, 1.75, 68.9,
                       11, 2, 1)

    lutador2 = Lutador('Putscript', 'Brasil', 29, 1.68, 57.8,
                       14, 2, 3)

    lutador3 = Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9,
                       12, 2, 1)

    lutador4 = Lutador('Dead Code', 'Austrália', 28, 1.93, 81.6,
                       13, 0, 2)

    lutador5 = Lutador('Ufocobol', 'Brasil', 37, 1.70, 119.3,
                       5, 4, 3)

    lutador6 = Lutador('Nerdaard', 'EUA', 30, 1.81, 105.7,
                       12, 2, 4)

    luta = Luta()
    luta.marcar_luta(lutador5, lutador6)
    luta.lutar()
    print()
    lutador5.status()
    lutador6.status()
