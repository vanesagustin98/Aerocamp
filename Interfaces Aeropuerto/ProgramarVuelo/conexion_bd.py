import psycopg2

def conexion_aerocampbd():
    conexion = psycopg2.connect(
        host = "localhost" , 
        database = "aerocampbd" ,
        user = "postgres" ,
        password = "zVGR1233191877"
        )
    return conexion