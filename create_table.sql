CREATE DATABASE IF NOT EXISTS db;

USE db;

CREATE TABLE IF NOT EXISTS `vagas` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `idade` int,
  `cidade` varchar(255)
);