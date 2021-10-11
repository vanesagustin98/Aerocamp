from conexion_bd import *

def formulario_aerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea):
    formulario_aerolinea = "insert into formtemp values('{}','{}','{}','{}','{}') ".format(nit_aerolinea,nombre_aerolinea,ciu_aerolinea,email_aerolinea,tel_aerolinea)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_aerolinea)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"