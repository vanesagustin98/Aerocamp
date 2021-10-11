-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/RTGET5
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "piloto" (
    "pilotoid" char(10)   NOT NULL,
    "aeronit" varchar(10)   NOT NULL,
    "nombre" varchar(30)   NOT NULL,
    "numerolicencia" varchar(10)   NOT NULL,
    "horasexperiencia" varchar(7)   NOT NULL,
    "revisionmedica" date   NOT NULL,
    CONSTRAINT "pk_piloto" PRIMARY KEY (
        "pilotoid"
     )
);

CREATE TABLE "copiloto" (
    "copilotoid" char(10)   NOT NULL,
    "aeronit" varchar(10)   NOT NULL,
    "nombre" varchar(30)   NOT NULL,
    "numerolicencia" varchar(10)   NOT NULL,
    "horasexperiencia" varchar(7)   NOT NULL,
    "revisionmedica" date   NOT NULL,
    CONSTRAINT "pk_copiloto" PRIMARY KEY (
        "copilotoid"
     )
);

CREATE TABLE "avion" (
    "avionid" varchar(10)   NOT NULL,
    "aeronit" varchar(10)   NOT NULL,
    "modelo" varchar(30)   NOT NULL,
    "tipopropulsion" varchar(30)   NOT NULL,
    "numeromotor" char(2)   NOT NULL,
    "pesonominal" varchar(30)   NOT NULL,
    "capacidad" varchar(30)   NOT NULL,
    CONSTRAINT "pk_avion" PRIMARY KEY (
        "avionid"
     )
);

CREATE TABLE "vuelo" (
    "codvuelo" varchar(10)   NOT NULL,
    "aeronit" varchar(10)   NOT NULL,
    "tipovuelo" char(1)   NOT NULL,
    "destino" varchar(30)   NOT NULL,
    "fechasalida" date   NOT NULL,
    "fechallegada" date   NOT NULL,
    "horasalida" time   NOT NULL,
    "horaentrada" time   NOT NULL,
    "pilotoid" char(10)   NOT NULL,
    "copilotoid" char(10)   NOT NULL,
    "avionid" varchar(10)   NOT NULL,
    "confirmacionvuelo" char(1)   NOT NULL,
    CONSTRAINT "pk_vuelo" PRIMARY KEY (
        "codvuelo"
     )
);

CREATE TABLE "aerolinea" (
    "aeronit" varchar(10)   NOT NULL,
    "nombreaerolinea" varchar(30)   NOT NULL,
    "ciudad" varchar(30)   NOT NULL,
    "email" varchar(30)   NOT NULL,
    "telefono" varchar(30)   NOT NULL,
    CONSTRAINT "pk_aerolinea" PRIMARY KEY (
        "aeronit"
     )
);

CREATE TABLE "formtemp" (
    "aeronit" varchar(10)   NOT NULL,
    "nombreaerolinea" varchar(30)   NOT NULL,
    "ciudad" varchar(30)   NOT NULL,
    "email" varchar(30)   NOT NULL,
    "telefono" varchar(30)   NOT NULL,
    CONSTRAINT "pk_formtemp" PRIMARY KEY (
        "aeronit"
     )
);

CREATE TABLE "aeropuerto" (
    "idaeropuerto" varchar(10)   NOT NULL,
    "nombre" varchar(30)   NOT NULL,
    "ciudad" varchar(30)   NOT NULL,
    "email" varchar(30)   NOT NULL,
    "telefono" varchar(30)   NOT NULL,
    CONSTRAINT "pk_aeropuerto" PRIMARY KEY (
        "idaeropuerto"
     )
);

CREATE TABLE "usuarios" (
    "identificador" varchar(10)   NOT NULL,
    "usuario" varchar(10)   NOT NULL,
    "contrasena" varchar(10)   NOT NULL,
    CONSTRAINT "pk_usuarios" PRIMARY KEY (
        "usuario"
     )
);

CREATE TABLE "soltemp" (
    "codvuelo" varchar(10)   NOT NULL,
    CONSTRAINT "pk_soltemp" PRIMARY KEY (
        "codvuelo"
     )
);

ALTER TABLE "piloto" ADD CONSTRAINT "fk_piloto_aeronit" FOREIGN KEY("aeronit")
REFERENCES "aerolinea" ("aeronit");

ALTER TABLE "copiloto" ADD CONSTRAINT "fk_copiloto_aeronit" FOREIGN KEY("aeronit")
REFERENCES "aerolinea" ("aeronit");

ALTER TABLE "avion" ADD CONSTRAINT "fk_avion_aeronit" FOREIGN KEY("aeronit")
REFERENCES "aerolinea" ("aeronit");

ALTER TABLE "vuelo" ADD CONSTRAINT "fk_vuelo_aeronit" FOREIGN KEY("aeronit")
REFERENCES "aerolinea" ("aeronit");

ALTER TABLE "vuelo" ADD CONSTRAINT "fk_vuelo_pilotoid" FOREIGN KEY("pilotoid")
REFERENCES "piloto" ("pilotoid");

ALTER TABLE "vuelo" ADD CONSTRAINT "fk_vuelo_copilotoid" FOREIGN KEY("copilotoid")
REFERENCES "copiloto" ("copilotoid");

ALTER TABLE "vuelo" ADD CONSTRAINT "fk_vuelo_avionid" FOREIGN KEY("avionid")
REFERENCES "avion" ("avionid");

ALTER TABLE "aerolinea" ADD CONSTRAINT "fk_aerolinea_aeronit" FOREIGN KEY("aeronit")
REFERENCES "usuarios" ("usuario");

ALTER TABLE "aeropuerto" ADD CONSTRAINT "fk_aeropuerto_idaeropuerto" FOREIGN KEY("idaeropuerto")
REFERENCES "usuarios" ("usuario");

ALTER TABLE "soltemp" ADD CONSTRAINT "fk_soltemp_codvuelo" FOREIGN KEY("codvuelo")
REFERENCES "vuelo" ("codvuelo");

