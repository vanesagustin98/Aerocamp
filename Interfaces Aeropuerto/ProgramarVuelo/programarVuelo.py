import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QStandardItemModel
import psycopg2
from conexion_bd import *
from interaccion_bd import *

class iniciar:
    def __init__(self):
        
        app = QtWidgets.QApplication([])
        self.agendamientoVuelos = uic.loadUi("agendamientoVuelos.ui")
        self.autenticacion = uic.loadUi("autenticacion.ui")
        self.consultarAgenda = uic.loadUi("consultarAgenda.ui")
        self.formularioRegistro = uic.loadUi("formularioRegistro.ui")
        self.aerolinea = uic.loadUi("interfazAerolinea.ui")
        self.aeropuerto = uic.loadUi("interfazAeropuerto.ui")
        self.listadoAerolineas = uic.loadUi("listadoAerolineas.ui")
        self.modicarDatosAerolinea = uic.loadUi("modificarDatosAerolinea.ui")
        self.modificarDatosAeropuerto = uic.loadUi("modificarDatosAeropuerto.ui")
        self.registrarAvion = uic.loadUi("registrarAvion.ui")
        self.registrarCopiloto = uic.loadUi("registrarCopiloto.ui")
        self.registrarPiloto = uic.loadUi("registrarPiloto.ui")
        self.solicitudesPendientesVuelos = uic.loadUi("solicitudesPendientesVuelos.ui")
        self.solicitudesRegistroAerolinea = uic.loadUi("solicitudesRegistroAerolinea.ui")
        self.vuelo = uic.loadUi("vuelo.ui")
        self.dialogo = uic.loadUi("dialogo.ui")

        self.aeropuerto.label_2.setPixmap(QtGui.QPixmap("iconoavion.jpg"))
        self.agendamientoVuelos.label_2.setPixmap(QtGui.QPixmap("iconoagenda.jpg"))
        self.autenticacion.label_2.setPixmap(QtGui.QPixmap("iconoiniciosesion.jpg"))
        self.formularioRegistro.label_6.setPixmap(QtGui.QPixmap("iconoformulario.jpg"))
        self.registrarAvion.label.setPixmap(QtGui.QPixmap("iconoregistroavion.jpg"))
        self.registrarCopiloto.label.setPixmap(QtGui.QPixmap("iconopiloto.jpg"))
        self.registrarPiloto.label.setPixmap(QtGui.QPixmap("iconopiloto.jpg"))
        self.solicitudesPendientesVuelos.label_2.setPixmap(QtGui.QPixmap("iconoavion.jpg"))
        self.solicitudesRegistroAerolinea.label_2.setPixmap(QtGui.QPixmap("iconosolicitudregistro.jpg"))
        self.vuelo.label_3.setPixmap(QtGui.QPixmap("iconoprogramarvuelo.jpg"))
        self.aerolinea.label_2.setPixmap(QtGui.QPixmap("iconoregistroavion.jpg"))

        self.autenticacion.show()

        self.aerolinea.bt_programarVuelo.clicked.connect(self.ProgramarVuelo)
        self.vuelo.crearVuelo.clicked.connect(self.CrearVuelo)
        self.aeropuerto.bt_solicitudesVuelos.clicked.connect(self.SolicitudesVuelos)
        self.solicitudesPendientesVuelos.bt_buscarDisponibilidad.clicked.connect(self.BuscarDisponibilidad)
        self.aeropuerto.bt_agendaVuelosAeropuerto.clicked.connect(self.ConsultarAgendaAeropuerto)
        self.aerolinea.bt_solicitarAgendamiento.clicked.connect(self.SolicitarAgendamiento)
        self.solicitudesPendientesVuelos.bt_confirmarSolicitud.clicked.connect(self.ConfirmarSolicitud)
        self.agendamientoVuelos.bt_realizarSolicitud.clicked.connect(self.RealizarSolicitud)
        self.aerolinea.bt_cerrarSesion.clicked.connect(self.Salir)
        self.aeropuerto.bt_cerrarSesion.clicked.connect(self.Salir)
        self.consultarAgenda.bt_consultarAgenda.clicked.connect(self.consultarAgenda2)
        self.autenticacion.pushButton_3.clicked.connect(self.LlenarFormulario)
        self.autenticacion.pushButton.clicked.connect(self.autenticarusuario)
        self.aeropuerto.bt_visualizarAerolineas.clicked.connect(self.VisualizarAerolineas)
        self.aerolinea.bt_visualizarDatos.clicked.connect(self.VerDatosAerolinea)
        self.listadoAerolineas.pushButton.clicked.connect(self.VerListadoAeropuerto)
        self.aerolinea.pushButton_4.clicked.connect(self.RegistrarAvion)
        self.aerolinea.pushButton_3.clicked.connect(self.RegistrarCopiloto)
        self.aerolinea.pushButton_2.clicked.connect(self.RegistrarPiloto)
        self.aeropuerto.bt_revisarSoliRegistros.clicked.connect(self.verSolicitudesRegistro)
        self.formularioRegistro.pushButton.clicked.connect(self.enviarformulario)
        self.registrarPiloto.bt_registrar_piloto_7.clicked.connect(self.enviarpiloto)
        self.registrarCopiloto.bt_registrar_piloto_7.clicked.connect(self.EnviarCopiloto)
        self.registrarAvion.bt_registrar_piloto_7.clicked.connect(self.enviarAvion)
        self.solicitudesRegistroAerolinea.pushButton.clicked.connect(self.crearusuario)
        self.solicitudesRegistroAerolinea.pushButton_2.clicked.connect(self.rechazarusuario)
        self.modificarDatosAeropuerto.pushButton.clicked.connect(self.registraraerolinea)
        app.exec()

    def rechazarusuario(self):
        nombre = self.solicitudesRegistroAerolinea.comboBox.currentText()
        borrar_erolineaformtemp(nombre)
        listsoliaero = listado_aerolineasusuario()
        self.solicitudesRegistroAerolinea.comboBox.clear()
        for n in listsoliaero:
            for k in n:
                self.solicitudesRegistroAerolinea.comboBox.addItem(k)
        self.solicitudesRegistroAerolinea.update()
        
    def crearusuario(self):
        nombre = self.solicitudesRegistroAerolinea.comboBox.currentText()
        aeronit = buscar_nitaerolinea(nombre)
        ciudad = buscar_ciuaerolinea(nombre)
        email = buscar_correoaerolinea(nombre)
        telefono = buscar_telaerolinea(nombre)

        self.modificarDatosAeropuerto.lineEdit_4.setText(nombre)
        self.modificarDatosAeropuerto.lineEdit_5.setText(aeronit)
        self.modificarDatosAeropuerto.comboBox.setText(ciudad)
        self.modificarDatosAeropuerto.lineEdit_6.setText(email)
        self.modificarDatosAeropuerto.lineEdit_7.setText(telefono)
        self.modificarDatosAeropuerto.lineEdit.setText(aeronit)

        self.modificarDatosAeropuerto.show()
        
    def registraraerolinea(self):
        nombre_aerolinea= self.modificarDatosAeropuerto.lineEdit_4.text()
        nit_aerolinea= self.modificarDatosAeropuerto.lineEdit_5.text()
        ciu_aerolinea= self.modificarDatosAeropuerto.comboBox.text()
        email_aerolinea= self.modificarDatosAeropuerto.lineEdit_6.text()
        tel_aerolinea= self.modificarDatosAeropuerto.lineEdit_7.text()
        usuario = self.modificarDatosAeropuerto.lineEdit.text()
        contrasena = self.modificarDatosAeropuerto.lineEdit_2.text()
        contrasenar = self.modificarDatosAeropuerto.lineEdit_3.text()
        identificador = 'A'
        
        if(contrasena==contrasenar and nit_aerolinea==usuario):
            print('son iguales')
            formulario_usuario(identificador,usuario,contrasena)
            formulario_registrosaerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea)
            print("3")

            borrar_erolineaformtemp(nombre_aerolinea)
            listsoliaero = listado_aerolineasusuario()
            self.solicitudesRegistroAerolinea.comboBox.clear()
            for n in listsoliaero:
                for k in n:
                    self.solicitudesRegistroAerolinea.comboBox.addItem(k)

            nombre_aerolinea= self.modificarDatosAeropuerto.lineEdit_4.clear()
            nit_aerolinea= self.modificarDatosAeropuerto.lineEdit_5.clear()
            ciu_aerolinea= self.modificarDatosAeropuerto.comboBox.clear()
            email_aerolinea= self.modificarDatosAeropuerto.lineEdit_6.clear()
            tel_aerolinea= self.modificarDatosAeropuerto.lineEdit_7.clear()
            usuario = self.modificarDatosAeropuerto.lineEdit.clear()
            contrasena = self.modificarDatosAeropuerto.lineEdit_2.clear()
            contrasenar = self.modificarDatosAeropuerto.lineEdit_3.clear()
            self.modificarDatosAeropuerto.close()
            self.solicitudesRegistroAerolinea.update() 
            
        else:
            print("no son iguales")
            print("nit=usuario")
    
    def autenticarusuario(self):
        usuario     = self.autenticacion.lineEdit.text()
        contrasena  = self.autenticacion.lineEdit_2.text()

        if len(usuario)>0 and len(contrasena)>0:
            a = autenticar_usuario(usuario,contrasena)
            b = verificar_identificador(usuario)
            if autenticar_usuario(usuario,contrasena) and verificar_identificador(usuario) == "P" :
                print(a)
                print(b)
                self.Ingresar_aeropuerto()
            elif autenticar_usuario(usuario,contrasena) and verificar_identificador(usuario) == "A":
                print(a)
                print(b)
                self.Ingresar_aerolinea()
            else:
                self.dialogo.label.setText("El nombre de usuario y/o la contraseña son \n incorrectos")
                self.dialogo.show()
        else: 
            self.dialogo.label.setText("Se debe llenar la información de todos los campos")
            self.dialogo.show()
        
        self.autenticacion.lineEdit.clear()
        self.autenticacion.lineEdit_2.clear()
        
    def enviarpiloto(self):
        nombrepiloto = self.registrarPiloto.lineEdit_27.text()
        idpiloto = self.registrarPiloto.lineEdit_28.text()
        nrolicenciapiloto = self.registrarPiloto.lineEdit_29.text()
        horasexperienciapiloto = self.registrarPiloto.spinBox_11.text()
        revisionmedicapiloto = self.registrarPiloto.dateEdit_10.text()
        aeronit = '1234'
        
        formulario_pilotos(idpiloto,aeronit,nombrepiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto)
        
        nombrepiloto = self.registrarPiloto.lineEdit_27.clear()
        idpiloto = self.registrarPiloto.lineEdit_28.clear()
        nrolicenciapiloto = self.registrarPiloto.lineEdit_29.clear()
        horasexperienciapiloto = self.registrarPiloto.spinBox_11.clear()
        revisionmedicapiloto = self.registrarPiloto.dateEdit_10.clear()
        aeronit = '1234'
        if(len(nombrepiloto)>0 and len(idpiloto)>0 and len(nrolicenciapiloto)>0):
            if(idpiloto.isnumeric()):
                #if(buscarpiloto(idpiloto) is False):
                    
                    formulario_pilotos(idpiloto,aeronit,nombrepiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto)
                    
                    nombrepiloto = self.registrarPiloto.lineEdit_27.clear()
                    idpiloto = self.registrarPiloto.lineEdit_28.clear()
                    nrolicenciapiloto = self.registrarPiloto.lineEdit_29.clear()
                    horasexperienciapiloto = self.registrarPiloto.spinBox_11.clear()
                    revisionmedicapiloto = self.registrarPiloto.dateEdit_10.clear()
                    aeronit = '1234'
                    self.dialogo.label.setText("Se ha registrado el piloto correctamente")
                    self.dialogo.show()
                    
                #else:
                #    self.dialogo.label.setText("El piloto ya ha sido registrado")
                #    self.dialogo.show()
            else:        
                self.dialogo.label.setText("Uno o varios campos se han \n ingresado incorrectamente")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Todos los campos se deben rellenar")
            self.dialogo.show()

    def EnviarCopiloto(self):
        nombre = self.registrarCopiloto.lineEdit_24.text()
        copilotoid = self.registrarCopiloto.lineEdit_25.text()
        numerolicencia = self.registrarCopiloto.lineEdit_26.text()
        horasexperiencia = self.registrarCopiloto.spinBox_10.text()
        revisionmedica = self.registrarCopiloto.dateEdit_9.text()
        aeronit = "1234"
        
        if(len(nombre)>0 and len(copilotoid)>0 and len(numerolicencia)>0):
            if(copilotoid.isnumeric()):
                
                #if(buscarcopiloto(copilotoid) is True):
                    
                    formulario_copilotos(copilotoid,aeronit,nombre,numerolicencia,horasexperiencia,revisionmedica)

                    self.registrarCopiloto.lineEdit_24.clear()
                    self.registrarCopiloto.lineEdit_25.clear()
                    self.registrarCopiloto.lineEdit_26.clear()
                    
                    self.dialogo.label.setText("Se ha registrado el copiloto correctamente")
                    self.dialogo.show()
                    
                #else:
                #    self.dialogo.label.setText("El copiloto ya ha sido registrado")
                #    self.dialogo.show()
            else:        
                self.dialogo.label.setText("Uno o varios campos se han \n ingresado incorrectamente")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Todos los campos se deben rellenar")
            self.dialogo.show()
        
    def enviarAvion(self):
        avionid         = self.registrarAvion.lineEdit.text()
        modelo          = self.registrarAvion.lineEdit_2.text()
        tipopropulsion  = self.registrarAvion.comboBox_2.currentText()
        numeromotor     = self.registrarAvion.lineEdit_10.text()
        pesonominal     = self.registrarAvion.lineEdit_11.text()
        capacidad       = self.registrarAvion.lineEdit_12.text()
        aeronit         = "1234"

        if len(avionid) > 0 and len(modelo) > 0 and len(tipopropulsion) > 0 and len(numeromotor) > 0 and len(pesonominal) and len(capacidad) > 0:
            if numeromotor.isnumeric() and pesonominal.isnumeric() and capacidad.isnumeric():
                formulario_aviones(avionid, aeronit, modelo, tipopropulsion, numeromotor, pesonominal, capacidad)
                self.dialogo.label.setText("Se ha registrado el avión correctamente")
                self.dialogo.show()
            else:
                self.dialogo.label.setText("Uno o varios campos se han ingresado \n incorrectamente")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Todos los campos se deben rellenar")
            self.dialogo.show()

        avionid =self.registrarAvion.lineEdit.clear()
        modelo =self.registrarAvion.lineEdit_2.clear()
        numeromotor =self.registrarAvion.lineEdit_10.clear()
        pesonominal =self.registrarAvion.lineEdit_11.clear()
        capacidad =self.registrarAvion.lineEdit_12.clear()

    def enviarformulario(self):
        nombre_aerolinea= self.formularioRegistro.lineEdit.text()
        nit_aerolinea= self.formularioRegistro.lineEdit_2.text()
        ciu_aerolinea= self.formularioRegistro.comboBox.currentText()
        email_aerolinea= self.formularioRegistro.lineEdit_3.text()
        tel_aerolinea= self.formularioRegistro.lineEdit_4.text()

        formulario_aerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea)

        self.formularioRegistro.lineEdit.clear()
        self.formularioRegistro.lineEdit_2.clear()
        self.formularioRegistro.lineEdit_3.clear()
        self.formularioRegistro.lineEdit_4.clear()

    def verSolicitudesRegistro(self):
        listsoliaero = listado_aerolineasusuario()
        self.solicitudesRegistroAerolinea.comboBox.clear()
        for n in listsoliaero:
            for k in n:
                self.solicitudesRegistroAerolinea.comboBox.addItem(k)
        self.solicitudesRegistroAerolinea.show()

    def RegistrarAvion(self):
        self.registrarAvion.show()

    def RegistrarCopiloto(self):
        self.registrarCopiloto.show()

    def RegistrarPiloto(self):
        self.registrarPiloto.show()

    def VerListadoAeropuerto(self):
        self.modificarDatosAeropuerto.show()

    def VerDatosAerolinea(self):
        self.modicarDatosAerolinea.show()

    def VisualizarAerolineas(self):
        self.listadoAerolineas.show()
        self.listadoAerolineas.listView.clear()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select nombreaerolinea from aerolinea;"
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        for n in listcdvuelos:
            for k in n:

                self.listadoAerolineas.listView.addItem(k)

        print(type(listcdvuelos))
        conexion.close()

    def Ingresar_aeropuerto(self):
        self.aeropuerto.show()
        self.autenticacion.close()

    def Ingresar_aerolinea(self):
        self.aerolinea.show()
        self.autenticacion.close()

    def LlenarFormulario(self):
        self.formularioRegistro.show()

    def ProgramarVuelo(self):  
        #Agregar los nombres de los pilotos al comboBox correspondiente
        self.vuelo.comboBox_3.clear()
        listpilotos = listado_pilotos()
        for n in listpilotos:
            for k in n:
                self.vuelo.comboBox_3.addItem(k)
        #Agregar los nombres de los copilotos al comboBox correspondiente
        self.vuelo.comboBox_5.clear()
        listcopilotos = listado_copilotos()
        for m in listcopilotos:
            for j in m:
                self.vuelo.comboBox_5.addItem(j)
        #Agregar los nombres de los aviones al comboBox correspondiente
        self.vuelo.comboBox_6.clear()
        listaviones = listado_aviones()
        for d in listaviones:
            for a in d:
                self.vuelo.comboBox_6.addItem(a)
        #Abrimos la ventana donde se programa el vuelo, con los combobox con los datos correspondientes        
        self.vuelo.show()

    def CrearVuelo(self):
        #Vuelo
        horasalida= self.vuelo.timeEdit.text()
        horaentrada= self.vuelo.timeEdit_2.text()
        fechasalida = self.vuelo.dateEdit_3.text()
        fechallegada = self.vuelo.dateEdit_4.text()
        codvuelo =self.vuelo.lineEdit_13.text()
        destino = self.vuelo.comboBox.currentText()
        carga= self.vuelo.comboBox_2.currentText()
        piloto= self.vuelo.comboBox_3.currentText()
        copiloto= self.vuelo.comboBox_5.currentText()
        avionid= self.vuelo.comboBox_6.currentText()
        confirmacionvuelo = "1"
        aeronit= "1234"
        pilotoid= buscar_idpiloto(piloto,aeronit)
        copilotoid= buscar_idcopiloto(copiloto,aeronit)
        if (carga== "Carga"):
            tipovuelo= "1"
        elif (carga== "Pasajeros"):
            tipovuelo="0"
        else:
            tipovuelo="NS"

        if(len(codvuelo)>0):
            vuelo = formulario_crear_vuelo(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo)
            print(vuelo)
            self.dialogo.label.setText("Se ha registrado el vuelo correctamente")
            self.dialogo.show()
            
        else: self.dialogo.label.setText("Todos los campos se deben rellenar")
        self.dialogo.show()
        

        self.vuelo.lineEdit_13.setText("")

    def BuscarDisponibilidad(self):
        ##aquiuiiii
        n=self.solicitudesPendientesVuelos.cb_listaVuelos.currentText()
        self.consultarAgenda.tableWidget.clear()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        date= self.consultarAgenda.dateEdit.text()

        fechallegadacomp= "select fechallegada from vuelo where codvuelo ='{}'".format(n)
        cursor.execute(fechallegadacomp)
        fechallegadares= cursor.fetchall()

        horallegadacomp=  "select horaentrada from vuelo where codvuelo ='{}'".format(n)
        cursor.execute(horallegadacomp)
        horallegadacres= cursor.fetchall()

        f=fechallegadares[0][0]
        h=horallegadacres[0][0]

        busquedadis= "select codvuelo, confirmacionvuelo, fechallegada, horaentrada from vuelo where confirmacionvuelo='0' and fechallegada='{}' and horaentrada ='{}';".format(f,h)
        cursor.execute(busquedadis)
        listbusqueda= cursor.fetchall()

        if len(listbusqueda)== 0:
            self.solicitudesPendientesVuelos.bt_confirmarSolicitud.setEnabled(True)
            self.dialogo.label.setText("Hay espacio en la agenda para programar el vuelo")
            self.dialogo.show()
        else: 
            self.solicitudesPendientesVuelos.bt_confirmarSolicitud.setEnabled(False)
            self.solicitudesPendientesVuelos.bt_rechazarSolicitud.setEnabled(True)
            self.dialogo.label.setText("No hay espacio en la agenda para programar el vuelo")
            self.dialogo.show()
        
        conexion.commit()
        print("Consulta hecha con éxito")
        conexion.close()

    def SolicitudesVuelos(self):
        self.solicitudesPendientesVuelos.cb_listaVuelos.clear()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        solicitudesaeroc= "select * from soltemp;"
        cursor.execute(solicitudesaeroc)
        listsolicitudes= cursor.fetchall()
        print(type(listsolicitudes))
        conexion.commit()
        print("Consulta hecha con éxito")
        for n in listsolicitudes:
            for k in n:
                self.solicitudesPendientesVuelos.cb_listaVuelos.addItem(k)
        print(type(listsolicitudes))
        conexion.close()
        
        if self.solicitudesPendientesVuelos.cb_listaVuelos.count()==0:
            self.solicitudesPendientesVuelos.bt_buscarDisponibilidad.setEnabled(False)
            self.solicitudesPendientesVuelos.bt_confirmarSolicitud.setEnabled(False)
            self.solicitudesPendientesVuelos.bt_rechazarSolicitud.setEnabled(False)
        self.solicitudesPendientesVuelos.show()
        
    def ConsultarAgendaAeropuerto(self):
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select codvuelo, destino, tipovuelo from vuelo where confirmacionvuelo= '0' ;"
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()

        if len(listcdvuelos)>0:
            self.consultarAgenda.show()
        else:
            self.dialogo.show()

        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")

        conexion.close()

    def consultarAgenda2(self):
        self.consultarAgenda.tableWidget.clearContents()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        date= self.consultarAgenda.dateEdit.text()
        cdvuelos= "select codvuelo, destino, tipovuelo from vuelo where confirmacionvuelo= '0' and fechallegada='{}';".format(date)
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        fila=0
        for n in listcdvuelos:
            columna=0
            self.consultarAgenda.tableWidget.insertRow(fila)
            for k in n:
                celda = QtWidgets.QTableWidgetItem(k)
                self.consultarAgenda.tableWidget.setItem(fila, columna, celda)
                columna+=1
            fila+=1
        print(type(listcdvuelos))
        conexion.close()

    def SolicitarAgendamiento(self):
        self.agendamientoVuelos.ls_vuelos.clearContents()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select codvuelo, destino, tipovuelo from vuelo;"

        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        fila=0
        for n in listcdvuelos:
            columna=0
            self.agendamientoVuelos.ls_vuelos.insertRow(fila)
            for k in n:
                celda = QtWidgets.QTableWidgetItem(k)
                self.agendamientoVuelos.ls_vuelos.setItem(fila, columna, celda)
                columna+=1
            fila+=1
        print(type(listcdvuelos))
        conexion.close()

        if len(listcdvuelos)>0:
            self.agendamientoVuelos.show()
        else:
            self.agendamientoVuelos.bt_realizarSolicitud.setEnabled(False)
            self.agendamientoVuelos.bt_modificarDatos.setEnabled(False)
            self.agendamientoVuelos.bt_eliminarVuelo.setEnabled(False)
    
    def ConfirmarSolicitud(self):
        n=self.solicitudesPendientesVuelos.cb_listaVuelos.currentText()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()

        cfvuelos= "update vuelo set confirmacionvuelo='0'where codvuelo='{}';".format(n)
        borrartupla= "delete from soltemp where codvuelo='{}';".format(n)
        cursor.execute(cfvuelos)
        cursor.execute(borrartupla)
        conexion.commit()
        print("Datos actualizados con éxito")
        conexion.close()
        self.solicitudesPendientesVuelos.close()

        self.dialogo.show()
        
    def RealizarSolicitud(self):       
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        ls = self.agendamientoVuelos.ls_vuelos.selectedItems()
        for n in ls:
            cdvuelos= "insert into soltemp values('{}');".format(n.text())
            print(n.text())
            cursor.execute(cdvuelos)
        conexion.commit()
        print("Datos agregados con éxito")
        
        conexion.close()

        self.dialogo.show()
        
    def Salir(self):
        self.aerolinea.close()
        self.aeropuerto.close()
        self.autenticacion.show()

iniciar()