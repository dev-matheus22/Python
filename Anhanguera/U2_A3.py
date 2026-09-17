class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa('João', 25, 'Masculino')

print(pessoa1.apresentar())
print(pessoa1.aniversario())

# Herança

# A herança é um conceito da programação orientada a objetos que permite criar uma nova classe baseada em uma classe existente. 
# A nova classe herda os atributos e métodos da classe base, podendo 
# adicionar novos atributos e métodos ou sobrescrever os existentes.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

rex = Cachorro("Rex")
Whiskers = Gato("Whiskers")

print(rex.nome, "faz som:", rex.fazer_som())
print(Whiskers.nome, "faz som:", Whiskers.fazer_som())

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self): 
        return f"Veículo: {self.marca} {self.modelo}"

    def frear(self):
        return f"Veículo: {self.marca} {self.modelo}"

    def status(self):
        return f"Veículo: {self.marca} {self.modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def acelerar(self):
        return f"Carro: {self.marca} {self.modelo} está acelerando!"

    def frear(self):
        return f"Carro: {self.marca} {self.modelo} está freando!"

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def status(self):
        return f"Bicicleta: {self.marca} {self.modelo}, Tipo: {self.tipo}"     

carro1 = Carro("Toyota", "Corolla", 4)
bicicleta1 = Bicicleta("Caloi", "Elite", "Speed")

print(carro1.acelerar())
print(carro1.frear())
print(bicicleta1.acelerar())
print(bicicleta1.frear())