class ContaBanco:

    def __init__(self):
        self.num_conta: int = None
        self._tipo: str = None
        self.__dono: str = None
        self.__saldo: float = 0
        self.__status: bool = False

    #  MÉTODOS ASSESSORES
    def get_num_conta(self):
        return self.num_conta

    def set_num_conta(self, num_conta: int):
        self.num_conta = num_conta

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: str):
        self._tipo = tipo

    def get_dono(self):
        return self.__dono

    def set_dono(self, dono: str):
        self.__dono = dono

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo: float):
        self.__saldo = saldo

    def get_status(self):
        return self.__status

    def set_status(self, status: bool):
        self.__status = status

    #  MÉTODOS
    def estado_atual(self):
        print(f'{"-" * 20}\n'
              f'Conta: {self.get_num_conta()}\n'
              f'Tipo: {self.get_tipo()}\n'
              f'Dono: {self.get_dono()}\n'
              f'Saldo: R${self.get_saldo()}\n'
              f'Status conta: {self.get_status()}\n'
              f'{"-" * 20}')

    def abrir_conta(self, tipo: str):
        self.set_tipo(tipo)
        self.set_status(True)
        if self.get_tipo() == 'CC':
            self.set_saldo(self.get_saldo() + 50)
            print('Conta aberta com sucesso!')
        elif self.get_tipo() == 'CP':
            self.set_saldo(self.get_saldo() + 150)
            print('Conta aberta com sucesso!')
        else:
            self.set_status(False)
            print('ERRO! Não foi possível abrir a conta')

    def fechar_conta(self):
        if self.get_saldo() != 0:
            print(f'Não é possível fechar a conta, saldo de R${self.get_saldo()}')
        else:
            self.set_status(False)
            print('Conta encerrada!')

    def depositar(self, valor: float):
        if self.get_status():
            self.set_saldo(self.get_saldo() + valor)
            print(f'Depósito realizado na conta de {self.get_dono()}')
        else:
            print('Não é possível acessar essa conta.')

    def sacar(self, valor: float):
        if self.get_status() and self.get_saldo() > 0:
            if valor > self.get_saldo():
                print(f'ERRO! Saque permitido de no máximo R${self.get_saldo()}')
            else:
                self.set_saldo(self.get_saldo() - valor)
                print('Saque realizado com sucesso.')
        else:
            print('ERRO! Não é possível sacar dinheiro da sua conta')

    def pagar_mensalidade(self):
        valor: float = 0
        if self.get_tipo() == 'CC':
            valor = 12
        elif self.get_tipo() == 'CP':
            valor = 20

        if self.get_status(): #and self.get_saldo() > valor:
            print(f'Mensalidade paga por {self.get_dono()}')
            self.set_saldo(self.get_saldo() - valor)
        else:
            print('ERRO! Não é possível pagar a mensalidade da sua conta')


if __name__ == '__main__':

    pessoa1 = ContaBanco()
    pessoa1.set_num_conta(1111)
    pessoa1.set_dono('Jubileu')
    pessoa1.abrir_conta('CC')
    pessoa1.depositar(100)
    pessoa1.sacar(140)
    pessoa1.pagar_mensalidade()
    pessoa1.fechar_conta()

    print()

    pessoa2 = ContaBanco()
    pessoa2.set_num_conta(2222)
    pessoa2.set_dono('Creuza')
    pessoa2.abrir_conta('CP')
    pessoa2.depositar(500)
    pessoa2.sacar(100)

    pessoa1.estado_atual()
    pessoa2.estado_atual()
