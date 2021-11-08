from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime, QTime
from PyQt5.QtGui import *
from conexion_bd import *
from interaccion_bd import *

class iniciar:
    def __init__(self):
        app                                 = QtWidgets.QApplication([])
        self.agendamientoVuelos             = uic.loadUi("agendamientoVuelos.ui")
        self.autenticacion                  = uic.loadUi("autenticacion.ui")
        self.consultarAgenda                = uic.loadUi("consultarAgenda.ui")
        self.formularioRegistro             = uic.loadUi("formularioRegistro.ui")
        self.aerolinea                      = uic.loadUi("interfazAerolinea.ui")
        self.aeropuerto                     = uic.loadUi("interfazAeropuerto.ui")
        self.listadoAerolineas              = uic.loadUi("listadoAerolineas.ui")
        self.modificarDatosAerolinea        = uic.loadUi("modificarDatosAerolinea.ui")
        self.modificarDatosAeropuerto       = uic.loadUi("modificarDatosAeropuerto.ui")
        self.registrarAvion                 = uic.loadUi("registrarAvion.ui")
        self.registrarCopiloto              = uic.loadUi("registrarCopiloto.ui")
        self.registrarPiloto                = uic.loadUi("registrarPiloto.ui")
        self.solicitudesPendientesVuelos    = uic.loadUi("solicitudesPendientesVuelos.ui")
        self.solicitudesRegistroAerolinea   = uic.loadUi("solicitudesRegistroAerolinea.ui")
        self.visualizarVuelos               = uic.loadUi("visualizarVuelos.ui")
        self.vuelo                          = uic.loadUi("vuelo.ui")
        self.dialogo                        = uic.loadUi("dialogo.ui")
        self.modificarVuelo                 = uic.loadUi("modificarVuelo.ui")

        self.aeropuerto.label_2.setPixmap(QtGui.QPixmap("iconoavion.jpg"))
        self.aerolinea.label_2.setPixmap(QtGui.QPixmap("iconoregistroavion.jpg"))
        self.agendamientoVuelos.label_2.setPixmap(QtGui.QPixmap("iconoagenda.jpg"))
        self.autenticacion.label_2.setPixmap(QtGui.QPixmap("iconoiniciosesion.jpg"))
        self.formularioRegistro.label_6.setPixmap(QtGui.QPixmap("iconoformulario.jpg"))
        self.registrarAvion.label.setPixmap(QtGui.QPixmap("iconoregistroavion.jpg"))
        self.registrarCopiloto.label.setPixmap(QtGui.QPixmap("iconopiloto.jpg"))
        self.registrarPiloto.label.setPixmap(QtGui.QPixmap("iconopiloto.jpg"))
        self.solicitudesPendientesVuelos.label_2.setPixmap(QtGui.QPixmap("iconoavion.jpg"))
        self.solicitudesRegistroAerolinea.label_2.setPixmap(QtGui.QPixmap("iconosolicitudregistro.jpg"))
        self.vuelo.label_3.setPixmap(QtGui.QPixmap("iconoprogramarvuelo.jpg"))
        self.modificarVuelo.label_3.setPixmap(QtGui.QPixmap("iconoprogramarvuelo.jpg"))

        self.aeropuerto.bt_solicitudesVuelos.clicked.connect(self.SolicitudesVuelos)
        self.aeropuerto.bt_agendaVuelosAeropuerto.clicked.connect(self.ConsultarAgendaAeropuerto)
        self.aeropuerto.bt_cerrarSesion.clicked.connect(self.Salir)
        self.aeropuerto.bt_visualizarAerolineas.clicked.connect(self.VisualizarAerolineas)
        self.aeropuerto.bt_revisarSoliRegistros.clicked.connect(self.verSolicitudesRegistro)
        self.aerolinea.bt_programarVuelo.clicked.connect(self.ProgramarVuelo)
        self.aerolinea.bt_solicitarAgendamiento.clicked.connect(self.SolicitarAgendamiento)
        self.aerolinea.bt_cerrarSesion.clicked.connect(self.Salir)
        self.aerolinea.bt_visualizarDatos.clicked.connect(self.modificarDatosAerolineaPropios)
        self.aerolinea.pushButton_4.clicked.connect(self.RegistrarAvion)
        self.aerolinea.pushButton_3.clicked.connect(self.RegistrarCopiloto)
        self.aerolinea.pushButton_2.clicked.connect(self.RegistrarPiloto)
        self.aerolinea.pushButton.clicked.connect(self.visualizarvuelos)
        self.agendamientoVuelos.bt_realizarSolicitud.clicked.connect(self.RealizarSolicitud)
        self.agendamientoVuelos.bt_modificarDatos.clicked.connect(self.modificarVueloAerolinea)
        self.agendamientoVuelos.bt_eliminarVuelo.clicked.connect(self.eliminarVueloAerolinea)
        self.autenticacion.pushButton_3.clicked.connect(self.LlenarFormulario)
        self.autenticacion.pushButton.clicked.connect(self.autenticarusuario)
        self.consultarAgenda.bt_consultarAgenda.clicked.connect(self.consultarAgenda2)
        self.consultarAgenda.bt_cancelarVuelo.clicked.connect(self.cancelarVueloAeropuerto)
        self.formularioRegistro.pushButton.clicked.connect(self.enviarformulario)
        self.listadoAerolineas.pushButton.clicked.connect(self.modificarDatosAerop)
        self.listadoAerolineas.pushButton_2.clicked.connect(self.eliminarAerolinea)
        self.modificarDatosAerolinea.pushButton.clicked.connect(self.registraraerolinea)
        self.modificarDatosAeropuerto.pushButton.clicked.connect(self.modificarAerolinea)
        self.modificarDatosAeropuerto.pushButton_2.clicked.connect(self.editarDatosAerolinea)
        self.modificarVuelo.bt_modificar_vuelo.clicked.connect(self.modificar_Vuelo)
        self.registrarAvion.bt_registrar_piloto_7.clicked.connect(self.enviarAvion)
        self.registrarCopiloto.bt_registrar_piloto_7.clicked.connect(self.EnviarCopiloto)
        self.registrarPiloto.bt_registrar_piloto_7.clicked.connect(self.enviarpiloto)
        self.solicitudesRegistroAerolinea.pushButton.clicked.connect(self.crearusuario)
        self.solicitudesRegistroAerolinea.pushButton_2.clicked.connect(self.rechazarusuario)
        self.solicitudesPendientesVuelos.bt_buscarDisponibilidad.clicked.connect(self.BuscarDisponibilidad)
        self.solicitudesPendientesVuelos.bt_confirmarSolicitud.clicked.connect(self.ConfirmarSolicitud)
        self.solicitudesPendientesVuelos.bt_rechazarSolicitud.clicked.connect(self.rechazarvuelo)
        self.vuelo.crearVuelo.clicked.connect(self.CrearVuelo)
    
        self.autenticacion.show()
        app.exec()

    def autenticarusuario(self):
        global usuario
        usuario     = self.autenticacion.lineEdit.text()
        contrasena  = self.autenticacion.lineEdit_2.text()

        if len(usuario)>0 and len(contrasena)>0:
            a = autenticar_usuario(usuario,contrasena)
            b = verificar_identificador(usuario)
            if autenticar_usuario(usuario,contrasena) and verificar_identificador(usuario) == "P" :
                self.Ingresar_aeropuerto()
            elif autenticar_usuario(usuario,contrasena) and verificar_identificador(usuario) == "A":
                self.Ingresar_aerolinea()
            else:
                self.dialogo.label.setText("El nombre de usuario y/o la contraseña son \n incorrectos")
                self.dialogo.show()
        else: 
            self.dialogo.label.setText("Se debe llenar la información de todos los campos")
            self.dialogo.show()
        
        self.autenticacion.lineEdit.clear()
        self.autenticacion.lineEdit_2.clear()

    def BuscarDisponibilidad(self):
        if (self.solicitudesPendientesVuelos.cb_listaVuelos.count() == 0):
            self.dialogo.label.setText("No hay solicitudes donde buscar disponibilidad")
            self.dialogo.show()
        else:
            n=self.solicitudesPendientesVuelos.cb_listaVuelos.currentText()
            self.consultarAgenda.tableWidget.clear()
            conexion = conexion_aerocampbd()
            cursor = conexion.cursor()
            date = self.consultarAgenda.dateEdit.text()

            fechallegadacomp = "select fechallegada from vuelo where codvuelo ='{}'".format(n)
            cursor.execute(fechallegadacomp)
            fechallegadares = cursor.fetchall()

            horallegadacomp = "select horaentrada from vuelo where codvuelo ='{}'".format(n)
            cursor.execute(horallegadacomp)
            horallegadacres = cursor.fetchall()

            
            f = fechallegadares[0][0]
            h = horallegadacres[0][0]

            busquedadis = "select codvuelo, confirmacionvuelo, fechallegada, horaentrada from vuelo where confirmacionvuelo='0' and fechallegada='{}' and horaentrada ='{}';".format(f,h)
            cursor.execute(busquedadis)
            listbusqueda = cursor.fetchall()

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
            conexion.close()

    def crearusuario(self):
        nombre      = self.solicitudesRegistroAerolinea.comboBox.currentText()
        aeronit     = buscar_nitaerolinea(nombre)
        ciudad      = buscar_ciuaerolinea(nombre)
        email       = buscar_correoaerolinea(nombre)
        telefono    = buscar_telaerolinea(nombre)

        self.modificarDatosAerolinea.lineEdit_4.setText(nombre)
        self.modificarDatosAerolinea.lineEdit_5.setText(aeronit)
        self.modificarDatosAerolinea.comboBox.setText(ciudad)
        self.modificarDatosAerolinea.lineEdit_6.setText(email)
        self.modificarDatosAerolinea.lineEdit_7.setText(telefono)
        self.modificarDatosAerolinea.lineEdit.setText(aeronit)

        self.modificarDatosAerolinea.show()

    def CrearVuelo(self):
        #Vuelo
        horasalida          = self.vuelo.timeEdit.text()
        horaentrada         = self.vuelo.timeEdit_2.text()
        fechasalida         = self.vuelo.dateEdit_3.text()
        fechallegada        = self.vuelo.dateEdit_4.text()
        codvuelo            = self.vuelo.lineEdit_13.text()
        destino             = self.vuelo.comboBox.currentText()
        carga               = self.vuelo.comboBox_2.currentText()
        piloto              = self.vuelo.comboBox_3.currentText()
        copiloto            = self.vuelo.comboBox_5.currentText()
        avionid             = self.vuelo.comboBox_6.currentText()
        confirmacionvuelo   = "C"
        aeronit             = usuario
        pilotoid            = buscar_idpiloto(piloto,aeronit)
        copilotoid          = buscar_idcopiloto(copiloto,aeronit)

        if (carga == "Carga"):
            tipovuelo = "1"
        elif (carga == "Pasajeros"):
            tipovuelo ="0"

        else:
            tipovuelo ="N"

        if(len(codvuelo)>0) and (destino!="Seleccionar Lugar") and (tipovuelo != "N"):
            try:
                vuelo =buscar_vuelo(codvuelo)
            except: vuelo = 0 
            if codvuelo!= vuelo:
                formulario_crear_vuelo(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo)
                self.dialogo.show()
                conexion    = conexion_aerocampbd()
                cursor      = conexion.cursor()

                cfvuelos= "update vuelo set confirmacionvuelo='C'where codvuelo='{}';".format(codvuelo)
                self.dialogo.label.setText("Se ha registrado el vuelo correctamente")

                cursor.execute(cfvuelos)
                conexion.commit()
                conexion.close()
            else: self.dialogo.label.setText("Ya existe un vuelo con este codigo")
            self.dialogo.show()
        else: self.dialogo.label.setText("Todos los campos se deben rellenar")
        self.dialogo.show()
        
        self.vuelo.lineEdit_13.setText("")

    def ConfirmarSolicitud(self):
        n           = self.solicitudesPendientesVuelos.cb_listaVuelos.currentText()
        conexion    = conexion_aerocampbd()
        cursor      = conexion.cursor()

        cfvuelos= "update vuelo set confirmacionvuelo='A'where codvuelo='{}';".format(n)
        borrartupla= "delete from soltemp where codvuelo='{}';".format(n)
        cursor.execute(cfvuelos)
        cursor.execute(borrartupla)
        conexion.commit()
        conexion.close()
        self.solicitudesPendientesVuelos.close()
        self.dialogo.label.setText("Vuelo programado con éxito")
        self.dialogo.show()

    def ConsultarAgendaAeropuerto(self):
        conexion = conexion_aerocampbd()
        cursor = conexion.cursor()
        cdvuelos = "select codvuelo, destino, tipovuelo from vuelo where confirmacionvuelo= 'A' ;"
        cursor.execute(cdvuelos)
        listcdvuelos = cursor.fetchall()

        if len(listcdvuelos)>0:
            self.consultarAgenda.show()
        else:
            self.dialogo.label.setText("No hay vuelos programados")
            self.dialogo.show()

        conexion.commit()
        conexion.close()

    def consultarAgenda2(self):
        self.consultarAgenda.tableWidget.setColumnWidth(0,100)
        self.consultarAgenda.tableWidget.setColumnWidth(1,100)
        self.consultarAgenda.tableWidget.setColumnWidth(2,100)

        conexion = conexion_aerocampbd()
        cursor = conexion.cursor()
        date= self.consultarAgenda.dateEdit.text()
        cdvuelos= "select codvuelo, destino, to_char(fechasalida,'YYYY-MM-DD') from vuelo where confirmacionvuelo= 'A' and fechallegada='{}';".format(date)
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        conexion.commit()
        self.consultarAgenda.tableWidget.setRowCount(0)
        fila=0
        for n in listcdvuelos:
            columna=0
            self.consultarAgenda.tableWidget.insertRow(fila)
            for k in n:
                celda = QtWidgets.QTableWidgetItem(k)
                self.consultarAgenda.tableWidget.setItem(fila, columna, celda)
                columna+=1
            fila+=1
        conexion.close()

    def cancelarVueloAeropuerto(self):
        try:
            row = self.consultarAgenda.tableWidget.currentRow()  
            codigo = self.consultarAgenda.tableWidget.item(row,0).text()
            conexion = conexion_aerocampbd()
            cursor = conexion.cursor()
            vueloscancelar= "update vuelo set confirmacionvuelo='R'where codvuelo='{}';".format(codigo)
            cursor.execute(vueloscancelar)

            date= self.consultarAgenda.dateEdit.text()
            cdvuelos= "select codvuelo, destino, to_char(fechasalida,'YYYY-MM-DD') from vuelo where confirmacionvuelo= 'A' and fechallegada='{}';".format(date)
            cursor.execute(cdvuelos)
            listcdvuelos= cursor.fetchall()
            
            self.consultarAgenda.tableWidget.setRowCount(0)
            fila=0
            for n in listcdvuelos:
                columna=0
                self.consultarAgenda.tableWidget.insertRow(fila)
                for k in n:
                    celda = QtWidgets.QTableWidgetItem(k)
                    self.consultarAgenda.tableWidget.setItem(fila, columna, celda)
                    columna+=1
                fila+=1
            
            conexion.commit()
            conexion.close()
            self.dialogo.label.setText("Vuelo cancelado correctamente")
            self.dialogo.show()
        except:
            self.dialogo.label.setText("No se ha seleccionado ningún vuelo")
            self.dialogo.show()

    def editarDatosAerolinea(self):
        self.modificarDatosAeropuerto.pushButton.setEnabled(True)
        self.modificarDatosAeropuerto.lineEdit_2.setEnabled(True)
        self.modificarDatosAeropuerto.lineEdit_3.setEnabled(True)
        self.modificarDatosAeropuerto.lineEdit_4.setEnabled(True)
        self.modificarDatosAeropuerto.lineEdit_6.setEnabled(True)
        self.modificarDatosAeropuerto.lineEdit_7.setEnabled(True)
        self.modificarDatosAeropuerto.comboBox.setEnabled(True)

    def eliminarAerolinea(self):
        try:
            row = self.listadoAerolineas.listView.currentRow()  
            aeronit = self.listadoAerolineas.listView.item(row,1).text()
            if self.listadoAerolineas.listView.rowCount() == 0:
                self.dialogo.label.setText("No hay Aerolineas que eliminar")
                self.dialogo.show()
            else:
                eliminar_aerolineaformtemp(aeronit)
                self.dialogo.label.setText("Aerolinea Eliminada")
                self.dialogo.show()
            self.VisualizarAerolineas()
        except AttributeError:
            self.dialogo.label.setText("No se ha seleccionado una aerolínea")
            self.dialogo.show()
    
    def eliminarVueloAerolinea(self):
        try:
            row = self.agendamientoVuelos.ls_vuelos.currentRow()  
            codvuelo = self.agendamientoVuelos.ls_vuelos.item(row,0).text()
            if self.agendamientoVuelos.ls_vuelos.rowCount() == 0:
                self.dialogo.label.setText("No hay vuelos que eliminar")
                self.dialogo.show()
            else:
                eliminar_vueloAerolinea(codvuelo)
                self.dialogo.label.setText("El vuelo ha sido eliminado")
                self.dialogo.show()
        except AttributeError:
            self.dialogo.label.setText("No se ha seleccionado ningún vuelo")
            self.dialogo.show()
        
        conexion = conexion_aerocampbd()
        cursor = conexion.cursor()
        cdvuelos = "select codvuelo, to_char(fechasalida,'YYYY-MM-DD'), confirmacionvuelo from vuelo where confirmacionvuelo in ('C','R') and aeronit='{}';".format(usuario)

        cursor.execute(cdvuelos)
        listcdvuelos = cursor.fetchall()
        conexion.commit()
        self.agendamientoVuelos.ls_vuelos.setRowCount(0)
        fila = 0
        for n in listcdvuelos:
            columna = 0
            self.agendamientoVuelos.ls_vuelos.insertRow(fila)
            for k in n:
                celda = QtWidgets.QTableWidgetItem(k)
                self.agendamientoVuelos.ls_vuelos.setItem(fila, columna, celda)
                columna+=1
            fila+=1
        conexion.commit()
        conexion.close()

    def enviarpiloto(self):
        nombrepiloto            = self.registrarPiloto.lineEdit_27.text()
        idpiloto                = self.registrarPiloto.lineEdit_28.text()
        nrolicenciapiloto       = self.registrarPiloto.lineEdit_29.text()
        horasexperienciapiloto  = self.registrarPiloto.spinBox_11.text()
        revisionmedicapiloto    = self.registrarPiloto.dateEdit_10.text()
        aeronit                 = usuario

        if(len(nombrepiloto)>0 and len(idpiloto)>0 and len(nrolicenciapiloto)>0):
            if(idpiloto.isnumeric()):
                    formulario_pilotos(idpiloto,aeronit,nombrepiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto)
                    
                    nombrepiloto            = self.registrarPiloto.lineEdit_27.clear()
                    idpiloto                = self.registrarPiloto.lineEdit_28.clear()
                    nrolicenciapiloto       = self.registrarPiloto.lineEdit_29.clear()
                    horasexperienciapiloto  = self.registrarPiloto.spinBox_11.clear()
                    revisionmedicapiloto    = self.registrarPiloto.dateEdit_10.clear()
                    aeronit                 = usuario

                    self.dialogo.label.setText("Se ha registrado el piloto correctamente")
                    self.dialogo.show()
            else:        
                self.dialogo.label.setText("Uno o varios campos se han \n ingresado incorrectamente")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Todos los campos se deben rellenar")
            self.dialogo.show()
    
    def EnviarCopiloto(self):
        nombre              = self.registrarCopiloto.lineEdit_24.text()
        copilotoid          = self.registrarCopiloto.lineEdit_25.text()
        numerolicencia      = self.registrarCopiloto.lineEdit_26.text()
        horasexperiencia    = self.registrarCopiloto.spinBox_10.text()
        revisionmedica      = self.registrarCopiloto.dateEdit_9.text()
        aeronit             = usuario
        
        if(len(nombre)>0 and len(copilotoid)>0 and len(numerolicencia)>0):
            if(copilotoid.isnumeric()):
                    formulario_copilotos(copilotoid,aeronit,nombre,numerolicencia,horasexperiencia,revisionmedica)

                    self.registrarCopiloto.lineEdit_24.clear()
                    self.registrarCopiloto.lineEdit_25.clear()
                    self.registrarCopiloto.lineEdit_26.clear()
                    
                    self.dialogo.label.setText("Se ha registrado el copiloto correctamente")
                    self.dialogo.show()
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
        aeronit         = usuario

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

        avionid         = self.registrarAvion.lineEdit.clear()
        modelo          = self.registrarAvion.lineEdit_2.clear()
        numeromotor     = self.registrarAvion.lineEdit_10.clear()
        pesonominal     = self.registrarAvion.lineEdit_11.clear()
        capacidad       = self.registrarAvion.lineEdit_12.clear()

    def enviarformulario(self):
        nombre_aerolinea= self.formularioRegistro.lineEdit.text()
        nit_aerolinea= self.formularioRegistro.lineEdit_2.text()
        ciu_aerolinea= self.formularioRegistro.comboBox.currentText()
        email_aerolinea= self.formularioRegistro.lineEdit_3.text()
        tel_aerolinea= self.formularioRegistro.lineEdit_4.text()

        if(len(nombre_aerolinea)>0 and len(nit_aerolinea)>0 and len(ciu_aerolinea)>0 and len(email_aerolinea)>0 and len(tel_aerolinea)>0):
            if nit_aerolinea.isnumeric() and tel_aerolinea.isnumeric():
                formulario_aerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea)
                self.formularioRegistro.lineEdit.clear()
                self.formularioRegistro.lineEdit_2.clear()
                self.formularioRegistro.lineEdit_3.clear()
                self.formularioRegistro.lineEdit_4.clear()
                self.dialogo.label.setText("La información de la aerolínea fue enviada \n exitosamente")
                self.dialogo.show()
            else:
                self.dialogo.label.setText("Uno o varios campos se han ingresado \n incorrectamente")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Todos los campos se deben rellenar")
            self.dialogo.show()

    def Ingresar_aeropuerto(self):
        self.aeropuerto.show()
        self.autenticacion.close()

    def Ingresar_aerolinea(self):
        self.aerolinea.show()
        self.autenticacion.close()

    def LlenarFormulario(self):
        self.formularioRegistro.show()

    def modificar_Vuelo(self):
        horasalida          = self.modificarVuelo.timeEdit.text()
        horaentrada         = self.modificarVuelo.timeEdit_2.text()
        fechasalida         = self.modificarVuelo.dateEdit_3.text()
        fechallegada        = self.modificarVuelo.dateEdit_4.text()
        codvuelo            = self.modificarVuelo.lineEdit_13.text()
        destino             = self.modificarVuelo.comboBox.currentText()
        carga               = self.modificarVuelo.comboBox_2.currentText()
        piloto              = self.modificarVuelo.comboBox_3.currentText()
        copiloto            = self.modificarVuelo.comboBox_5.currentText()
        avionid             = self.modificarVuelo.comboBox_6.currentText()
        aeronit             = usuario
        pilotoid            = buscar_idpiloto(piloto,aeronit)
        copilotoid          = buscar_idcopiloto(copiloto,aeronit)

        if (carga == "Carga"):
            tipovuelo = "1"
        elif (carga == "Pasajeros"):
            tipovuelo ="0"
        else:
            tipovuelo ="N"

        if(len(codvuelo)>0) and (destino!="Seleccionar Lugar") and (tipovuelo != "N"):
            formulario_vuelo_modificar(codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid)
            self.dialogo.label.setText("El vuelo se ha modificado exitosamente")
            self.dialogo.show()
            self.modificarVuelo.close()
            conexion = conexion_aerocampbd()
            cursor = conexion.cursor()
            cdvuelos = "select codvuelo, to_char(fechasalida,'YYYY-MM-DD'), confirmacionvuelo from vuelo where confirmacionvuelo in ('C','R') and aeronit='{}';".format(usuario)
            cursor.execute(cdvuelos)
            listcdvuelos = cursor.fetchall()
            conexion.commit()
            self.agendamientoVuelos.ls_vuelos.setRowCount(0)
            fila = 0
            for n in listcdvuelos:
                columna = 0
                self.agendamientoVuelos.ls_vuelos.insertRow(fila)
                for k in n:
                    celda = QtWidgets.QTableWidgetItem(k)
                    self.agendamientoVuelos.ls_vuelos.setItem(fila, columna, celda)
                    columna+=1
                fila+=1
        else: self.dialogo.label.setText("Todos los campos se deben seleccionar")
        self.dialogo.show()

    def modificarAerolinea(self):
        nombre_aerolinea    = self.modificarDatosAeropuerto.lineEdit_4.text()
        nit_aerolinea       = self.modificarDatosAeropuerto.lineEdit_5.text()
        ciu_aerolinea       = self.modificarDatosAeropuerto.comboBox.text()
        email_aerolinea     = self.modificarDatosAeropuerto.lineEdit_6.text()
        tel_aerolinea       = self.modificarDatosAeropuerto.lineEdit_7.text()
        usuario             = self.modificarDatosAeropuerto.lineEdit.text()
        contrasena          = self.modificarDatosAeropuerto.lineEdit_2.text()
        contrasenar         = self.modificarDatosAeropuerto.lineEdit_3.text()
        if len(contrasena)>0 and len(contrasenar)>0:
            if(contrasena == contrasenar):
                formulario_usuario_modificar(usuario, contrasena)
                formulario_registrosaerolineas_modificar(nit_aerolinea, nombre_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea)

                nombre_aerolinea    = self.modificarDatosAeropuerto.lineEdit_4.clear()
                nit_aerolinea       = self.modificarDatosAeropuerto.lineEdit_5.clear()
                ciu_aerolinea       = self.modificarDatosAeropuerto.comboBox.clear()
                email_aerolinea     = self.modificarDatosAeropuerto.lineEdit_6.clear()
                tel_aerolinea       = self.modificarDatosAeropuerto.lineEdit_7.clear()
                usuario             = self.modificarDatosAeropuerto.lineEdit.clear()
                contrasena          = self.modificarDatosAeropuerto.lineEdit_2.clear()
                contrasenar         = self.modificarDatosAeropuerto.lineEdit_3.clear()

                self.modificarDatosAeropuerto.close()
                self.dialogo.label.setText("Los datos de la aerolinea fueron modificados exitosamente")
                self.dialogo.show()
                if buscar_identificador == "P":
                    self.VisualizarAerolineas()
            else:
                self.dialogo.label.setText("Las contraseñas no coinciden")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Todos los campos deben ser rellenados")
            self.dialogo.show()

    def modificarDatosAerop(self):
        try:
            row = self.listadoAerolineas.listView.currentRow()  
            aeronit     = self.listadoAerolineas.listView.item(row,1).text()
            nombre      = buscar_nombreaerolinea2(aeronit)
            ciudad      = buscar_ciuaerolinea2(aeronit)
            email       = buscar_correoaerolinea2(aeronit)
            telefono    = buscar_telaerolinea2(aeronit)

            self.modificarDatosAeropuerto.lineEdit_4.setText(nombre)
            self.modificarDatosAeropuerto.lineEdit_5.setText(aeronit)
            self.modificarDatosAeropuerto.comboBox.setText(ciudad)
            self.modificarDatosAeropuerto.lineEdit_6.setText(email)
            self.modificarDatosAeropuerto.lineEdit_7.setText(telefono)
            self.modificarDatosAeropuerto.lineEdit.setText(aeronit)
            self.modificarDatosAeropuerto.show()
        except AttributeError:
            self.dialogo.label.setText("No se ha seleccionado una aerolínea")
            self.dialogo.show()
    
    def modificarDatosAerolineaPropios(self):
        self.modificarDatosAeropuerto.pushButton.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit_2.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit_3.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit_4.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit_5.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit_6.setEnabled(False)
        self.modificarDatosAeropuerto.lineEdit_7.setEnabled(False)
        self.modificarDatosAeropuerto.comboBox.setEnabled(False)
        aeronit     = usuario
        nombre      = buscar_nombreaerolinea2(aeronit)
        ciudad      = buscar_ciuaerolinea2(aeronit)
        email       = buscar_correoaerolinea2(aeronit)
        telefono    = buscar_telaerolinea2(aeronit)

        self.modificarDatosAeropuerto.lineEdit_4.setText(nombre)
        self.modificarDatosAeropuerto.lineEdit_5.setText(aeronit)
        self.modificarDatosAeropuerto.comboBox.setText(ciudad)
        self.modificarDatosAeropuerto.lineEdit_6.setText(email)
        self.modificarDatosAeropuerto.lineEdit_7.setText(telefono)
        self.modificarDatosAeropuerto.lineEdit.setText(aeronit)

        self.modificarDatosAeropuerto.show()

    def modificarVueloAerolinea(self):
        try:
            aeronit = usuario
            self.modificarVuelo.comboBox_3.clear()
            listpilotos = listado_pilotos(aeronit)
            for n in listpilotos:
                for k in n:
                    self.modificarVuelo.comboBox_3.addItem(k)
            self.modificarVuelo.comboBox_5.clear()
            listcopilotos = listado_copilotos(aeronit)
            for m in listcopilotos:
                for j in m:
                    self.modificarVuelo.comboBox_5.addItem(j)
            self.modificarVuelo.comboBox_6.clear()
            listaviones = listado_aviones(aeronit)
            for d in listaviones:
                for a in d:
                    self.modificarVuelo.comboBox_6.addItem(a)       

            row             = self.agendamientoVuelos.ls_vuelos.currentRow()  
            codvuelo        = self.agendamientoVuelos.ls_vuelos.item(row,0).text()
            tipovuelo       = buscar_tipovuelo(codvuelo,aeronit)
            fechasalida     = buscar_fechasalida (codvuelo,aeronit)
            fechallegada    = buscar_fechallegada (codvuelo,aeronit)
            # horasalida      = buscar_horasalida (codvuelo,aeronit)
            # horallegada     = buscar_horallegada (codvuelo,aeronit)
            destinos        = ["Pasto","Bogota","Medellin","Cali"]
            destino         = buscar_destino(codvuelo,aeronit)
            pilotos         = listado_pilotos(aeronit)
            copilotos       = listado_copilotos(aeronit)
            aviones         = listado_aviones(aeronit)
            pilotonom       = buscar_nompiloto(codvuelo,aeronit)
            copilotonom     = buscar_nomcopiloto(codvuelo,aeronit)
            avioncod        = buscar_codavion(codvuelo,aeronit)

            index = 0
            if tipovuelo == '0':
                index = 1
            elif tipovuelo == '1':
                index = 2
            else:
                index = 0

            indexp = 0
            cont   = 0
            for piloto in pilotos:
                for i in piloto:
                    if i == pilotonom:
                        indexp = cont
                cont = cont + 1 

            indexc = 0
            cont   = 0
            for copiloto in copilotos:
                for i in copiloto:
                    if i == copilotonom:
                        indexc = cont
                cont = cont + 1 

            indexa = 0
            cont   = 0
            for avion in aviones:
                for i in avion:
                    if i == avioncod:
                        indexa = cont
                cont = cont + 1  

            indexd = 0
            cont   = 0
            for dest in destinos:
                if destino == dest:
                    indexd = cont+1
                cont = cont + 1
            
            self.modificarVuelo.lineEdit_13.setEnabled(False)
            self.modificarVuelo.lineEdit_13.setText(codvuelo)
            self.modificarVuelo.dateEdit_3.setDate(fechasalida)
            self.modificarVuelo.dateEdit_4.setDate(fechallegada)
            # self.modificarVuelo.timeEdit.setDateTime(QDateTime(0,0,0,0,0))
            # self.modificarVuelo.timeEdit_2.setDateTime(QDateTime(0,0,0,0,0))
            self.modificarVuelo.comboBox_2.setCurrentIndex(index)
            self.modificarVuelo.comboBox_3.setCurrentIndex(indexp)
            self.modificarVuelo.comboBox_5.setCurrentIndex(indexc)
            self.modificarVuelo.comboBox_6.setCurrentIndex(indexa)
            self.modificarVuelo.comboBox.setCurrentIndex(indexd)
            self.modificarVuelo.show()
        except AttributeError:
            self.dialogo.label.setText("No se ha seleccionado ningún vuelo")
            self.dialogo.show()

    def rechazarvuelo(self):
        
        codigo = self.solicitudesPendientesVuelos.cb_listaVuelos.currentText()
        if self.solicitudesPendientesVuelos.cb_listaVuelos.count() == 0:
            self.dialogo.label.setText("No hay solicitudes que rechazar")
            self.dialogo.show()
        else:
            borrar_vuelosoltemp(codigo)
            self.dialogo.label.setText("Solicitud rechazada")
            self.dialogo.show()
            conexion    = conexion_aerocampbd()
            cursor      = conexion.cursor()

            cfvuelos= "update vuelo set confirmacionvuelo='R'where codvuelo='{}';".format(codigo)

            cursor.execute(cfvuelos)
            conexion.commit()
            conexion.close()
        listvuelos = listado_vuelos()
        self.solicitudesPendientesVuelos.cb_listaVuelos.clear()
        for n in listvuelos:
            for k in n:
                self.solicitudesPendientesVuelos.cb_listaVuelos.addItem(k)
        self.solicitudesPendientesVuelos.update()

    def rechazarusuario(self):
        nombre = self.solicitudesRegistroAerolinea.comboBox.currentText()
        if self.solicitudesRegistroAerolinea.comboBox.count() == 0:
            self.dialogo.label.setText("No hay solicitudes que rechazar")
            self.dialogo.show()
        else:
            borrar_aerolineaformtemp(nombre)
            self.dialogo.label.setText("Solicitud rechazada")
            self.dialogo.show()
        listsoliaero    = listado_aerolineasusuario()
        self.solicitudesRegistroAerolinea.comboBox.clear()
        for n in listsoliaero:
            for k in n:
                self.solicitudesRegistroAerolinea.comboBox.addItem(k)
        self.solicitudesRegistroAerolinea.update()
        
    def registraraerolinea(self):
        nombre_aerolinea    = self.modificarDatosAerolinea.lineEdit_4.text()
        nit_aerolinea       = self.modificarDatosAerolinea.lineEdit_5.text()
        ciu_aerolinea       = self.modificarDatosAerolinea.comboBox.text()
        email_aerolinea     = self.modificarDatosAerolinea.lineEdit_6.text()
        tel_aerolinea       = self.modificarDatosAerolinea.lineEdit_7.text()
        usuario             = self.modificarDatosAerolinea.lineEdit.text()
        contrasena          = self.modificarDatosAerolinea.lineEdit_2.text()
        contrasenar         = self.modificarDatosAerolinea.lineEdit_3.text()
        identificador       = 'A'
        
        if len(contrasena)>0 and len(contrasenar)>0:
            if(contrasena == contrasenar and nit_aerolinea == usuario):
                formulario_usuario(identificador,usuario,contrasena)
                formulario_registrosaerolineas(nombre_aerolinea,nit_aerolinea,ciu_aerolinea,email_aerolinea, tel_aerolinea)

                borrar_aerolineaformtemp(nombre_aerolinea)
                listsoliaero = listado_aerolineasusuario()
                self.solicitudesRegistroAerolinea.comboBox.clear()
                for n in listsoliaero:
                    for k in n:
                        self.solicitudesRegistroAerolinea.comboBox.addItem(k)

                nombre_aerolinea    = self.modificarDatosAerolinea.lineEdit_4.clear()
                nit_aerolinea       = self.modificarDatosAerolinea.lineEdit_5.clear()
                ciu_aerolinea       = self.modificarDatosAerolinea.comboBox.clear()
                email_aerolinea     = self.modificarDatosAerolinea.lineEdit_6.clear()
                tel_aerolinea       = self.modificarDatosAerolinea.lineEdit_7.clear()
                usuario             = self.modificarDatosAerolinea.lineEdit.clear()
                contrasena          = self.modificarDatosAerolinea.lineEdit_2.clear()
                contrasenar         = self.modificarDatosAerolinea.lineEdit_3.clear()

                self.modificarDatosAerolinea.close()
                self.solicitudesRegistroAerolinea.update() 
                self.dialogo.label.setText("La aerolínea fue registrada exitosamente")
                self.dialogo.show()
            else:
                self.dialogo.label.setText("Las contraseñas no coinciden")
                self.dialogo.show()
        else:
            self.dialogo.label.setText("Hace falta información para crear el usuario")
            self.dialogo.show()

    def RegistrarAvion(self):
        self.registrarAvion.show()

    def RegistrarCopiloto(self):
        self.registrarCopiloto.show()

    def RegistrarPiloto(self):
        self.registrarPiloto.show()

    def RealizarSolicitud(self):
        try:
            row = self.agendamientoVuelos.ls_vuelos.currentRow()  
            codigo = self.agendamientoVuelos.ls_vuelos.item(row,0).text()
            conexion = conexion_aerocampbd()
            cursor = conexion.cursor()
            cfvuelos= "update vuelo set confirmacionvuelo='E'where codvuelo='{}';".format(codigo)
            cursor.execute(cfvuelos)
            cdvuelos = "select codvuelo, to_char(fechasalida,'YYYY-MM-DD'), confirmacionvuelo from vuelo where confirmacionvuelo in ('C','R') and aeronit='{}';".format(usuario)

            cursor.execute(cdvuelos)
            listcdvuelos = cursor.fetchall()
            conexion.commit()
            ls = self.agendamientoVuelos.ls_vuelos.selectedItems()
            for n in ls:
                cdvuelos= "insert into soltemp values('{}');".format(n.text())
                cursor.execute(cdvuelos)
            self.agendamientoVuelos.ls_vuelos.setRowCount(0)
            fila = 0
            for n in listcdvuelos:
                columna = 0
                self.agendamientoVuelos.ls_vuelos.insertRow(fila)
                for k in n:
                    celda = QtWidgets.QTableWidgetItem(k)
                    self.agendamientoVuelos.ls_vuelos.setItem(fila, columna, celda)
                    columna+=1
                fila+=1
            conexion.commit()
            conexion.close()
            self.dialogo.label.setText("La solicitud fue enviada con éxito")
            self.dialogo.show()
        except AttributeError:
            self.dialogo.label.setText("No se ha seleccionado ningún vuelo")
            self.dialogo.show()

    def ProgramarVuelo(self):
        aeronit = usuario
        self.vuelo.comboBox_3.clear()
        listpilotos = listado_pilotos(aeronit)
        for n in listpilotos:
            for k in n:
                self.vuelo.comboBox_3.addItem(k)
        self.vuelo.comboBox_5.clear()
        listcopilotos = listado_copilotos(aeronit)
        for m in listcopilotos:
            for j in m:
                self.vuelo.comboBox_5.addItem(j)
        self.vuelo.comboBox_6.clear()
        listaviones = listado_aviones(aeronit)
        for d in listaviones:
            for a in d:
                self.vuelo.comboBox_6.addItem(a)       
        self.vuelo.show()

    def SolicitudesVuelos(self):
        self.solicitudesPendientesVuelos.cb_listaVuelos.clear()
        conexion = conexion_aerocampbd()
        cursor = conexion.cursor()
        solicitudesaeroc = "select * from soltemp;"
        cursor.execute(solicitudesaeroc)
        listsolicitudes= cursor.fetchall()
        conexion.commit()
        for n in listsolicitudes:
            for k in n:
                self.solicitudesPendientesVuelos.cb_listaVuelos.addItem(k)
        conexion.close()
        
        if self.solicitudesPendientesVuelos.cb_listaVuelos.count()==0:
            self.solicitudesPendientesVuelos.bt_buscarDisponibilidad.setEnabled(True)
            self.solicitudesPendientesVuelos.bt_confirmarSolicitud.setEnabled(False)
            self.solicitudesPendientesVuelos.bt_rechazarSolicitud.setEnabled(False)
        self.solicitudesPendientesVuelos.show()

    def SolicitarAgendamiento(self):
        self.agendamientoVuelos.ls_vuelos.setColumnWidth(0,100)
        self.agendamientoVuelos.ls_vuelos.setColumnWidth(1,100)
        self.agendamientoVuelos.ls_vuelos.setColumnWidth(2,100)
        
        conexion = conexion_aerocampbd()
        cursor   = conexion.cursor()
        cdvuelos = "select codvuelo, to_char(fechasalida,'YYYY-MM-DD'), confirmacionvuelo from vuelo where confirmacionvuelo in ('C','R') and aeronit='{}';".format(usuario)

        cursor.execute(cdvuelos)
        listcdvuelos = cursor.fetchall()
        conexion.commit()
        self.agendamientoVuelos.ls_vuelos.setRowCount(0)
        fila = 0
        for n in listcdvuelos:
            columna = 0
            self.agendamientoVuelos.ls_vuelos.insertRow(fila)
            for k in n:
                celda = QtWidgets.QTableWidgetItem(k)
                self.agendamientoVuelos.ls_vuelos.setItem(fila, columna, celda)
                columna+=1
            fila+=1
        conexion.close()

        if len(listcdvuelos)>0:
            self.agendamientoVuelos.show()
            self.agendamientoVuelos.bt_realizarSolicitud.setEnabled(True)
            self.agendamientoVuelos.bt_modificarDatos.setEnabled(True)
            self.agendamientoVuelos.bt_eliminarVuelo.setEnabled(True)
        else:
            self.agendamientoVuelos.show()
            self.agendamientoVuelos.bt_realizarSolicitud.setEnabled(False)
            self.agendamientoVuelos.bt_modificarDatos.setEnabled(False)
            self.agendamientoVuelos.bt_eliminarVuelo.setEnabled(False)
    
    def visualizarvuelos(self):
            self.visualizarVuelos.tableWidget.setColumnWidth(0,100)
            self.visualizarVuelos.tableWidget.setColumnWidth(1,100)
            self.visualizarVuelos.tableWidget.setColumnWidth(2,100)
            
            conexion = conexion_aerocampbd()
            cursor   = conexion.cursor()
            cdvuelos = "select codvuelo,to_char(fechasalida,'YYYY-MM-DD'),confirmacionvuelo from vuelo where aeronit='{}';".format(usuario)
            cursor.execute(cdvuelos)
            listcdvuelos = cursor.fetchall()
            conexion.commit()
            if len(listcdvuelos)>0:
                self.visualizarVuelos.tableWidget.setRowCount(0)
                fila = 0
                for n in listcdvuelos:
                    columna = 0
                    self.visualizarVuelos.tableWidget.insertRow(fila)
                    for k in n:
                        celda = QtWidgets.QTableWidgetItem(k)
                        self.visualizarVuelos.tableWidget.setItem(fila, columna, celda)
                        columna+=1
                    fila+=1
                conexion.close()
                self.visualizarVuelos.show()
            else:
                self.dialogo.label.setText("No existen vuelos registrados")
                self.dialogo.show()

    def verSolicitudesRegistro(self):
        listsoliaero = listado_aerolineasusuario()
        self.solicitudesRegistroAerolinea.comboBox.clear()
        for n in listsoliaero:
            for k in n:
                self.solicitudesRegistroAerolinea.comboBox.addItem(k)
        if self.solicitudesRegistroAerolinea.comboBox.count() > 0:
            self.solicitudesRegistroAerolinea.show()
        else:
            self.dialogo.label.setText("No hay aerolíneas registradas")
            self.dialogo.show()

    def VerDatosAerolinea(self):
        self.modificarDatosAerolinea.show()

    def VisualizarAerolineas(self):
        conexion = conexion_aerocampbd()
        cursor       = conexion.cursor()
        cdvuelos     = "select nombreaerolinea, aeronit from aerolinea;"
        cursor.execute(cdvuelos)
        listcdvuelos = cursor.fetchall()
        conexion.commit()
        self.listadoAerolineas.listView.setRowCount(0)
        fila = 0
        for n in listcdvuelos:
            columna = 0 
            self.listadoAerolineas.listView.insertRow(fila)
            for k in n:
                celda = QtWidgets.QTableWidgetItem(k)
                self.listadoAerolineas.listView.setItem(fila, columna, celda)
                columna+=1
            fila+=1
        if self.listadoAerolineas.listView.rowCount() == 0:
            self.dialogo.label.setText("No hay aerolíneas registradas")
            self.dialogo.show()
        else:
            self.listadoAerolineas.show()
        conexion.close()

    def Salir(self):
        self.aerolinea.close()
        self.aeropuerto.close()
        self.agendamientoVuelos.close()
        self.consultarAgenda.close()
        self.formularioRegistro.close()
        self.listadoAerolineas.close()
        self.modificarDatosAerolinea.close()
        self.modificarDatosAeropuerto.close()
        self.registrarAvion.close()
        self.registrarCopiloto.close()
        self.registrarPiloto.close()
        self.solicitudesPendientesVuelos.close()
        self.solicitudesRegistroAerolinea.close()
        self.visualizarVuelos.close()
        self.vuelo.close()
        self.dialogo.close()
        self.autenticacion.show()

iniciar()