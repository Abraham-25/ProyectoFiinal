dto1 = []
class Prestamo:
  nombre="Abraham"
  dto1.append(nombre)
  apellido="Infante"
  dto1.append(apellido)
  telefono= 5556667777
  dto1.append(telefono)
  direccion="Lugar #69"
  dto1.append(direccion)
  
  def CuotaFija(self, monto, tasa, cuotas, periodo=MENSUAL, limit_dec=None):

    tasa = tasa / Decimal(100)
    if periodo == DIARIO:
        tasa /= Decimal(30.4167)
    elif periodo == SEMANAL:
        tasa /= Decimal(4.34524)
    if periodo == QUINCENAL:
        tasa /= Decimal(2.0)
    elif periodo == ANUAL:
        tasa *= 12
    if not tasa:
        tasa = Decimal(0.00000000001)
    valor = monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )
    interes = valor - monto
    if limit_dec:
        return (round(valor, limit_dec), round(interes, limit_dec), round(monto, limit_dec))    
    return (valor, interes, monto)