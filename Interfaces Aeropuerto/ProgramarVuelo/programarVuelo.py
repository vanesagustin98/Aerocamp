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
        self.autenticacion.pushButton.clicked.connect(self.Ingresar)
        #self.autenticacion.pushButton.clicked.connect(self.Ingresar)
        self.aeropuerto.bt_visualizarAerolineas.clicked.connect(self.VisualizarAerolineas)
        self.aerolinea.bt_visualizarDatos.clicked.connect(self.VerDatosAerolinea)
        self.listadoAerolineas.pushButton.clicked.connect(self.VerListadoAeropuerto)
        self.aerolinea.pushButton_4.clicked.connect(self.RegistrarAvion)
        self.aerolinea.pushButton_3.clicked.connect(self.RegistrarCopiloto)
        self.aerolinea.pushButton_2.clicked.connect(self.RegistrarPiloto)
        self.aeropuerto.bt_revisarSoliRegistros.clicked.connect(self.verSolicitudesRegistro)
        self.formularioRegistro.pushButton.clicked.connect(self.enviarformulario)
        app.exec()

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

    def Ingresar(self):

        self.aerolinea.show()
        self.aeropuerto.show()
        self.autenticacion.close()

    def LlenarFormulario(self):
        self.formularioRegistro.show()

    def ProgramarVuelo(self):  
        self.vuelo.show()

    def CrearVuelo(self):

        #Piloto
        nombrepiloto = self.vuelo.lineEdit_15.text()
        idpiloto = self.vuelo.lineEdit_16.text()
        nrolicenciapiloto = self.vuelo.lineEdit_17.text()
        horasexperienciapiloto = self.vuelo.spinBox_6.text()
        revisionmedicapiloto = self.vuelo.dateEdit_5.text()
        piloto = "insert into piloto values('{}','{}','{}','{}','{}')".format(idpiloto,nombrepiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto)

        #Copiloto
        nombrecopiloto = self.vuelo.lineEdit_4.text()
        idcopiloto = self.vuelo.lineEdit_5.text()
        nrolicenciacopiloto = self.vuelo.lineEdit_6.text()
        horasexperienciacopiloto = self.vuelo.spinBox_3.text()
        revisionmedicacopiloto = self.vuelo.dateEdit_2.text()
        copiloto= "insert into copiloto values('{}','{}','{}','{}','{}')".format( idcopiloto,nombrecopiloto,nrolicenciacopiloto,horasexperienciacopiloto,revisionmedicacopiloto)

        #Avion 
        idavion =self.vuelo.lineEdit_7.text()
        modelo =self.vuelo.lineEdit_8.text()
        tipopropulsion =self.vuelo.comboBox_2.currentText()
        numerodemotor =self.vuelo.lineEdit_10.text()
        pesonominal =self.vuelo.lineEdit_11.text()
        capacidad =self.vuelo.lineEdit_11.text()
        carga= self.vuelo.radioButton.isChecked()
        pasajeros= self.vuelo.radioButton_2.isChecked()
        

        if (carga is True) :
            tipo= "1"
        elif (pasajeros is True):
            tipo="0"
        else:
            tipo="NS"

        avion = "insert into avion values('{}','{}','{}','{}','{}','{}','{}')".format(idavion,modelo,tipopropulsion,pesonominal,capacidad,tipo,numerodemotor)

        #Vuelo
        fechasalida = self.vuelo.dateEdit_3.text()
        horasalida= self.vuelo.timeEdit.text()
        fechallegada = self.vuelo.dateEdit_4.text()
        horallegada= self.vuelo.timeEdit_2.text()
        cdvuelo =self.vuelo.lineEdit_13.text()
        destino = self.vuelo.comboBox.currentText()
        nitaerolinea= "1234"
        confirmacionVuelo = "1"

        vuelo = "insert into vuelo values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(cdvuelo,destino,fechasalida,fechallegada,horasalida,horallegada,idpiloto,idcopiloto,idavion,nitaerolinea,confirmacionVuelo)

        if (nombrepiloto.__len__() > 0 and idpiloto.__len__() > 0 and nrolicenciapiloto.__len__() > 0 and nombrecopiloto.__len__() > 0 
        and idcopiloto.__len__() > 0 and nrolicenciapiloto.__len__() > 0 and idavion.__len__() > 0 and modelo.__len__() > 0 
        and numerodemotor.__len__() > 0 and pesonominal.__len__() > 0 and capacidad.__len__() > 0 and cdvuelo.__len__() > 0) :
            if(capacidad.isnumeric() and numerodemotor.isnumeric() and pesonominal.isnumeric() and idcopiloto.isnumeric() 
            and idpiloto.isnumeric() and nrolicenciacopiloto.isnumeric() and nrolicenciapiloto.isnumeric()):
                conexion = conexion_aerocampbd()
                print("Conexión exitosa")
                cursor = conexion.cursor()
                cursor.execute(piloto)
                cursor.execute(copiloto)
                cursor.execute(avion)
                cursor.execute(vuelo)
                conexion.commit()
                print("Tablas creada con éxito")
                conexion.close()
                
                print(nombrepiloto,idpiloto,nrolicenciapiloto,horasexperienciapiloto,revisionmedicapiloto)
                print(nombrecopiloto,idcopiloto,nrolicenciacopiloto,horasexperienciacopiloto,revisionmedicacopiloto)
                print(idavion, modelo, tipopropulsion,numerodemotor, pesonominal, capacidad, tipo )
                print(fechasalida, horasalida, fechallegada, horallegada, cdvuelo, destino)


                self.dialogo.show()
                self.vuelo.lineEdit_15.setText("")
                self.vuelo.lineEdit_16.setText("")
                self.vuelo.lineEdit_17.setText("")
                self.vuelo.lineEdit_4.setText("")
                self.vuelo.lineEdit_5.setText("")
                self.vuelo.lineEdit_6.setText("")
                self.vuelo.lineEdit_7.setText("")
                self.vuelo.lineEdit_8.setText("")
                self.vuelo.lineEdit_10.setText("")
                self.vuelo.lineEdit_11.setText("")
                self.vuelo.lineEdit_12.setText("")
                self.vuelo.lineEdit_13.setText("")
                self.vuelo.close()
            else:
                self.dialogo.show()

        else:
            self.dialogo.show()



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
        solicitudesaeroc= "select * from solicitudesaeropuerto;"
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

        self.model_1 = QStandardItemModel(self.consultarAgenda.tableWidget)
        self.model_1.clear()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select codvuelo from vuelo where confirmacionvuelo= '0' ;"
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
        
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        date= self.consultarAgenda.dateEdit.text()
        cdvuelos= "select codvuelo, destino, fechasalida, fechallegada from vuelo where confirmacionvuelo= '0' and fechallegada='{}';".format(date)
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        for n in listcdvuelos:
            for k in n:
                self.model_1.setHorizontalHeaderLabels(['Codigo','Destino','Fecha Salida','Fecha llegada'])
                print("hecho")
                self.consultarAgenda.tableWidget.setModel(self.model_1)
                # self.consultarAgenda.tableWidget.addItem(k)
        print(type(listcdvuelos))
        conexion.close()

    def SolicitarAgendamiento(self):
        
        self.model = QStandardItemModel(self.agendamientoVuelos.ls_vuelos)
        self.model.clear()
        conexion = conexion_aerocampbd()
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select codvuelo, destino, fechasalida, fechallegada from vuelo;"
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        for n in listcdvuelos:
            for k in n:
                
                self.model.setHorizontalHeaderLabels(['Codigo','Destino','Fecha Salida','Fecha llegada'])
                self.agendamientoVuelos.ls_vuelos.setModel(self.model)
                # self.model.setItem(1, 1, k)
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
        borrartupla= "delete from solicitudesaeropuerto where codvuelo='{}';".format(n)
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
            cdvuelos= "insert into solicitudesaeropuerto values('{}');".format(n.text())
            print(n.text())
            cursor.execute(cdvuelos)
        conexion.commit()
        print("Datos agregados con éxito")
        
        conexion.close()

        self.dialogo.show()
        
    def Salir(self):
        sys.exit()

iniciar()