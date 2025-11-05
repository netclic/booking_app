create table logements
(
    id          INTEGER
        primary key autoincrement,
    nom         TEXT,
    adresse     TEXT,
    code_postal TEXT,
    ville       TEXT,
    capacite    INTEGER,
    classement  integer
);

