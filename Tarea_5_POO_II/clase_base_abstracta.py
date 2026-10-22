from abc import ABC, abstractmethod
from decimal import Decimal

class CuentaBancaria(ABC):
    def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self._cbu = cbu
        self.saldo = saldo_inicial  # Pasa por el setter

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nuevo_titular):
        if not nuevo_titular.strip():
            raise ValueError("Error: El titular no puede estar vacío.")
        self._titular = nuevo_titular

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        saldo_decimal = Decimal(str(nuevo_saldo))
        if saldo_decimal < 0:
            raise ValueError("Error: El saldo no puede ser menor a cero.")
        self._saldo = saldo_decimal

    def depositar(self, monto: float):
        monto_decimal = Decimal(str(monto))
        if monto_decimal <= 0:
            raise ValueError("Error: El monto a depositar debe ser mayor a cero.")
        self.saldo += monto_decimal
        print(f"Depósito exitoso de ${monto_decimal}. Nuevo saldo: ${self.saldo}")

    def __str__(self):
        tipo_cuenta = self.__class__.__name__.upper()
        return f"[{tipo_cuenta}] TITULAR: {self.titular} | CBU: {self._cbu} | SALDO: ${self._saldo}"

    @abstractmethod
    def extraer(self, monto: float):
        pass