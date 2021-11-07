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
            ban = True
    conexion.close()
    return ban

def verificar_identificador(usuario):
    identificadorbd = "select identificador from usuarios where usuario = '{}'".format(usuario)
    conexion        = conexion_aerocampbd()
    cursor          = conexion.cursor()
    cursor.execute(identificadorbd)
    identificador = cursor.fetchall()
    conexion.commit()
    ident = ""

    if len(identificador) == 0:
        ident = ""
    else:
        lident = identificador[0][0]
        if lident == "P":
            ident = "P"
        elif lident == "A":
            ident = "A"
    conexion.close()
    return ident

def formulario_registrosaerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea):
    formulario_aerolinea = "insert into aerolinea values('{}','{}','{}','{}','{}') ".format(nit_aerolinea,nombre_aerolinea,ciu_aerolinea,email_aerolinea,tel_aerolinea)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_aerolinea)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def formulario_registrosaerolineas_modificar(nit_aerolinea, nombre_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea):
    formulario_aerolinea = "update aerolinea set nombreaerolinea='{}',ciudad='{}',email='{}',telefono='{}' where aeronit='{}'".format(nombre_aerolinea,ciu_aerolinea,email_aerolinea,tel_aerolinea,nit_aerolinea)
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

def formulario_usuario_modificar(usuario, contrasena):
    formulario_usuario = "update usuarios set contrasena='{}' where usuario='{}'".format(contrasena,usuario)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute(formulario_usuario)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def listado_pilotos(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    nom_pilotos= "select nombre from piloto where aeronit='{}';".format(aeronit)
    cursor.execute(nom_pilotos)
    listpilotos= cursor.fetchall()
    conexion.commit()
    conexion.close()        
    return listpilotos

def listado_copilotos(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    nom_copilotos= "select nombre from copiloto where aeronit='{}';".format(aeronit)
    cursor.execute(nom_copilotos)
    listcopilotos= cursor.fetchall()
    conexion.commit()
    conexion.close()
    return listcopilotos

def listado_aviones(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    nom_aviones= "select avionid from avion where aeronit='{}';".format(aeronit)
    cursor.execute(nom_aviones)
    listaviones= cursor.fetchall()
    conexion.commit()
    conexion.close()
    return listaviones

def buscar_idpiloto(nombre, aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_pilotoid= "select pilotoid from piloto where aeronit='{}' and nombre='{}';".format(aeronit,nombre)
    cursor.execute(bus_pilotoid)
    pilotoid= cursor.fetchall()
    conexion.commit()
    conexion.close()
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
    copilotoid=copilotoid[0][0]
    return copilotoid  

def buscar_identificador(usuario):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_identificador= "select identificador from usuarios where usuario='{}' ;".format(usuario)
    cursor.execute( bus_identificador)
    identificador= cursor.fetchall()
    conexion.commit()
    conexion.close()
    identificador=identificador[0][0]
    return identificador  

def formulario_crear_vuelo(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo):
    form_crear_vuelo="insert into vuelo values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') ".format(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    cursor.execute( form_crear_vuelo)
    conexion.commit()
    conexion.close()
    return "Formulario agregado"

def listado_aerolineasusuario():
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    list_aerousu= "select nombreaerolinea from formtemp;"
    cursor.execute(list_aerousu)
    listusuariosaero= cursor.fetchall()
    conexion.commit()
    conexion.close()           
    return listusuariosaero

def listado_vuelos():
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    list_vuelos = "select codvuelo from soltemp;"
    cursor.execute(list_vuelos)
    listvuelotes= cursor.fetchall()
    conexion.commit()
    conexion.close()       
    return listvuelotes

def buscar_nitaerolinea(nombre):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_nitaerolinea= "select aeronit from formtemp where nombreaerolinea='{}';".format(nombre)
    cursor.execute( bus_nitaerolinea)
    nitaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    nitaerolinea=nitaerolinea[0][0]
    return nitaerolinea

def buscar_correoaerolinea(nombre):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_correoaerolinea= "select email from formtemp where nombreaerolinea='{}';".format(nombre)
    cursor.execute( bus_correoaerolinea)
    correoaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    correoaerolinea=correoaerolinea[0][0]
    return correoaerolinea

def buscar_ciuaerolinea(nombre):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_ciuaerolinea= "select ciudad from formtemp where nombreaerolinea='{}';".format(nombre)
    cursor.execute( bus_ciuaerolinea)
    ciuaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    ciuaerolinea=ciuaerolinea[0][0]
    return ciuaerolinea

def buscar_telaerolinea(nombre):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_telaerolinea= "select telefono from formtemp where nombreaerolinea='{}';".format(nombre)
    cursor.execute( bus_telaerolinea)
    telaerolinea = cursor.fetchall()
    conexion.commit()
    conexion.close()
    telaerolinea = telaerolinea[0][0]
    return telaerolinea

def buscar_nombreaerolinea2(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_nitaerolinea= "select nombreaerolinea from aerolinea where aeronit='{}';".format(aeronit)
    cursor.execute( bus_nitaerolinea)
    nitaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    nitaerolinea=nitaerolinea[0][0]
    return nitaerolinea

def buscar_nitaerolinea2(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_nitaerolinea= "select aeronit from aerolinea where aeronit='{}';".format(aeronit)
    cursor.execute( bus_nitaerolinea)
    nitaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    nitaerolinea=nitaerolinea[0][0]
    return nitaerolinea

def buscar_correoaerolinea2(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_correoaerolinea= "select email from aerolinea where aeronit='{}';".format(aeronit)
    cursor.execute( bus_correoaerolinea)
    correoaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    correoaerolinea=correoaerolinea[0][0]
    return correoaerolinea

def buscar_ciuaerolinea2(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_ciuaerolinea= "select ciudad from aerolinea where aeronit='{}';".format(aeronit)
    cursor.execute( bus_ciuaerolinea)
    ciuaerolinea= cursor.fetchall()
    conexion.commit()
    conexion.close()
    ciuaerolinea=ciuaerolinea[0][0]
    return ciuaerolinea

def buscar_telaerolinea2(aeronit):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_telaerolinea= "select telefono from aerolinea where aeronit='{}';".format(aeronit)
    cursor.execute( bus_telaerolinea)
    telaerolinea = cursor.fetchall()
    conexion.commit()
    conexion.close()
    telaerolinea = telaerolinea[0][0]
    return telaerolinea

def buscar_vuelo(codigo):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    bus_vuelo= "select codvuelo from vuelo where codvuelo='{}';".format(codigo)
    cursor.execute( bus_vuelo)
    vuelo = cursor.fetchall()
    conexion.commit()
    conexion.close()
    vuelo = vuelo[0][0]
    return vuelo

def borrar_aerolineaformtemp(nombre):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    borr_aerolinea= "delete from formtemp where nombreaerolinea='{}';".format(nombre)
    cursor.execute(borr_aerolinea)
    conexion.commit()
    conexion.close()
    return "Borrado c:"

def borrar_vuelosoltemp(codigo):
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    borr_vuelo = "delete from soltemp where codvuelo ='{}';".format(codigo)
    cursor.execute(borr_vuelo)
    conexion.commit()
    conexion.close()
    return "Borrado c:"

def buscarpiloto(idpiloto):
    bpiloto = "select pilotoid from piloto where pilotoid = '{}'".format(idpiloto)
    conexion     = conexion_aerocampbd()
    cursor       = conexion.cursor()
    cursor.execute(bpiloto)
    lstbusqueda = cursor.fetchall()
    conexion.commit()
    ban = True
    
    if len(lstbusqueda) == 0:
        ban = True
    else:        
        lbusqueda = lstbusqueda[0][0]
        if lbusqueda == idpiloto:
            ban = False
    conexion.close()
    return ban

def buscarcopiloto(idcopiloto):
    bpiloto = "select copilotoid from copiloto where copilotoid = '{}'".format(idcopiloto)
    conexion     = conexion_aerocampbd()
    cursor       = conexion.cursor()
    cursor.execute(bpiloto)
    lstbusqueda = cursor.fetchall()
    conexion.commit()
    ban = True
    
    if len(lstbusqueda) == 0:
        ban = True
    else:        
        lbusqueda = lstbusqueda[0][0]
        if lbusqueda == idcopiloto:
            ban = False
    conexion.close()
    return ban



def eliminar_aerolineaformtemp(nombre):
    print(nombre)
    conexion = conexion_aerocampbd()
    cursor = conexion.cursor()
    borr_avion= "delete from avion where aeronit ='{}';".format(nombre)
    borr_piloto= "delete from piloto where aeronit ='{}';".format(nombre)
    borr_copiloto= "delete from copiloto where aeronit ='{}';".format(nombre)
    borr_vuelos= "delete from vuelo where aeronit ='{}';".format(nombre)
    borr_aerolinea= "delete from aerolinea where aeronit ='{}';".format(nombre)
    borr_usuario= "delete from usuarios where usuario ='{}';".format(nombre)
    cursor.execute(borr_vuelos)
    cursor.execute(borr_avion)
    cursor.execute(borr_piloto)
    cursor.execute(borr_copiloto)
    cursor.execute(borr_aerolinea)
    cursor.execute(borr_usuario)
    conexion.commit()
    conexion.close()
    return "Borrado c:"