CREATE TABLE societa (
    id VARCHAR(5) NOT NULL,
    nome VARCHAR(255),
    link VARCHAR(255),
    PRIMARY KEY (id)
);

-- Crea la tabella 'atleta'
CREATE TABLE atleta (
    id INT AUTO_INCREMENT,
    nome VARCHAR(255),
    cognome VARCHAR(255),
    data_nascita DATE,
    PRIMARY KEY (id)
);

-- Crea la tabella 'storico'
CREATE TABLE storico (
    id INT AUTO_INCREMENT,
    anno INT,
    categoria VARCHAR(255),
    id_societa VARCHAR(5),
    id_atleta INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_societa) REFERENCES societa(id),
    FOREIGN KEY (id_atleta) REFERENCES atleta(id)
);

-- Crea la tabella 'disciplina'
CREATE TABLE disciplina (
    id INT AUTO_INCREMENT,
    disciplina VARCHAR(255),
    PRIMARY KEY (id)
);

-- Crea la tabella 'prestazione'
CREATE TABLE prestazione (
    id INT AUTO_INCREMENT,
    data DATE,
    luogo VARCHAR(255),
    disciplina_id INT,
    risultato DECIMAL(10, 2),
    vento DECIMAL(5, 2),
    storico_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplina(id),
    FOREIGN KEY (storico_id) REFERENCES storico(id)
);