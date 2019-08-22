import self as self


class Pessoa:
    def __init__(self, nome, idade, genero, cep, telefone, rg):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cep = cep
        self.telefone = telefone
        self.rg = rg

class Medico(Pessoa):
    def __init__(self, nome, idade, genero, cep, telefone, rg):
    super.__init__('nome', 'idade', 'genero', 'cep', 'telefone', 'rg')
    self.crm = crm

    def crm(self):
        print('4686463')

class Paciente(Pessoa):
    def __init__(self, nome, idade, genero, cep, telefone, rg):
    super.__init__('nome', 'idade', 'genero', 'cep', 'telefone', 'rg')

    def sintoma(self):
        print('dor no peito')

Medico = Medico('Lucas', '45 anos', 'Não definido', '54524-7', '4569-5648', '65985658-8')
Paciente = Paciente('Maria do Socorro', '20 anos', 'Feminino', '456468-9', '4956-8765', '54986523-5')
Pessoa = Pessoa('nome', 'idade', 'genero', 'cep', 'telefone', 'rg')

print(medico.crm)
