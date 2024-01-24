class InterfaceControlador:
    #  MÉTODOS
    def ligar(self):
        pass

    def desligar(self):
        pass

    def abrir_menu(self):
        pass

    def fechar_menu(self):
        pass

    def mais_volume(self):
        pass

    def menos_volume(self):
        pass

    def ligar_mudo(self):
        pass

    def desligar_mudo(self):
        pass

    def play(self):
        pass

    def pause(self):
        pass


class ControleRemoto(InterfaceControlador):

    def __init__(self):
        self.__volume: int = 50
        self.__ligado: bool = False
        self.__tocando: bool = False

    #  MÉTODOS ASSESSORES
    def __get_volume(self):
        return self.__volume

    def __set_volume(self, volume: int):
        self.__volume = volume

    def __get_ligado(self):
        return self.__ligado

    def __set_ligado(self, ligado: bool):
        self.__ligado = ligado

    def __get_tocando(self):
        return self.__tocando

    def __set_tocando(self, tocando: bool):
        self.__tocando = tocando

    #  MÉTODOS
    def ligar(self):
        self.__set_ligado(True)

    def desligar(self):
        self.__set_ligado(False)

    def abrir_menu(self):
        if not self.__get_ligado():
            print('TV desligada')
        else:
            print(f'Ligado? {self.__get_ligado()}\n'
                  f'Tocando? {self.__get_tocando()}\n'
                  f'Volume: {self.__get_volume()} ', end='')
            for c in range(0, self.__get_volume(), 10):
                print('|', end='')
            print()

    def fechar_menu(self):
        if self.__get_ligado():
            print('Fechando menu')

    def mais_volume(self):
        if self.__get_ligado():
            self.__set_volume(self.__get_volume() + 5)
        else:
            print('TV desligada')

    def menos_volume(self):
        if self.__get_ligado():
            self.__set_volume(self.__get_volume() - 5)
        else:
            print('TV desligada')

    def ligar_mudo(self):
        if self.__get_ligado() and self.__get_volume() > 0:
            self.__set_volume(0)

    def desligar_mudo(self):
        if self.__get_ligado() and self.__get_volume() == 0:
            self.__set_volume(50)

    def play(self):
        if self.__get_ligado() and not self.__get_tocando():
            self.__set_tocando(True)
        else:
            print('Não consegui reproduzir')

    def pause(self):
        if self.__get_ligado() and self.__get_tocando():
            self.__set_tocando(False)
        else:
            print('Não consegui pausar')


controle1 = ControleRemoto()

controle1.ligar()
controle1.play()
#controle1.pause()
controle1.mais_volume()
#controle1.menos_volume()
#controle1.ligar_mudo()
#controle1.desligar_mudo()
#controle1.desligar()

controle1.abrir_menu()
#controle1.fechar_menu()
