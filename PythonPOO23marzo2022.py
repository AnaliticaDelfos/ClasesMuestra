

# Código visto en la clase muestra del día 
# 23 de marzo del 2022
# Autor: Alberto Herrera
# Analítica Delfos 



class Lote_de_tacos:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
        
class Transaccion:
    def __init__(self, tipo, cantidad, ingresos):
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__ingresos = ingresos
        
    def ver_tipo(self):
        return self.__tipo
        
    def ver_cantidad(self):
        return self.__cantidad
        
    def ver_ingresos(self):
        return self.__ingresos
        
class Carrito:
    def __init__(self):
        self.__menu = {}
        self.__total_vendidos = 0
        self.__ingresos_totales = 0
        self.__transacciones = []
        
    def ver_menu():
        return """
        1.- Pastor
        2.- Bistek
        3.- Adobada
        4.- Salir
        """
        
    def __add__(self, t):
        
        if t.tipo in self.__menu:
            self.__menu[tipo]['cantidad'] += t.cantidad
        else:
            precio = float(input("""
        Precio:
            """))
            self.__menu[t.tipo] = {}
            self.__menu[t.tipo]['cantidad'] = t.cantidad
            self.__menu[t.tipo]['precio'] = precio
    
    def __sub__(self, lote):
        if self.__menu[lote.tipo]['cantidad'] < lote.cantidad:
            vendidos = self.__menu[lote.tipo]['cantidad']
            ingresos = vendidos * self.__menu[lote.tipo]['precio']
            self.__transacciones.append(Transaccion(lote.tipo, vendidos, ingresos))
            self.__menu[lote.tipo]['cantidad'] = 0
        else:
            vendidos = lote.cantidad
            ingresos = vendidos * self.__menu[lote.tipo]['precio']
            self.__transacciones.append(Transaccion(lote.tipo, vendidos, ingresos))
            self.__menu[lote.tipo]['cantidad'] -= lote.cantidad
            
        self.__ingresos_totales += ingresos
        self.__total_vendidos += vendidos
    
    def agregar_tacos(self):
        while True:
            entrada = int(input(Carrito.ver_menu()))
            if entrada == 4:
                break
            elif entrada == 1:
                tipo = "Pastor"
            elif entrada == 2:
                tipo = "Bistek"
            elif entrada == 3:
                tipo = "Adobada"
            
            cantidad = int(input("""
        Cantidad: 
            """))
            lote = Lote_de_tacos(tipo, cantidad)
            
            self + lote
            
            
                
    def vender_tacos(self):
        while True:
            entrada = int(input(Carrito.ver_menu()))
            if entrada == 4:
                break
            elif entrada == 1:
                tipo = "Pastor"
            elif entrada == 2:
                tipo = "Bistek"
            elif entrada == 3:
                tipo = "Adobada"
            
            cantidad = int(input("""
        Cantidad: 
            """))
            
            self - Lote_de_tacos(tipo, cantidad)
            
    def ver_transacciones(self):
        for transaccion in self.__transacciones:
            print(f"Tipo de taco: {transaccion.ver_tipo()}. \
            Vendidos: {transaccion.ver_cantidad()}. Ingresos: {transaccion.ver_ingresos()}")
        print(f"Total vendidos: {self.__total_vendidos}. Ingresos totales: {self.__ingresos_totales}")
        
                
    def ver_tacos_en_existencia(self):
        for tipo in self.__menu:
            print(self.__menu[tipo])
                
        
weros_tacos = Carrito()
print("""
¡¡¡Bienvenido dueño de la taquería!!!
Es hora de agregar los tacos a vender
""")
weros_tacos.agregar_tacos()
print("""
¡¡¡Es hora de vender!!!
Suerte y éxito
""")
weros_tacos.vender_tacos()
print("""
Resumen de hoy
""")
weros_tacos.ver_transacciones()
        
    