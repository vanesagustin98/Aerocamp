import psycopg2

def conexion_aerocampbd():
    conexion = psycopg2.connect(
        host = "localhost" , 
        database = "aerocamp" ,
        user = "postgres" ,
        password = "1204"
        )
    return conexion