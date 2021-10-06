import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import psycopg2

class iniciar:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.aerolinea = uic.loadUi("interfazAerolinea.ui")
        self.aeropuerto = uic.loadUi("interfazAeropuerto.ui")
        self.vuelo = uic.loadUi("vuelo.ui")
        self.solicitudesPendientesVuelos = uic.loadUi("solicitudesPendientesVuelos.ui")
        self.agendamientoVuelos = uic.loadUi("agendamientoVuelos.ui")
        self.consultarAgenda = uic.loadUi("consultarAgenda.ui")
        self.dialogoVueloProgramado = uic.loadUi("dialogoVueloProgramado.ui")
        self.dialogoDisponibilidad = uic.loadUi("dialogoDisponibilidad.ui")
        self.dialogoAgendamiento = uic.loadUi("dialogoAgendamiento.ui")
        self.dialogoCampos = uic.loadUi("dialogoCampos.ui")
        self.dialogoCamposIncorrectos = uic.loadUi("dialogoCamposIncorrectos.ui")
        self.dialogoNoVuelosProgramados = uic.loadUi("dialogoNOvuelosprogramados.ui")

        self.vuelo.label.setPixmap(QPixmap("D:\Vanessa\Documents\Semestre 5\Ingeniera de Software III\Interfaces Aeropuerto\iconopiloto.jpg"))
        self.vuelo.label_2.setPixmap(QPixmap("D:\Vanessa\Documents\Semestre 5\Ingeniera de Software III\Interfaces Aeropuerto\iconopiloto - copia.jpg"))
        self.vuelo.label_3.setPixmap(QPixmap("D:\Vanessa\Documents\Semestre 5\Ingeniera de Software III\Interfaces Aeropuerto\iconoregistroavion.jpg"))
        self.vuelo.label_4.setPixmap(QPixmap("D:\Vanessa\Documents\Semestre 5\Ingeniera de Software III\Interfaces Aeropuerto\iconoprogramarvuelo.jpg"))
        self.vuelo.tabWidget.setStyleSheet("QMainWindow{background-image: url(D:\Vanessa\Documents\Semestre 5\Ingeniera de Software III\Interfaces Aeropuerto\transparente.png)}")



        self.aerolinea.show()
        # self.aeropuerto.show()

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
        app.exec()

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
                conexion = psycopg2.connect(
                    host = "localhost" , 
                    database = "aerocamp" ,
                    user = "postgres" ,
                    password = "zVGR1233191877"
                    )
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


                self.dialogoVueloProgramado.show()
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
                self.dialogoCamposIncorrectos.show()

        else:
            self.dialogoCampos.show()


        #self.dialogoVueloProgramado.show()

    def BuscarDisponibilidad(self):
        ##aquiuiiii
        n=self.solicitudesPendientesVuelos.cb_listaVuelos.currentText()
        self.consultarAgenda.tableWidget.clear()
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
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
            self.dialogoDisponibilidad.label.setText("Hay espacio en la agenda para programar el vuelo")
            self.dialogoDisponibilidad.show()
        else: 
            self.solicitudesPendientesVuelos.bt_confirmarSolicitud.setEnabled(False)
            self.solicitudesPendientesVuelos.bt_rechazarSolicitud.setEnabled(True)
            self.dialogoDisponibilidad.label.setText("No hay espacio en la agenda para programar el vuelo")
            self.dialogoDisponibilidad.show()
        
        conexion.commit()
        print("Consulta hecha con éxito")
        conexion.close()


    def SolicitudesVuelos(self):
        
        self.solicitudesPendientesVuelos.cb_listaVuelos.clear()
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
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

        self.consultarAgenda.tableWidget.clear()
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select codvuelo from vuelo where confirmacionvuelo= '0' ;"
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()

        if len(listcdvuelos)>0:
            self.consultarAgenda.show()
        else:
            self.dialogoNoVuelosProgramados.show()

        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")

        conexion.close()



    def consultarAgenda2(self):
        self.consultarAgenda.tableWidget.clear()
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
        print("Conexión exitosa")
        cursor = conexion.cursor()
        date= self.consultarAgenda.dateEdit.text()
        cdvuelos= "select codvuelo from vuelo where confirmacionvuelo= '0' and fechallegada='{}';".format(date)
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        for n in listcdvuelos:
            for k in n:
                self.consultarAgenda.tableWidget.addItem(k)
        print(type(listcdvuelos))
        conexion.close()

    def SolicitarAgendamiento(self):
        

        self.agendamientoVuelos.ls_vuelos.clear()
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
        print("Conexión exitosa")
        cursor = conexion.cursor()
        cdvuelos= "select codvuelo from vuelo;"
        cursor.execute(cdvuelos)
        listcdvuelos= cursor.fetchall()
        print(type(listcdvuelos))
        conexion.commit()
        print("Consulta hecha con éxito")
        for n in listcdvuelos:
            for k in n:
                self.agendamientoVuelos.ls_vuelos.addItem(k)
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
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
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

        self.dialogoVueloProgramado.show()
        
    def RealizarSolicitud(self):       
        conexion = psycopg2.connect(
            host = "localhost" , 
            database = "aerocamp" ,
            user = "postgres" ,
            password = "zVGR1233191877"
            )
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

        self.dialogoAgendamiento.show()
        
    def Salir(self):
        sys.exit()

iniciar()