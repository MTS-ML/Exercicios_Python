from abc import ABC  # IMPORTA UMA CLASSE ABSTRATA - ABSTRACTED BASE CLASS
from typing import Optional


class Pessoa(ABC):  # CLASSE ABSTRATA

    def __init__(self):
        self._nome: Optional[str] = None
        self.__idade: Optional[int] = None
        self.__sexo: Optional[str] = None

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, idade: int):
        self.__idade = idade

    def get_sexo(self) -> str:
        return self.__sexo

    def set_sexo(self, sexo: str):
        self.__sexo = sexo

    def fazer_aniversario(self):
        pass

    def __str__(self):
        print(f'Nome: {self.get_nome()}\n'
              f'Idade: {self.get_idade()}\n'
              f'Sexo: {self.get_sexo()}\n')


class Visitante(Pessoa):  # HERANÇA DE IMPLEMENTAÇÃO OU HERANÇA POBRE
    pass


class Aluno(Pessoa):  # HERANÇA PARA DIFERENÇA
    # CLASSES FINAIS EM PYTHON NÃO TEM UMA CARACTERÍSTICA NATIVA,
    # A CONVENÇÃO PARA INDICAR CLASSE FINAL É O DOCSTRING.

    """
    --- EXEMPLO --- ESSA CLASSE É FINAL E NÃO DEVE SER HERDADA  --- EXEMPLO ---
    """

    __matricula: int = None
    __curso: str = None

    def get_matricula(self) -> int:
        return self.__matricula

    def set_matricula(self, matricula: int):
        self.__matricula = matricula

    def get_curso(self) -> str:
        return self.__curso

    def set_curso(self, curso: str):
        self.__curso = curso

    def pagar_mensalidade(self):
        print(f'Pagando mensalidade de {self._nome}')


class Professor(Pessoa):

    __especialidade: str = None
    __salario: float = 4000

    def get_especialidade(self) -> str:
        return self.__especialidade

    def set_especialidade(self, especialidade: str):
        self.__especialidade = especialidade

    def get_salario(self) -> float:
        return self.__salario

    def set_salario(self, salario: float):
        self.__salario = salario

    #  MÉTODO
    def receber_aumento(self, aumento: float):
        self.set_salario(self.get_salario() + aumento)


class Bolsista(Aluno):

    __bolsa: float = None

    def get_bolsa(self) -> float:
        return self.__bolsa

    def set_bolsa(self, bolsa: float):
        self.__bolsa = bolsa

    def renovar_bolsa(self):
        print(f'Renovando bolsa de {self._nome}')

    # @Override - MÉTODO SOBREPOSTO -  EM PYTHON NÃO É NECESSÁRIO USAR OVERRIDE.
    def pagar_mensalidade(self):
        print(f'{self._nome} é bolsista. Pagamento facilitado')


class Tecnico(Aluno):

    __registro_profissional: int = None

    def get_registro_profissional(self) -> int:
        return self.__registro_profissional

    def set_registro_profissional(self, n_registro: int):
        self.__registro_profissional = n_registro

    #  MÉTODO
    def praticar(self):
        print('Praticando profissão')


if __name__ == '__main__':
    # p1 = Pessoa()
    visitante1 = Visitante()
    aluno1 = Aluno()
    bolsista1 = Bolsista()
    professor1 = Professor()
    tecnico1 = Tecnico()

    visitante1.set_nome('Juvenal')
    visitante1.set_idade(22)
    visitante1.set_sexo('M')
    visitante1.__str__()

    aluno1.set_nome('Cláudio')
    aluno1.set_matricula(1111)
    aluno1.set_curso('T.I')
    aluno1.set_idade(16)
    aluno1.set_sexo('M')
    aluno1.pagar_mensalidade()

    bolsista1.set_matricula(1112)
    bolsista1.set_nome('Jubileu')
    bolsista1.set_bolsa(12.5)
    bolsista1.set_sexo('M')
    bolsista1.pagar_mensalidade()

    professor1.set_nome('Nome_Professor')
    professor1.set_especialidade('Programação')
    print(professor1.get_salario())
    professor1.receber_aumento(500)
    print(professor1.get_salario())
    print(professor1.get_especialidade())

    tecnico1._nome = 'Mateus'
    print(tecnico1.get_nome())
    tecnico1.praticar()
