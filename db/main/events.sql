create table events
(
    id             INTEGER
        primary key autoincrement,
    client_id      INTEGER not null
        references clients
            on delete cascade,
    logement_id    INTEGER not null
        references logements
            on delete cascade,
    status         TEXT,
    date_debut     TEXT    not null,
    date_fin       TEXT,
    description    TEXT,
    nombre_adultes integer,
    nombre_enfants integer,
    type           TEXT,
    constraint check_status
        check (status IN ('Demande', 'En attente', 'Confirmée', 'Annulée')),
    constraint check_type
        check (type IN ('Fermeture', 'Réservation'))
);

create index idx_events_client
    on events (client_id);

create index idx_events_logement
    on events (logement_id);

