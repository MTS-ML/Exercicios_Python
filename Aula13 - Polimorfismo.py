from abc import ABC, abstractmethod
from typing import Optional


class Animal(ABC):

    def __init__(self):
        self.__peso: Optional[float] = None
        self.__idade: Optional[int] = None
        self.__membros: Optional[int] = None

    def get_peso(self) -> float:
        return self.get_peso()

    def set_peso(self, peso: float):
        self.__peso = peso

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, idade: int):
        self.__idade = idade

    def get_membros(self) -> int:
        return self.__membros

    def set_membros(self, membros: int):
        self.__membros = membros

    @abstractmethod
    def emitir_som(self):
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')


class Mamifero(Animal, ABC):

    __cor_pelo: str = None

    def get_cor_pelo(self) -> str:
        return self.__cor_pelo

    def set_cor_pelo(self, cor_pelo: str):
        self.__cor_pelo = cor_pelo

    def emitir_som(self):
        print('Som de mamífero')


class Lobo(Mamifero, ABC):

    def emitir_som(self):
        print('Lobo: Auuuuuuuuuuuu!')


class Cachorro(Lobo, ABC):

    def emitir_som(self):
        print('Cachorro: Au AU!')

    # EM PYTHON, NÃO EXISTE SUPORTE PARA POLIMORFISMO DE SOBRECARGA,
    # NECESSÁRIO PASSAR TODOS OS PARÂMETROS EM UMA MESMA FUNÇÃO,
    # SENDO ALGUNS OPCIONAIS.
    '''def reagir(self, frase: str):
        if frase == 'toma comida' or frase == 'Olá':
            print('Abanar e latir')
        else:
            print('Rosnar')

    def reagir(self, hora: int):
        if hora < 12:
            print('Abanar')
        elif hora >= 18:
            print('Ignorar')
        else:
            print('Abanar e latir')

    def reagir(self, dono: bool):
        if dono:
            print('Abanar')
        else:
            print('Ronar e latir')

    def reagir(self, idade: int, peso: float):
        if idade < 5:
            if peso < 10:
                print('Abanar')
            else:
                print('Latir')
        else:  # IDADE >= 5
            if peso < 10:
                print('Rosnar')
            else:
                print('Ignorar')'''

    @staticmethod
    def reagir(frase=None, hora=None, dono=None, idade=None, peso=None):
        if frase is not None:
            if frase == 'toma comida' or frase == 'Olá':
                print('Abanar e latir')
            else:
                print('Rosnar')

        elif hora is not None:
            if hora < 12:
                print('Abanar')
            elif hora >= 18:
                print('Ignorar')
            else:
                print('Abanar e latir')

        elif dono is not None:
            if dono:
                print('Abanar')
            else:
                print('Ronar e latir')

        elif idade is not None and peso is not None:
            if idade < 5:
                if peso < 10:
                    print('Abanar')
                else:
                    print('Latir')
            else:  # IDADE >= 5
                if peso < 10:
                    print('Rosnar')
                else:
                    print('Ignorar')


if __name__ == '__main__':

    cachorro1 = Cachorro()
    mamifero1 = Mamifero()
    lobo1 = Lobo()

    lobo1.emitir_som()
    cachorro1.emitir_som()
    print()

    cachorro1.reagir('Olá')
    print()

    cachorro1.reagir(None, 11)
    print()

    cachorro1.reagir(None, None, True)
    cachorro1.reagir(None, None, False)
    print()

    cachorro1.reagir(None, None, None, 4, 9)
    cachorro1.reagir(None, None, None, 6, 12)
    print()
