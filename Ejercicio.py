resultados=[]
stock = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],

}
productos= {
        'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
        'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
        'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
        'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
        'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
        'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
        'S007': ['Camisa Informal', 'camisa', 'M', 'blanco', 'algodon', False],
}

def validar_texto_no_vacio(valor):
    return valor.strip() !=""

def validar_codigo(codigo,productos,stock):
    if not validar_texto_no_vacio(codigo):
        return False
    if codigo.upper()in[c.upper()for c in productos] or codigo.upper() in [c.upper() for c in stock]:
        return False

def validar_talla(validar_talla):
    try:
        talla=float(validar_talla)
        return talla > 0 
    except ValueError:
        return False

def validar_precio(precio_texto):
    try:
        precio=int(precio_texto)
        return precio>0 
    except ValueError:
        return False


def leer_opcion():
    while True:
        entrada=input("ingresa una opcion:")
        try:
            opcion=int(entrada)
            if 1<=opcion<=6:
                return opcion
            else:
                print("seleccione una opcion valida")
        except ValueError:
            print("seleccione una opcion valida ")
def unidades_categoria(categoria, productos, stock):
    total=0
    for codigo in productos:
        if productos[codigo][1].lower()==categoria.lower():
            if codigo in stock:
                total += stock[codigo][1]
    print(f"el total de unidades disponibles es :{total}")

def busqueda_precio(p_min,p_max,productos,stock):
    resultados=[]
    for codigo in stock:
        precio=stock[codigo][0]
        unidades = stock[codigo][1]
        if p_min<= precio<=p_max and unidades != 0:
            nombre = productos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
if len(resultados)== 0:
    print("no hay productos en este rango")
else:
    resultados.sort()
    print(f"los profuctos encontrados son {resultados}")

def buscar_codigo(codigo,diccionario):
    for clave in diccionario:
        if clave.lower()== codigo.lower():
            return True

def codigo_real(codigo,diccionario):
    for clave in diccionario:
        if clave.lower()== codigo.lower():
            return clave
        return None

def actualizar_precio(codigo,nuevo_precio,stock):
     if buscar_codigo(codigo,stock):
         clave_real = codigo_real(codigo,stock)
         stock(clave_real)[0]=nuevo_precio
         return True
     else:
         return False
     
def agregar_producto(codigo,nombre,talla,color,material,es_unisex,
                     precio,unidades,productos,stock):
    
    if buscar_codigo(codigo,productos) or buscar_codigo(codigo,stock):
        return False
    
    productos[codigo]=[nombre,talla,color,material,es_unisex]
    stock[codigo]=[precio,unidades]
    return True

def eliminar_prducto(codigo,productos,stock):
    if buscar_codigo(codigo, productos):
        clave_real=codigo_real(codigo,productos)
        del productos[clave_real]
        if codigo in stock or buscar_codigo(codigo,stock):
            clave_stock = codigo_real(codigo,stock)
            if clave_stock is not None:
                del stock [clave_stock]
        return True
    else:
        return False
    

def main():
  productos= {
        'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
        'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
        'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
        'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
        'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
        'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
        'S007': ['Camisa Informal', 'camisa', 'M', 'blanco', 'algodon', False],
}

stock = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],

}

continuar= True
while continuar:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda*")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()


    if opcion==1:
        categoria=input("ingresa la categora:")
        unidades_categoria(categoria, productos,stock)
    
    elif opcion==2:
        valores_validos = False
        while not valores_validos:
            try:
                p_min =int(input("Ingrese precio minimo:"))
                p_max =int(input("ingrese precio maximo:"))
                if p_min >=0 and p_max >=0 and p_min <= p_max:
                    valores_validos = True
                else:
                    print("debe ingresar valores enteros")
            except ValueError:
                print("debe ingresar valores enteros")
        busqueda_precio(p_min,p_max, productos,stock)
        
    elif opcion==3:
        repetir=True
        while repetir:
            codigo=input("ingresa el codigo del producto")
            nuevo_precio = None
            while nuevo_precio is None:
                try:
                    valor=int(input("ingresa el valor"))
                    
                    if valor < 0:
                        nuevo_precio=valor
                    else:
                        print("el precio debe ser positivo")
                except ValueError:
                    print("el precio debe ser positivo")
                    
        resultado= actualizar_precio(codigo,nuevo_precio,stock)
        if resultado:
            print("precio actualizado")
        else:
            print("el codigo no existe")


        respuesta= input("desea actualizar otro precio(s/n)?")
        while respuesta.strip().lower() not in ("s","n"):
            respuesta= input("desea actualizar otro precio (s/n)?")
        repetir=respuesta.strip().lower()== "s"
        
        
    elif opcion == 4:
        codigo= int(input("ingrese el codigo del producto:"))
        nombre=input("")
        categoria=input("")
        talla=int(input(""))
        color=input("")
        material=input("")
        es_unisex=input("")
        precio=int(input(""))
        unidades=int(input(""))
        valido = True
        
    
    elif opcion == 5:
        codigo=input("ingrese el codigo del producto:")

        resultado= eliminar_prducto(codigo, productos,stock)
        if resultado:
            print("producto eliminado")
        else:
            print("el codigo no existe")


    elif opcion == 6:
        print("programa finalizado")
        continuar= False
        





