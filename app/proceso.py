import sqlite3
from tkinter import filedialog
import pandas as pd
import functions

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    if archivo:
        print("Archivo seleccionado: ", archivo)
        df = cargar_archivo(archivo)
        if df is not None:
            procesar_datos(df)
        return archivo
    
def cargar_archivo(archivo):
    df = pd.read_excel(archivo)
    return df

def procesar_datos(df):
    try:
        conn = sqlite3.connect('base_prueba.db')
        cursor =  conn.cursor()
    except sqlite3.Error as error:
        print("Error al conectar con la base de datos:", error)
        conn.close()

    for i, row in df.iterrows():
        fecha = functions.recorte_fecha(row['Fecha de Pago'])
        numero_movimiento = row['Número de Movimiento']

        cursor.execute(f"SELECT COUNT(*) FROM movimientos WHERE n_operacion = {numero_movimiento}")
        if cursor.fetchone()[0]==0:
            cursor.execute("INSERT OR REPLACE INTO movimientos (fecha,descripcion,importe, n_operacion) VALUES (?,?,?,?)",
                    (fecha, row['Tipo de Operación'],row['Importe'], row['Número de Movimiento']))

    conn.commit()
    conn.close()
    print("Proceso de datos completado con éxito.")
    
abrir_archivo()