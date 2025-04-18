from decimal import Decimal, ROUND_HALF_UP

def format_money(value):
    """Convierte un valor a Decimal redondeado a 2 decimales con ROUND_HALF_UP"""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
