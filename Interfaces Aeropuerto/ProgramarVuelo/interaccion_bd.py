from conexion_bd import *

def formulario_aerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea):
    formulario_aerolinea = "insert into formtemp values('{}','{}','{}','{}','{}') ".format(nit_aerolinea,nombre_aerolinea,ciu_aerolinea,email_aerolinea,tel_aerolinea)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_aerolinea)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def formulario_pilotos(idpiloto,aeronit,nombrepiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto):
    piloto = "insert into piloto values('{}','{}','{}','{}','{}','{}')".format(idpiloto,aeronit,nombrepiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto) 
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(piloto)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def formulario_copilotos(copilotoid,aeronit,nombre,numerolicencia,horasexperiencia,revisionmedica):
    copiloto = "insert into copiloto values('{}','{}','{}','{}','{}','{}') ".format(copilotoid,aeronit,nombre,numerolicencia,horasexperiencia,revisionmedica)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(copiloto)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def formulario_aviones(avionid, aeronit, modelo, tipopropulsion, numeromotor, pesonominal, capacidad):
    formulario_avion = "insert into avion values('{}','{}','{}','{}','{}','{}','{}') ".format(avionid, aeronit, modelo, tipopropulsion, numeromotor, pesonominal, capacidad)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_avion)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def autenticar_usuario(usuario,contrasena):
    contrasenabd = "select contrasena from usuarios where usuario = '{}'".format(usuario)
    conexion     = conexion_aerocampbd()
    cursor       = conexion.cursor()
    cursor.execute(contrasenabd)
    lstcontrasena = cursor.fetchall()
    conexion.commit()

    if len(lstcontrasena) == 0:
        ban = False
    else:        
        lcontrasena = lstcontrasena[0][0]
        if lcontrasena == contrasena:
            print(contrasena)
            ban = True
    conexion.close()
    return ban