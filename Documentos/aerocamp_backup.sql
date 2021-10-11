--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

-- Started on 2021-10-11 13:00:30

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 204 (class 1259 OID 16669)
-- Name: aerolinea; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aerolinea (
    aeronit character varying(10) NOT NULL,
    nombreaerolinea character varying(30) NOT NULL,
    ciudad character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    telefono character varying(30) NOT NULL
);


ALTER TABLE public.aerolinea OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16679)
-- Name: aeropuerto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aeropuerto (
    idaeropuerto character varying(10) NOT NULL,
    nombre character varying(30) NOT NULL,
    ciudad character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    telefono character varying(30) NOT NULL
);


ALTER TABLE public.aeropuerto OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16659)
-- Name: avion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.avion (
    avionid character varying(10) NOT NULL,
    aeronit character varying(10) NOT NULL,
    modelo character varying(30) NOT NULL,
    tipopropulsion character varying(30) NOT NULL,
    numeromotor character(2) NOT NULL,
    pesonominal character varying(30) NOT NULL,
    capacidad character varying(30) NOT NULL
);


ALTER TABLE public.avion OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16654)
-- Name: copiloto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.copiloto (
    copilotoid character(10) NOT NULL,
    aeronit character varying(10) NOT NULL,
    nombre character varying(30) NOT NULL,
    numerolicencia character varying(10) NOT NULL,
    horasexperiencia character varying(7) NOT NULL,
    revisionmedica date NOT NULL
);


ALTER TABLE public.copiloto OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16674)
-- Name: formtemp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.formtemp (
    aeronit character varying(10) NOT NULL,
    nombreaerolinea character varying(30) NOT NULL,
    ciudad character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    telefono character varying(30) NOT NULL
);


ALTER TABLE public.formtemp OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16649)
-- Name: piloto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.piloto (
    pilotoid character(10) NOT NULL,
    aeronit character varying(10) NOT NULL,
    nombre character varying(30) NOT NULL,
    numerolicencia character varying(10) NOT NULL,
    horasexperiencia character varying(7) NOT NULL,
    revisionmedica date NOT NULL
);


ALTER TABLE public.piloto OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16689)
-- Name: soltemp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.soltemp (
    codvuelo character varying(10) NOT NULL
);


ALTER TABLE public.soltemp OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16684)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    identificador character varying(10) NOT NULL,
    usuario character varying(10) NOT NULL,
    contrasena character varying(10) NOT NULL
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16664)
-- Name: vuelo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vuelo (
    codvuelo character varying(10) NOT NULL,
    aeronit character varying(10) NOT NULL,
    tipovuelo character(1) NOT NULL,
    destino character varying(30) NOT NULL,
    fechasalida date NOT NULL,
    fechallegada date NOT NULL,
    horasalida time without time zone NOT NULL,
    horaentrada time without time zone NOT NULL,
    pilotoid character(10) NOT NULL,
    copilotoid character(10) NOT NULL,
    avionid character varying(10) NOT NULL,
    confirmacionvuelo character(1) NOT NULL
);


ALTER TABLE public.vuelo OWNER TO postgres;

--
-- TOC entry 3042 (class 0 OID 16669)
-- Dependencies: 204
-- Data for Name: aerolinea; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aerolinea (aeronit, nombreaerolinea, ciudad, email, telefono) FROM stdin;
1234	Sat	Pasto	satp@gmail.com	7202020
1234567	Avianca	Bogota	avianca@gmail.com	3223336699
\.


--
-- TOC entry 3044 (class 0 OID 16679)
-- Dependencies: 206
-- Data for Name: aeropuerto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aeropuerto (idaeropuerto, nombre, ciudad, email, telefono) FROM stdin;
1111	AeroCamp	Pasto	aerocamp@gmail.com	7202020
\.


--
-- TOC entry 3040 (class 0 OID 16659)
-- Dependencies: 202
-- Data for Name: avion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.avion (avionid, aeronit, modelo, tipopropulsion, numeromotor, pesonominal, capacidad) FROM stdin;
1234567	1234	airbus300	Reacción	1 	1000	120
\.


--
-- TOC entry 3039 (class 0 OID 16654)
-- Dependencies: 201
-- Data for Name: copiloto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.copiloto (copilotoid, aeronit, nombre, numerolicencia, horasexperiencia, revisionmedica) FROM stdin;
009778    	1234	Fernando Gonzales	8273938202	45	2021-09-01
\.


--
-- TOC entry 3043 (class 0 OID 16674)
-- Dependencies: 205
-- Data for Name: formtemp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.formtemp (aeronit, nombreaerolinea, ciudad, email, telefono) FROM stdin;
\.


--
-- TOC entry 3038 (class 0 OID 16649)
-- Dependencies: 200
-- Data for Name: piloto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.piloto (pilotoid, aeronit, nombre, numerolicencia, horasexperiencia, revisionmedica) FROM stdin;
2356      	1234	Luis Criollo	10972881	48	2021-01-01
\.


--
-- TOC entry 3046 (class 0 OID 16689)
-- Dependencies: 208
-- Data for Name: soltemp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.soltemp (codvuelo) FROM stdin;
\.


--
-- TOC entry 3045 (class 0 OID 16684)
-- Dependencies: 207
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (identificador, usuario, contrasena) FROM stdin;
P	1111	1234
A	1234	0000
A	1234567	1111
\.


