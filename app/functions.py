def recorte_fecha(fecha):
    n_letras = 10
    if len(fecha) >= n_letras:
        fecha_recortada = fecha[:n_letras]
        
        return fecha_recortada
    else:
        print('La cadena es muy corta para obtener los datos')
    
        