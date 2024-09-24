# se crea la clase
class angel1086:
    # creacion de atributos
    id_surcursal=0
    ubicacion =" "
    tamaño=0
    capacidad=0
    gerente=" "
    horario=""
    telefono=0
    # creacion de funciones
    def mostrar_datos(self,id_surc,ubi,tama,capac,geren,horario,telef):
        print("---------mostrando datos surcursal----------\n")
        print(f"Id de la surcursal: {id_surc}")
        print(f"Ubicacion de la papelerias: {ubi}")
        print (f"el tamaño de la papeleria es de: {tama} metros cuadrados")
        print(f"La capacidad de la papeleria: {capac}")
        print(f"El gerente de la papeleria es: {geren}")
        print(f"el horario de la papeleria es {horario}")
        print(f"el telefono de la papeleria es: {telef}\n")



    def lista_ubicaciones1086(self):
        ubicaciones=["Las torres","Las americas","Gran patio","Sendero"]
        for x in ubicaciones:
            print(x)
    
    def tupla_tamaño(self,medida):
        tamaños=(100,200,300,400)
        for x in tamaños:
            print(x,"la medida es en",medida)

    def dic_capacidad(self):
        capacidad_tienda= {
            "sendero " : "1000 personas",
            "las americas " : "2000 personas",
            "Gran patio" : "3000 personas",
            "Las torres " : "4000 personas"
        }
        for x,y in capacidad_tienda.items():
            print("la papeleria: ",x,"Tiene capacidad de: ",y)

    def tienda_cerrada(self):
        print("la papeleria esta cerrada")

    def tienda_abierta(self):
        print("la papeleria esta abierta")
# creando objetos

surcursales = angel1086()

#asignar datosa los atributos

surcursales.id_surcursal=1
surcursales.ubicacion =" chiapas melgar "
surcursales.tamaño=1000
surcursales.capacidad=10000
surcursales.gerente=" carlos melgar "
surcursales.horario=" de 10 am a 12 pm"
surcursales.telefono=6569102943


surcursales.mostrar_datos(surcursales.id_surcursal,surcursales.ubicacion,surcursales.tamaño,surcursales.capacidad,
                        surcursales.gerente,surcursales.horario,surcursales.telefono)
# mostrando datos 

print("-------listas de las ubicaciones de las papelerias------------------")
surcursales.lista_ubicaciones1086()
print("----------------tupla de los tamaños de las papelerias-----------------")
surcursales.tupla_tamaño(" metros cuadrados")
print("--------diccionario con las capacidades de las papelerias-------------")
surcursales.dic_capacidad()
print("--- cuando papeleria esta cerrada------")
surcursales.tienda_cerrada()
print("----- cuando tienda esta abierta------")
surcursales.tienda_abierta()