--
-- TOC entry 3041 (class 0 OID 16664)
-- Dependencies: 203
-- Data for Name: vuelo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vuelo (codvuelo, aeronit, tipovuelo, destino, fechasalida, fechallegada, horasalida, horaentrada, pilotoid, copilotoid, avionid, confirmacionvuelo) FROM stdin;
0110	1234	0	Bogota	2021-10-25	2021-10-25	06:00:00	08:00:00	2356      	009778    	1234567	0
dsgfdhgfj	1234	1	Pasto	2000-01-01	2000-01-01	00:00:00	00:00:00	2356      	009778    	1234567	1
12312312	1234	0	Bogota	2000-01-01	2000-01-01	00:00:00	00:00:00	2356      	009778    	1234567	0
asdasdasd	1234	0	Seleccionar Lugar	2000-01-01	2000-01-01	00:00:00	00:00:00	2356      	009778    	1234567	1
asdf32	1234	1	Seleccionar Lugar	2000-01-01	2000-01-01	00:00:00	00:00:00	2356      	009778    	1234567	1
\.


--
-- TOC entry 2889 (class 2606 OID 16673)
-- Name: aerolinea pk_aerolinea; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aerolinea
    ADD CONSTRAINT pk_aerolinea PRIMARY KEY (aeronit);


--
-- TOC entry 2893 (class 2606 OID 16683)
-- Name: aeropuerto pk_aeropuerto; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aeropuerto
    ADD CONSTRAINT pk_aeropuerto PRIMARY KEY (idaeropuerto);


--
-- TOC entry 2885 (class 2606 OID 16663)
-- Name: avion pk_avion; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avion
    ADD CONSTRAINT pk_avion PRIMARY KEY (avionid);


--
-- TOC entry 2883 (class 2606 OID 16658)
-- Name: copiloto pk_copiloto; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.copiloto
    ADD CONSTRAINT pk_copiloto PRIMARY KEY (copilotoid);


--
-- TOC entry 2891 (class 2606 OID 16678)
-- Name: formtemp pk_formtemp; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.formtemp
    ADD CONSTRAINT pk_formtemp PRIMARY KEY (aeronit);


--
-- TOC entry 2881 (class 2606 OID 16653)
-- Name: piloto pk_piloto; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.piloto
    ADD CONSTRAINT pk_piloto PRIMARY KEY (pilotoid);


--
-- TOC entry 2897 (class 2606 OID 16693)
-- Name: soltemp pk_soltemp; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.soltemp
    ADD CONSTRAINT pk_soltemp PRIMARY KEY (codvuelo);


--
-- TOC entry 2895 (class 2606 OID 16688)
-- Name: usuarios pk_usuarios; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT pk_usuarios PRIMARY KEY (usuario);


--
-- TOC entry 2887 (class 2606 OID 16668)
-- Name: vuelo pk_vuelo; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vuelo
    ADD CONSTRAINT pk_vuelo PRIMARY KEY (codvuelo);


--
-- TOC entry 2905 (class 2606 OID 16729)
-- Name: aerolinea fk_aerolinea_aeronit; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aerolinea
    ADD CONSTRAINT fk_aerolinea_aeronit FOREIGN KEY (aeronit) REFERENCES public.usuarios(usuario);


--
-- TOC entry 2906 (class 2606 OID 16734)
-- Name: aeropuerto fk_aeropuerto_idaeropuerto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aeropuerto
    ADD CONSTRAINT fk_aeropuerto_idaeropuerto FOREIGN KEY (idaeropuerto) REFERENCES public.usuarios(usuario);


--
-- TOC entry 2900 (class 2606 OID 16704)
-- Name: avion fk_avion_aeronit; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avion
    ADD CONSTRAINT fk_avion_aeronit FOREIGN KEY (aeronit) REFERENCES public.aerolinea(aeronit);


--
-- TOC entry 2899 (class 2606 OID 16699)
-- Name: copiloto fk_copiloto_aeronit; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.copiloto
    ADD CONSTRAINT fk_copiloto_aeronit FOREIGN KEY (aeronit) REFERENCES public.aerolinea(aeronit);


--
-- TOC entry 2898 (class 2606 OID 16694)
-- Name: piloto fk_piloto_aeronit; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.piloto
    ADD CONSTRAINT fk_piloto_aeronit FOREIGN KEY (aeronit) REFERENCES public.aerolinea(aeronit);


--
-- TOC entry 2907 (class 2606 OID 16739)
-- Name: soltemp fk_soltemp_codvuelo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.soltemp
    ADD CONSTRAINT fk_soltemp_codvuelo FOREIGN KEY (codvuelo) REFERENCES public.vuelo(codvuelo);


--
-- TOC entry 2901 (class 2606 OID 16709)
-- Name: vuelo fk_vuelo_aeronit; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vuelo
    ADD CONSTRAINT fk_vuelo_aeronit FOREIGN KEY (aeronit) REFERENCES public.aerolinea(aeronit);


--
-- TOC entry 2904 (class 2606 OID 16724)
-- Name: vuelo fk_vuelo_avionid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vuelo
    ADD CONSTRAINT fk_vuelo_avionid FOREIGN KEY (avionid) REFERENCES public.avion(avionid);


--
-- TOC entry 2903 (class 2606 OID 16719)
-- Name: vuelo fk_vuelo_copilotoid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vuelo
    ADD CONSTRAINT fk_vuelo_copilotoid FOREIGN KEY (copilotoid) REFERENCES public.copiloto(copilotoid);


--
-- TOC entry 2902 (class 2606 OID 16714)
-- Name: vuelo fk_vuelo_pilotoid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vuelo
    ADD CONSTRAINT fk_vuelo_pilotoid FOREIGN KEY (pilotoid) REFERENCES public.piloto(pilotoid);


-- Completed on 2021-10-11 13:00:31

--
-- PostgreSQL database dump complete
--

