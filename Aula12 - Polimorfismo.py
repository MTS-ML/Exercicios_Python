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
    def locomover(self) -> str:
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')

    @abstractmethod
    def alimentar(self) -> str:
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')

    @abstractmethod
    def emitir_som(self) -> str:
        raise NotImplementedError('Método abstrato, deve ser implementado nas subclasses')


class Mamifero(Animal, ABC):

    __cor_pelo: str = None

    def get_cor_pelo(self) -> str:
        return self.__cor_pelo

    def set_cor_pelo(self, cor_pelo: str):
        self.__cor_pelo = cor_pelo

    def locomover(self):
        print('Mamífero Correndo')

    def alimentar(self):
        print('Mamífero mamando')

    def emitir_som(self):
        print('Som de mamífero')


class Reptil(Animal, ABC):
    __cor_escama: str = None

    def get_cor_escama(self) -> str:
        return self.__cor_escama

    def set_cor_escama(self, cor_escama: str):
        self.__cor_escama = cor_escama

    def locomover(self):
        print('Réptil rastejando')

    def alimentar(self):
        print('Péptil comendo vegetais')

    def emitir_som(self):
        print('Som de réptil')


class Peixe(Animal, ABC):
    __cor_escama: str = None

    def get_cor_escama(self) -> str:
        return self.__cor_escama

    def set_cor_escama(self, cor_escama):
        self.__cor_escama = cor_escama

    @staticmethod
    def soltar_bolha():
        print('Soltou uma bolha')

    def locomover(self):
        print('Peixe nadando')

    def alimentar(self):
        print('Peixe se alimentando')

    def emitir_som(self):
        print('Peixe não faz som')


class Ave(Animal, ABC):

    __cor_pena: str = None

    def get_cor_pena(self) -> str:
        return self.__cor_pena

    def set_cor_pena(self, cor_pena: str):
        self.__cor_pena = cor_pena

    @staticmethod
    def fazer_ninho():
        print('Construiu o ninho')

    def locomover(self):
        print('Ave voando')

    def alimentar(self):
        print('Ave se alimentando')

    def emitir_som(self):
        print('Som de ave')


class Canguru(Mamifero):

    @staticmethod
    def usar_bolsa():
        print('Usando a bolsa')

    def locomover(self):
        print('Canguru pulando')


class Cachorro(Mamifero):

    @staticmethod
    def enterrar_osso():
        print('Cachorro enterrando osso')

    @staticmethod
    def abanar_rabo():
        print('Cachorro abanando o rabo')


class Tartaruga(Reptil):

    def locomover(self):
        print('Tartaruga andando')


class Cobra(Reptil):
    pass


class Goldfish(Peixe):
    pass


class Arara(Ave):
    pass


if __name__ == '__main__':
    '''m = Mamifero()
    r = Reptil()
    p = Peixe()
    a = Ave()

    m.set_peso(85.3)
    m.set_idade(2)
    m.set_membros(4)
    m.locomover()
    print()

    p.set_peso(0.35)
    p.set_idade(1)
    p.set_membros(0)
    p.locomover()
    p.alimentar()
    p.soltar_bolha()
    p.emitir_som()
    print()

    a.set_peso(0.89)
    a.set_idade(2)
    a.set_membros(2)
    a.locomover()
    a.alimentar()
    a.emitir_som()
    a.fazer_ninho()'''

    ave1 = Ave()
    peixe1 = Peixe()
    mamifero1 = Mamifero()
    canguru1 = Canguru()
    cachorro1 = Cachorro()

    mamifero1.locomover()
    mamifero1.alimentar()
    mamifero1.emitir_som()
    print()

    canguru1.locomover()
    canguru1.alimentar()
    canguru1.emitir_som()
    canguru1.usar_bolsa()
    print()

    cachorro1.locomover()
    cachorro1.alimentar()
    cachorro1.emitir_som()
    cachorro1.abanar_rabo()
    print()

    ave1.locomover()
    peixe1.locomover()
    print()

    arara1 = Arara()
    arara1.locomover()
