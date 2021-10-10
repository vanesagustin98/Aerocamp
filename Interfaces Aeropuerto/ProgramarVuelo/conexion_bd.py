import psycopg2

def conexion_aerocampbd():
    conexion = psycopg2.connect(
        host = "localhost" , 
        database = "aerocamp" ,
        user = "postgres" ,
        password = "root1"
        )
    return conexion