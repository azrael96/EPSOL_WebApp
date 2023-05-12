drop database EPSOL_BD;
COMMIT;

CREATE DATABASE EPSOL_BD;
COMMIT;

USE EPSOL_BD;
COMMIT;

CREATE TABLE `clients` (
  `client_ID` int NOT NULL,
  `client_name` varchar(50) NOT NULL,
  `subscription_flag` BOOLEAN NOT NULL,
  `payment_flag` BOOLEAN NOT NULL,
  `client_address` varchar(50) NOT NULL,
  `client_city` varchar(50) NOT NULL,
  `client_state` varchar(50) NOT NULL,
  `client_phone` varchar(11) NOT NULL
);
ALTER TABLE `clients` ADD PRIMARY KEY (`client_ID`);

CREATE TABLE users (
    `user_ID` int NOT NULL,
    `user_name` varchar(50) NOT NULL,
    `user_pass` VARBINARY(72) NOT NULL,
    `user_type` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `user_client` int NOT NULL,
    `nick` varchar(20) NOT NULL
);
ALTER TABLE `users` ADD PRIMARY KEY (`user_ID`);
ALTER TABLE `users` ADD FOREIGN KEY (`user_client`) REFERENCES clients(client_ID);

CREATE TABLE sites (
    `site_ID` int NOT NULL,
    `site_name` varchar(50) NOT NULL,
    `site_location` varchar(50) NOT NULL,
    `site_client` int NOT NULL
);
ALTER TABLE `sites` ADD PRIMARY KEY (`site_ID`);
ALTER TABLE `sites` ADD FOREIGN KEY (`site_client`) REFERENCES clients(client_ID);

CREATE TABLE analizers (
    `analizer_ID` int NOT NULL,
    `manufacturer_name` varchar(50) NOT NULL,
    `usage_flag` BOOLEAN NOT NULL,
    `class_name` varchar(50) NOT NULL
);
ALTER TABLE `analizers` ADD PRIMARY KEY (`analizer_ID`);

CREATE TABLE mesTables (
    `meas_ID` int NOT NULL,
    `meas_site` int NOT NULL,
    `meas_analizer` int NOT NULL
);
ALTER TABLE `mesTables` ADD PRIMARY KEY (`meas_ID`);
ALTER TABLE `mesTables` ADD FOREIGN KEY (`meas_site`) REFERENCES sites(site_ID);
ALTER TABLE `mesTables` ADD FOREIGN KEY (`meas_analizer`) REFERENCES analizers(analizer_ID);

CREATE TABLE measurements ( 
    `timestamp` int NOT NULL,
    `powerFactor` DECIMAL(10, 9) NOT NULL,
    `thd` DECIMAL(10, 9) NOT NULL, /* theres more to add*/
    `measure_meas` int NOT NULL
);
ALTER TABLE `measurements` ADD PRIMARY KEY (`timestamp`);
ALTER TABLE `measurements` ADD FOREIGN KEY (`measure_meas`) REFERENCES mesTables(meas_ID);

COMMIT;

INSERT INTO clients VALUES (100000, 'EPSOL', 1, 1, 'dir', 'ciudad', 'estado', 'tel');
INSERT INTO users VALUES (200000, 'ADMIN_EPSOL', '$2b$12$kjPPb2N/VrrZmQtz461SjOjJAZnzwhQIr2P7N6GP8OV5eIM9QZeXu', 'Admin', 'email@', 100000, 'nick');

COMMIT;