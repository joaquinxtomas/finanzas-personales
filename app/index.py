import proceso
import consultas

dec = input(""" Que deseas hacer? 
                
                1 - Cargar un nuevo archivo XLSX
                2 - Consultas sobre mi dinero.
                """)

if dec == "2":
    text =  f"""
        --- Tu ingreso historico es de: {consultas.total_ingresado()}
        --- Tu gasto historico es de: {consultas.total_gastado()}
        --- Tus rendimientos en MP son: {consultas.total_generadoXinversion()}
        """    
    print(text)
    
    new_cons = input("""
                     Deseas realizar una consulta avanzada? 
                     
                     1 - Consultar INGRESO total en un mes.
                     2 - Consultar GASTO total en un mes.
                     3 - Consultar RENDIMIENTOS totales en un mes.
                     4 - Consultar PERCEPCIONES totales historicas.
                     5 - Consultar PERCEPCIONES totales en un mes.
                     
                     """)
    
    if new_cons == "1":
        mes = input("Ingrese el mes que desea consultar (1-12): ")
        print(consultas.total_ingresadoXmes(mes))
    elif new_cons == "2":
        mes = input("Ingrese el mes que desea consultar (1-12): ")
        print(consultas.total_gastadoXmes(mes))
    elif new_cons == "3":
        mes = input("Ingrese el mes que desea consultar (1-12): ")
        print(consultas.total_generadoXinversionXmes(mes))
    elif new_cons == "4":
        print(consultas.percepciones_totales())
    elif new_cons == "4":
        mes = input("Ingrese el mes que desea consultar (1-12): ")
        print(consultas.percepciones_X_mes(mes))
    else:
        print("Opción inválida.")
    