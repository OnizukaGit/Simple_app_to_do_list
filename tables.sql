CREATE TABLE to_do_list(
    id serial primary key,
    name varchar(64) not null,
    task varchar(100) not null
);