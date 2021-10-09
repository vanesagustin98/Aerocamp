import psycopg2
class conexion:
    def __init__(self, password):
        self.password = password
        pass
    def conectar(self):
        psycopg2.connect(
            host        = "localhost" , 
            database    = "aerocamp" ,
            user        = "postgres" ,
            password    = self.password
            )
        print("Conexión exitosa")
        # cursor = conexion.cursor()
        # cursor = self.conectar.cursor()
        pass

        #probando