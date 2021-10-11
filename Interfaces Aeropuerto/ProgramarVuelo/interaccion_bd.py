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
    ban = False

    if len(lstcontrasena) == 0:
        ban = False
    else:        
        lcontrasena = lstcontrasena[0][0]
        if lcontrasena == contrasena:
            print(contrasena)
            ban = True
    conexion.close()
    return ban

def formulario_aerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea):
    formulario_aerolinea = "insert into aerolinea values('{}','{}','{}','{}','{}') ".format(nit_aerolinea,nombre_aerolinea,ciu_aerolinea,email_aerolinea,tel_aerolinea)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_aerolinea)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def formulario_usuario(identificador,usuario,contrasena):
    formulario_usuario = "insert into usuarios values('{}','{}','{}') ".format(identificador,usuario,contrasena)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_usuario)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def listado_pilotos():
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    nom_pilotos= "select nombre from piloto;"
    cursor.execute(nom_pilotos)
    listpilotos= cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("Consulta hecha con éxito")            
    return listpilotos

def listado_copilotos():
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    nom_copilotos= "select nombre from copiloto;"
    cursor.execute(nom_copilotos)
    listcopilotos= cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("Consulta hecha con éxito")
    return listcopilotos

def listado_aviones():
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    nom_aviones= "select avionid from avion;"
    cursor.execute(nom_aviones)
    listaviones= cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("Consulta hecha con éxito")
    return listaviones

def buscar_idpiloto(nombre, aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_pilotoid= "select pilotoid from piloto where aeronit='{}' and nombre='{}';".format(aeronit,nombre)
    cursor.execute(bus_pilotoid)
    pilotoid= cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("Consulta hecha con éxito")
    pilotoid=pilotoid[0][0]
    return pilotoid  

def buscar_idcopiloto(nombre,aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_copilotoid= "select copilotoid from copiloto where aeronit='{}' and nombre='{}';".format(aeronit,nombre)
    cursor.execute( bus_copilotoid)
    copilotoid= cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("Consulta hecha con éxito")
    copilotoid=copilotoid[0][0]
    return copilotoid  

def formulario_crear_vuelo(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo):
    form_crear_vuelo="insert into vuelo values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') ".format(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute( form_crear_vuelo)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"
