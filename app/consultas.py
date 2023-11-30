import sqlite3
import os

conn = sqlite3.connect('base_prueba.db')
cursor =  conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS movimientos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                descripcion TEXT,
                importe INTEGER,
                n_operacion TEXT
                )""")

def total_gastado():
    cursor.execute("""
                   SELECT SUM(importe) FROM movimientos
                   WHERE importe < 0
                   """)
    total_gastado = cursor.fetchone()
    return total_gastado[0]

def total_ingresado():
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos
                   WHERE importe >= 0
                   """)
    total_ingresado = cursor.fetchone()
    return total_ingresado[0]

def total_ingresadoXmes(mes):
    mes = str(mes)
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos
                   WHERE CAST(substr(fecha, 6, 2) AS INTEGER) = ? AND importe >= 0
                   """, (mes,))
    total_ingresado_x_mes = cursor.fetchone()
    return total_ingresado_x_mes[0]

def total_gastadoXmes(mes):
    mes = str(mes)
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos
                   WHERE CAST(substr(fecha, 6, 2) AS INTEGER) = ? AND importe < 0
                   """, (mes,))
    gastado_x_mes = cursor.fetchone()
    return gastado_x_mes[0]

def total_generadoXinversion():
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos	
                   WHERE descripcion = "Rendimiento positivo de la inversión"
                   """)
    total_generado = cursor.fetchone()
    return total_generado

def total_generadoXinversionXmes(mes):
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos
                   WHERE CAST(substr(fecha, 6, 2) AS INTEGER) = ? AND descripcion = "Rendimiento positivo de la inversión"
                   """, (mes,))
    generado_x_mes = cursor.fetchone()
    return generado_x_mes[0]

def percepciones_totales(): 
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos
                   WHERE descripcion LIKE '%Percepción%'
                   """)
    percepciones = cursor.fetchone()
    return percepciones

def percepciones_X_mes(mes): 
    cursor.execute("""
                   SELECT ROUND(SUM(importe),2) FROM movimientos
                   WHERE descripcion LIKE '%Percepción%' AND CAST(substr(fecha,6,2) AS INTEGER) = ?
                   """, (mes,))
    percepciones_mes = cursor.fetchone()
    return percepciones_mes

    
    