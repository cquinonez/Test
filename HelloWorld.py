//crea un funcion que calcule el impuesto de una compra en Canada en la provincia de Quebec tanto federal como provincial
def calcular_impuesto(precio):
    impuesto_federal = 0.05
    impuesto_provincial = 0.09975
    total_impuesto = precio * (impuesto_federal + impuesto_provincial)
    return total_impuesto
