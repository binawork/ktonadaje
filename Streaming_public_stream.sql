create table stream
(
    id               serial        not null
        constraint stream_pk
            primary key,
    type_of_activity varchar(100)  not null,
    title            varchar(60)   not null,
    last_name        varchar(30)   not null,
    first_name       varchar(30)   not null,
    beginning        timestamp     not null,
    finish            timestamp     not null,
    your_description      varchar(1000) not null,
    link_to                varchar(100)  not null
);

alter table stream
    owner to maciej;

create unique index stream_id_uindex
    on stream (id);

