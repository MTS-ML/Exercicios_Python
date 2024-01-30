class Pessoa:

    def __init__(self):
        self.__nome: str = None
        self.__idade: int = None
        self.__sexo: str = None

    def get_nome(self) -> str:
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

    # MÉTODO
    def fazer_aniversario(self):
        self.set_idade(self.get_idade() + 1)

    def status(self):
        print(f'Nome: {self.get_nome()}\n'
              f'Idade: {self.get_idade()}\n'
              f'Sexo: {self.get_sexo()}\n')


class Aluno(Pessoa):

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

    # MÉTODO
    def cancelar_matricula(self):
        print('matrícula será cancelada')


class Professor(Pessoa):

    __especialiade: str = None
    __salario: float = None

    def get_especialidade(self) -> str:
        return self.__especialiade

    def set_especialidade(self, especialidade: str):
        self.__especialiade = especialidade

    def get_salario(self) -> float:
        return self.__salario

    def set_salario(self, salario: float):
        self.__salario = salario

    # MÉTODO
    def receber_aumento(self, aumento: float):
        self.set_salario(self.get_salario() + aumento)


class Funcionario(Pessoa):

    __setor: str = None
    __trabalhando: bool = None

    def get_setor(self) -> str:
        return self.__setor

    def set_setor(self, setor: str):
        self.__setor = setor

    def get_trabalhando(self) -> bool:
        return self.__trabalhando

    def set_trabalhando(self, trabalhando: bool):
        self.__trabalhando = trabalhando

    #  MÉTODO
    def mudar_trabalho(self):
        self.set_trabalhando(False if self.get_trabalhando() else True)


if __name__ == '__main__':
    pessoa1 = Pessoa()
    aluno1 = Aluno()
    professor1 = Professor()
    funcionario1 = Funcionario()

    pessoa1.set_nome('Pedro')
    pessoa1.set_sexo('M')

    aluno1.set_nome('Maria')
    aluno1.set_idade(18)
    aluno1.set_curso('T.I.')

    professor1.set_nome('Cláudio')
    professor1.set_salario(2500.75)

    funcionario1.set_nome('Fabiana')
    funcionario1.set_sexo('M')
    funcionario1.set_setor('Estoque')

    pessoa1.status()
    aluno1.status()
    professor1.status()
    funcionario1.status()
