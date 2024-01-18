class Caneta:

    def __init__(self, modelo: str, cor: str, ponta: float):
        self.__modelo: str = modelo
        self.__ponta: float = ponta
        self.__cor: str = cor
        self.__tampada: bool = True

    #  MODELO
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo: str):
        self.__modelo = modelo
        return modelo

    #  PONTA
    def get_ponta(self):
        return self.__ponta

    def set_ponta(self, ponta: float):
        self.__ponta = ponta
        return ponta

    #  COR
    def get_cor(self):
        return self.__cor

    def set_cor(self, cor: str):
        self.__cor = cor
        return cor

    #  TAMPADA
    def get_tampada(self):
        return self.__tampada

    def set_tampada(self, tampada):
        self.__tampada = tampada
        return tampada

    #  MÉTODOS
    def tampar(self, __tampada: bool):
        self.__tampada = True

    def destampar(self, __tampada: bool):
        self.__tampada = False

    def status(self):
        print(f'{"-" * 16}\n{"SOBRE A CANETA".center(16)}\n{"-" * 16}')
        print(f'Modelo: {self.get_modelo()}')
        print(f'Ponta: {self.get_ponta()}')
        print(f'Cor: {self.get_cor()}')
        print(f'Tampada: {self.get_tampada()}')


#caneta1 = Caneta()
caneta1 = Caneta('NIC', 'Amarelo', 0.4)
caneta2 = Caneta('kkk', 'Laranja', 1.5)

'''caneta1.set_modelo('BICCCC')
caneta1.set_ponta(0.555)'''

caneta1.status()
print()
caneta2.status()
