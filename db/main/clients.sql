create table clients
(
    id                 INTEGER
        primary key autoincrement,
    nom                TEXT not null,
    email              TEXT not null
        unique,
    telephone          TEXT,
    prenom             TEXT,
    adresse            TEXT,
    code_postal        integer,
    ville              TEXT,
    adresse_complement TEXT
);

