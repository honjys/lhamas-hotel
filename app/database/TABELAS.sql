CREATE TABLE funcionario(
	cpf VARCHAR(15) NOT NULL,
	nome VARCHAR(250) NOT NULL,
	email VARCHAR(250) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	senha VARCHAR(51) NOT NULL,
	PRIMARY KEY (cpf));

insert into funcionario(cpf,nome,email,telefone,senha) values ('1111','janailson','janailsonsoares@','989182983','wheyprotein');
insert into funcionario(cpf,nome,email, telefone,senha) values ('7788', 'micheal jackson','reidopop@','666999666','biliejean');
insert into funcionario(cpf, nome, email, telefone, senha) values ('123','salami','salada@','28022017','123');

CREATE TABLE cliente(
	cpf VARCHAR(15) NOT NULL,
	nome VARCHAR(250) NOT NULL,
	email VARCHAR(250) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	PRIMARY KEY (cpf));


insert into cliente(cpf, nome, email, telefone) values ('12332','irineu','vocenasabe@','40028922');
insert into cliente(cpf, nome, email, telefone) values ('987789', 'bon scott', 'shotgirls@', '689843');


CREATe Table admin(
	cpf varchar(15) not null,
	nome varchar(67) not null,
	email varchar(200) not null,
	telefone varchar(20) not null,
	senha varchar(80) not null,
	primary key (cpf));
insert into admin(cpf, nome, email, telefone, senha) values ('1','João Victor','tearsofthedragon@','87688768','123');
insert into admin(cpf, nome, email, telefone, senha) values ('2','Isaque', 'Lovehurts@','22333446','1234');

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
	cpf_cliente VARCHAR(15),
	numero_quarto varchar(6) not null,
	alugado_em date not null,
	alugado_ate date not null,
	primary key (numero_quarto),
	foreign key (cpf_cliente) references cliente(cpf),
	foreign key (numero_quarto) references quartos(numero));
insert into alugados(cpf_cliente,numero_quarto,alugado_em,alugado_ate) values ('12332','2','2019-04-01','2019-04-02');
insert into alugados(cpf_cliente,numero_quarto,alugado_em,alugado_ate) values ('987789', '7','2019-04-01','2019-04-04'); 