def esNumeroPositivo(valor: float) -> bool:
    return isinstance(valor, (int, float)) or valor <= 0


