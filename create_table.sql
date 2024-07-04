CREATE DATABASE IF NOT EXISTS db;

USE db;

CREATE TABLE IF NOT EXISTS `vagas` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `idade` int,
  `cidade` varchar(255)
);

INSERT INTO vagas (nome, idade, cidade)
VALUES ('João', 30, 'São Paulo'),
       ('Maria', 25, 'Rio de Janeiro'),
       ('Carlos', 35, 'Belo Horizonte');