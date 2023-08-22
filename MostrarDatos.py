from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from collections import Counter
from bson.objectid import ObjectId
import conexion
import pymongo


def obtener_top_ubicaciones(coleccion, num_locations=3):
    """Obtiene las ubicaciones mas comunes"""

    # Agregación para obtener las ubicaciones más usadas
    pipeline = [
        {"$group": {"_id": "$userLocation", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": num_locations}
    ]

    top_locations = list(coleccion.aggregate(pipeline))

    return top_locations


def obtener_mas_comunes_fuentes(coleccion, num_sources=3):


    # Obtener los valores del campo "tweetSource"
    tweet_sources = [doc["tweetSource"] for doc in coleccion.find()]

    # Calcular las fuentes más comunes
    sources_counter = Counter(tweet_sources)
    most_common_sources = sources_counter.most_common(num_sources)

    return most_common_sources

#Sirve para mostrar los datos
def mostrarDatos():
    objetoBuscar={} # Crea un objeto de búsqueda vacío
    try:
        #Obtiene la conexion a la bd
        coleccion = conexion.ObtenerConexion()

        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)  # Borra los registros actuales en la tabla
        for documento in coleccion.find(objetoBuscar):
            # Inserta en la tabla un nuevo registro con el ID y valores seleccionados del documento
            tabla.insert('', 0,text=documento["tweetID"],  values=(documento["tweetText"], documento["tweetCreated"], documento["userName"], documento["userLocation"]))

        #Obtiene las ubicaciones mas comunes
        ubaciones_top = obtener_top_ubicaciones(coleccion, num_locations=3)
        # Insertar valores en los campos de entrada para ubicaciones
        pais1.delete(0, END)
        pais1.insert(0, f"{ubaciones_top[0]['_id']} - {ubaciones_top[0]['count']}")

        pais2.delete(0, END)
        pais2.insert(0, f"{ubaciones_top[1]['_id']} - {ubaciones_top[1]['count']}")

        pais3.delete(0, END)
        pais3.insert(0, f"{ubaciones_top[2]['_id']} - {ubaciones_top[2]['count']}")

        #Obtiene las fuentes mas comunes
        fuentes_top = obtener_mas_comunes_fuentes(coleccion, num_sources=3)
        # Insertar valores en los campos de entrada para fuentes



    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)

    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
    


#Interaz TK
ventana=Tk()
tabla = ttk.Treeview(ventana, columns=("Text", "created", "userName", "userLocation"))
tabla.grid(row=1, column=0, columnspan=2)

# Define los anchos de las columnas
tabla.column("#0", width=150)
tabla.column("Text", width=700) 
tabla.column("created", width=150)
tabla.column("userName", width=150)
tabla.column("userLocation", width=150)

# Configura los encabezados de las columnas
tabla.heading("#0", text="TWEET ID")
tabla.heading("Text", text="TEXTO")
tabla.heading("created", text="FECHA CREACION")
tabla.heading("userName", text="NOMBRE USUARIO")
tabla.heading("userLocation", text="UBICACION USER")


#Etiqueta 1
Label(ventana,text="Pais 1:").grid(row=2,column=0,sticky=W+E)
pais1=Entry(ventana)
pais1.grid(row=2,column=1,sticky=W+E)

#Etiqueta 2
Label(ventana,text="Pais 2:").grid(row=3,column=0,sticky=W+E)
pais2=Entry(ventana)
pais2.grid(row=3,column=1,sticky=W+E)

#Etiqueta 3
Label(ventana,text="Pais 3:").grid(row=4,column=0,sticky=W+E)
pais3 =Entry(ventana)
pais3.grid(row=4,column=1,sticky=W+E)



#Boton Actualizar
actualizar=Button(ventana,text="Actualizar",command=mostrarDatos,bg="green",fg="white")
actualizar.grid(row=5,columnspan=2,sticky=W+E)

mostrarDatos()
ventana.mainloop()