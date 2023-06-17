CREATE TABLE IF NOT EXISTS USUARIO(
    id_usuario VARCHAR(10) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    apellido VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    rol VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_usuario)
);

ALTER TABLE USUARIO ALTER COLUMN email VARCHAR(50) NOT NULL UNIQUE;
INSERT INTO USUARIO (id_usuario, nombre, apellido, email, password, rol) VALUES ('marcalexan', 'Marc Alexander', 'Vasquez', 'marcalexander@mail.com', 'marc123', 'residente'), ('octaviowey', 'Octavio', 'Flores', 'octy@mail.com', 'octy123', 'supervisor');
