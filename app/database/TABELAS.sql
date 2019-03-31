CREATE TABLE funcionario(
	cpf VARCHAR(15) NOT NULL,
	nome VARCHAR(250) NOT NULL,
	email VARCHAR(250) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	senha VARCHAR(51) NOT NULL,
	PRIMARY KEY (cpf));

CREATE TABLE cliente(
	cpf VARCHAR(15) NOT NULL,
	nome VARCHAR(250) NOT NULL,
	email VARCHAR(250) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	PRIMARY KEY (cpf));

CREATe Table admin(cpf varchar(15) not null,
	nome varchar(67) not null,
	endereço varchar(200) not null,
	email varchar(200) not null,
	telefone varchar(20) not null,
	primary key (cpf));

create table quartos(
	numero varchar(3) not null,
	metros2 varchar(6) not null,
	aluguel_dia float not null,
	status varchar(20) not null,
	primary key (numero));


insert into quartos(numero,metros2,aluguel_dia, status) values ('1','120','400', 'vago');
insert into quartos(numero,metros2,aluguel_dia, status) values ('2','200','600', 'alugado');
insert into quartos(numero,metros2,aluguel_dia, status) values ('3','70','180', 'indisponivel');
insert into quartos(numero,metros2,aluguel_dia, status) values ('4','200','600', 'vago');
insert into quartos(numero,metros2,aluguel_dia, status) values ('5','170','450', 'vago');
insert into quartos(numero,metros2,aluguel_dia, status) values ('6','120','400', 'vago');
insert into quartos(numero,metros2,aluguel_dia, status) values ('7','120','400', 'alugado');


create table alugados(
	cpf_funcio VARCHAR(15) NOT NULL,
	numero_quarto varchar(6) not null,
	alugado_em date not null,
	alugado_ate date not null,
	primary key (numero_quarto),
	foreign key (cpf_funcio) references funcionario(cpf),
	foreign key (numero_quarto) references quartos(numero));