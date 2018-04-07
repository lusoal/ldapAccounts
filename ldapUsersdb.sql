create database if not exists ldapUsers;

use ldapUsers;

create table if not exists usuarios(
	uid varchar(25) not null primary key,
    nome varchar(30) not null,
    sobrenome varchar(40) not null,
    password varchar(50) not null,
    email varchar(100) not null
);

