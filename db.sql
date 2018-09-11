CREATE DATABASE IF NOT EXISTS `melico`;

CREATE TABLE IF NOT EXISTS `melico`.`request` (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    url varchar(255) NOT NULL UNIQUE,
    user varchar(255),
    pass varchar(255),
    email varchar(255) NOT NULL UNIQUE,
    date_registration TIMESTAMP
);