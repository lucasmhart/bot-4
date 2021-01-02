CREATE DATABASE bot;

USE bot;

CREATE TABLE trf4_numbers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    code_number INT NOT NULL,
    prefix VARCHAR(10),
    origin VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE trf4_processed(
    id INT PRIMARY KEY AUTO_INCREMENT,
    code_number INT NOT NULL,
    originario VARCHAR(255),
    data_autuacao VARCHAR(255),
    relator VARCHAR(255),
    orgao_julgador VARCHAR(255),
    orgao_atual VARCHAR(255),
    situacao VARCHAR(255),
    competencia VARCHAR(255),
    requerente VARCHAR(255),
    advogado_1 VARCHAR(255),
    advogado_2 VARCHAR(255),
    requerido VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);