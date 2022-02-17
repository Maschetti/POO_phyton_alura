

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo {} do titular {}". format(self.__saldo, self.__titular))
        
    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor):
        return valor <= (self.__limite + self.__saldo)
        
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor passou o limite!")
        
    def tesnferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @staticmethod
    def codigo():
        return "001"
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite