class Caneta:

    def __init__(self):
        self.modelo: str = ""
        self.cor: str = ''
        self.__ponta: float = 0.0
        self._carga: int = 0
        self.__tampada: bool = True

    def _rabiscar(self):
        if self.__tampada:
            print('ERRO! Não posso rabiscar! A caneta está tampada.')
        else:
            print('Estou rabiscando')

    def status(self):
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Ponta: {self.__ponta}')
        print(f'Carga: {self._carga}')
        print(f'Está tampada? {"Sim" if self.__tampada else "Não"}')

    def tampar(self):
        self.__tampada = True

    def destampar(self):
        self.__tampada = False


# Exemplo de uso
objeto1 = Caneta()

objeto1.modelo = 'BIC'
objeto1.cor = 'Azul'
objeto1.__ponta = 0.5  # Atributo __ponta é acessado diretamente (não é a melhor prática)
objeto1._carga = 80
objeto1.tampar()  # Método para tampar a caneta
#objeto1.destampar()  # Método para destampar a caneta
objeto1.status()
objeto1._rabiscar()
