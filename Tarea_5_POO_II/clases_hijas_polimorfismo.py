from decimal import Decimal
from clase_base_abstracta import CuentaBancaria

# 1. CUENTA AHORRO
class CuentaAhorro(CuentaBancaria):
    def extraer(self, monto: float):
        monto_decimal = Decimal(str(monto))
        if monto_decimal <= 0:
            raise ValueError("Error: El monto a extraer debe ser mayor a cero.")
        if monto_decimal > self.saldo:
            raise ValueError("Error: Saldo insuficiente en la caja de ahorros.")
        
        self.saldo -= monto_decimal
        print(f"Extracción exitosa de ${monto_decimal}. Saldo actual: ${self.saldo}")

    def aplicar_interes(self):
        """Suma al saldo un interés del 0.1% (tasa = 0.001)."""
        interes = self.saldo * Decimal("0.001")
        self.saldo += interes
        print(f"Interés aplicado (${interes:.2f}). Nuevo saldo: ${self.saldo}")


# 2. CUENTA CORRIENTE
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0, limite_descubierto: float = 500.0):
        super().__init__(titular, cbu, saldo_inicial)
        self.limite_descubierto = Decimal(str(limite_descubierto))

    def extraer(self, monto: float):
        monto_decimal = Decimal(str(monto))
        if monto_decimal <= 0:
            raise ValueError("Error: El monto a extraer debe ser mayor a cero.")
        
        # Validamos contra el descubierto permitido (saldo + límite)
        if monto_decimal > (self.saldo + self.limite_descubierto):
            raise ValueError("Error: El monto supera el saldo disponible y el límite de descubierto.")
        
        # Modificamos _saldo directamente para permitir el saldo negativo 
        # sin que el setter del padre lo bloquee injustamente.
        self._saldo -= monto_decimal
        print(f"Extracción con descubierto de ${monto_decimal}. Saldo actual: ${self._saldo}")


# 3. CUENTA CHEQUE
class CuentaCheque(CuentaBancaria):
    def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0, costo_emision: float = 50.0):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = Decimal(str(costo_emision))

    def extraer(self, monto: float):
        monto_decimal = Decimal(str(monto))
        if monto_decimal <= 0:
            raise ValueError("Error: El monto a extraer debe ser mayor a cero.")
        
        total_a_descontar = monto_decimal + self.costo_emision
        
        if total_a_descontar > self.saldo:
            raise ValueError(f"Error: Saldo insuficiente para cubrir el monto y el costo de emisión (${self.costo_emision}).")
        
        self.saldo -= total_a_descontar
        print(f"Emisión de cheque por ${monto_decimal} (Costo administrativo: ${self.costo_emision}). Saldo actual: ${self.saldo}")