
CREATE DATABASE IF NOT EXISTS `facerecognition`;
DROP TABLE IF EXISTS `Account`;
DROP TABLE IF EXISTS `Login_`;
DROP TABLE IF EXISTS `SavingAccount`;
DROP TABLE IF EXISTS `CurrentHKDAccount`;
DROP TABLE IF EXISTS `CurrentUSDAccount`;
DROP TABLE IF EXISTS `Customer`;
DROP TABLE IF EXISTS `Identification`;
DROP TABLE IF EXISTS `Transaction_`;
DROP TABLE IF EXISTS `Withdrawal`;
DROP TABLE IF EXISTS `Deposit`;
DROP TABLE IF EXISTS `Transfer_`;

CREATE TABLE Customer (
  customer_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  password_ BINARY(40) NOT NULL,
  date_of_birth DATE NOT NULL,
	address VARCHAR(100) NOT NULL,
	phone_number VARCHAR(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Account (
  account_number VARCHAR(20) PRIMARY KEY NOT NULL,
  customer_id INT NOT NULL,
  balance INT NOT NULL,
  date_opened DATE NOT NULL,
  last_access DATETIME NOT NULL,
  min_balance FLOAT NOT NULL,
  account_status VARCHAR(20) NOT NULL,
  account_type VARCHAR(20) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE SavingAccount (
  account_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  account_number VARCHAR(20),
  interest_rate FLOAT NOT NULL,
  FOREIGN KEY (account_number) REFERENCES Account(account_number)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE CurrentAccount (
  account_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  account_number VARCHAR(20),
  overdraft FLOAT NOT NULL,
  FOREIGN KEY (account_number) REFERENCES Account(account_number)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Login_(
  login_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  customer_id INT NOT NULL,
  login_time DATETIME NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Identification (
  identification_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  customer_id INT NOT NULL,
  upload_time DATETIME NOT NULL,
  address_proof blob,
  identification_document blob,
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#Create TABLE Transaction_
CREATE TABLE Transaction_(
  transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  account_number VARCHAR(20) NOT NULL,
  transaction_time DATETIME NOT NULL,
  transaction_amount FLOAT NOT NULL,
	transaction_type VARCHAR(20),
  transaction_description VARCHAR(2000),
	FOREIGN KEY (account_number) REFERENCES Account(account_number)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Withdrawal (
  transaction_id INT NOT NULL PRIMARY KEY,
  FOREIGN KEY (transaction_id) REFERENCES Transaction_(transaction_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Deposit (
  transaction_id INT NOT NULL PRIMARY KEY,
  FOREIGN KEY (transaction_id) REFERENCES Transaction_(transaction_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Transfer_ (
  transaction_id INT NOT NULL PRIMARY KEY,
  FOREIGN KEY (transaction_id) REFERENCES Transaction_(transaction_id),
  to_account VARCHAR(20)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (1,'Ping','Luo','pluo@cs.hku.hk', SHA1('qwer1234'), '1990-05-16', 'Sai Ying Pun', '93728104');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (2,'Jiannan','Wu','wjn922@connect.hku.hk', SHA1('thisisbadpasswd'), '1994-11-25', 'Central', '93040210');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (3,'Sukmin','Kim','skim@connect.hku.hk', SHA1('abcdefg'), '1999-02-26', 'Tsuen Mun', '70732912');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (4,'Ayoung','Kwon','akwon@connect.hku.hk', SHA1('akak1116'), '1997-11-16', 'Kennedy Town', '50920421');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (5,'Pranay','Periwal','pperiwal@connect.hku.hk', SHA1('comp3278'), '1999-06-17', 'North Point', '53928415');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (6,'Anishka','Bhargava','abhargava@connect.hku.hk', SHA1('database'), '1999-05-22', 'Jordan', '98392014');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (7,'Julie','Park','jpark@connect.hku.hk', SHA1('passwdpasswd'), '2000-12-04', 'Sai Kung', '58399204');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (8,'Yao','Mu','muyao@connect.hku.hk', SHA1('rootyaomu'), '1992-07-02', 'Lamma Island', '70721850');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (9,'Schnieders','Dirk','sdirk@connect.hku.hk', SHA1('hashmypasswd'), '1989-04-12', 'Cyberport', '70767421');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (10,'HeungMin','Son','spurs@gmail.com', SHA1('pwow0212r'), '1988-06-14', 'Wood Green', '98302915');
INSERT INTO Customer (customer_id, first_name, last_name, email, password_, date_of_birth, address, phone_number) VALUES (11,'Sundar','Pichai','alphabet@gmail.com', SHA1('123123g'), '1975-03-16', 'Silicon Valley', '56565555');

INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-00700', 1, 1225321.5, '2020-10-01', '2021-10-10 23:18:24', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-00800', 2, 86892.5, '2020-12-02', '2021-10-03 21:17:59', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-00900', 3, 626892.5, '2020-12-17', '2021-11-03 19:00:19', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01000', 4, 21425.4, '2021-01-04', '2021-11-05 12:25:21', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01100', 5, 9920452.1, '2021-01-12', '2021-10-16 21:16:59', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01200', 6, 3028592.0, '2021-02-25', '2021-09-09 04:15:14', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01300', 7, 142956.4, '2021-02-28', '2021-08-21 07:01:41', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01400', 8, 124.5, '2021-04-11', '2021-11-03 09:12:42', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01500', 9, 2400.7, '2021-05-26', '2021-11-06 15:51:15', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01600', 10, 364.0, '2021-05-27', '2021-10-30 14:20:52', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01700', 11, 15.6, '2021-06-01', '2021-10-22 17:24:11', 1000, 1, 'Savings');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-00711', 1, 62522.1, '2020-10-01', '2021-10-10 23:18:24', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-00811', 2, 5728.5, '2020-12-02', '2021-10-03 21:17:59', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-00911', 3, 263632.7, '2020-12-17', '2021-11-03 19:00:19', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01011', 4, 1245.4, '2021-01-04', '2021-11-05 12:25:21', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01111', 5, 12923.0, '2021-01-12', '2021-10-16 21:16:59', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01211', 6, 4643613.2, '2021-02-25', '2021-09-09 04:15:24', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01311', 7, 3200.1, '2021-02-28', '2021-08-21 07:01:41', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01411', 8, 89.4, '2021-04-11', '2021-11-03 09:12:42', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01511', 9, 126.1, '2021-05-26', '2021-11-06 15:51:15', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01611', 10, 14.5, '2021-05-27', '2021-10-30 14:20:52', 1000, 1, 'Current');
INSERT INTO Account (account_number, customer_id, balance, date_opened, last_access, min_balance, account_status, account_type) VALUES ('00800-01711', 11, 8.1, '2021-06-01', '2021-10-22 17:24:11', 1000, 1, 'Current');


INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-00700', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-00800', 0.05);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-00900', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01000', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01100', 0.05);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01200', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01300', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01400', 0.05);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01500', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01600', 0.04);
INSERT INTO SavingAccount (account_number, interest_rate) VALUES ('00800-01700', 0.05);

INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-00711', 750.4);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-00811', 980.2);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-00911', 94.1);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01011', 722.0);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01111', 245.7);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01211', 125.4);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01311', 45.5);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01411', 27.0);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01511', 25.1);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01611', 920.1);
INSERT INTO CurrentAccount (account_number, overdraft) VALUES ('00800-01711', 177.2);


INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2020-11-13 14:31:40');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-02-10 10:31:46');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-02-26 06:17:58');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-03-09 23:52:56');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-04-14 14:38:00');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-06-15 10:37:55');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-06-17 19:08:01');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-06-18 14:06:52');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-07-18 12:12:48');
INSERT INTO Login_ (customer_id, login_time) VALUES (1, '2021-10-18 12:02:17');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2020-12-16 05:27:03');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2020-12-21 12:20:29');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2021-01-23 05:45:59');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2021-01-31 06:32:48');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2021-05-19 13:03:01');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2021-06-01 06:40:45');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2021-08-31 18:52:11');
INSERT INTO Login_ (customer_id, login_time) VALUES (2, '2021-10-06 12:21:53');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2020-12-28 10:54:35');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-01-10 17:35:00');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-03-01 07:43:05');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-03-28 07:56:05');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-04-04 20:51:16');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-06-27 11:50:14');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-09-06 05:59:06');
INSERT INTO Login_ (customer_id, login_time) VALUES (3, '2021-09-16 03:00:49');
INSERT INTO Login_ (customer_id, login_time) VALUES (4, '2021-02-20 23:55:49');
INSERT INTO Login_ (customer_id, login_time) VALUES (4, '2021-03-04 16:34:52');
INSERT INTO Login_ (customer_id, login_time) VALUES (4, '2021-06-03 02:03:34');
INSERT INTO Login_ (customer_id, login_time) VALUES (4, '2021-06-06 21:07:31');
INSERT INTO Login_ (customer_id, login_time) VALUES (4, '2021-07-18 21:48:43');
INSERT INTO Login_ (customer_id, login_time) VALUES (4, '2021-09-07 21:18:28');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-09-24 05:25:52');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-10-01 21:21:15');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-10-02 23:21:43');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-10-03 04:21:23');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-10-04 01:21:11');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-10-05 14:21:05');
INSERT INTO Login_ (customer_id, login_time) VALUES (5, '2021-10-06 12:21:53');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-03-01 22:24:18');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-03-13 11:06:15');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-03-14 16:49:11');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-03-30 22:47:30');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-05-30 03:29:04');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-06-02 10:00:27');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-07-03 12:34:45');
INSERT INTO Login_ (customer_id, login_time) VALUES (6, '2021-08-14 03:44:34');
INSERT INTO Login_ (customer_id, login_time) VALUES (7, '2021-03-17 05:56:49');
INSERT INTO Login_ (customer_id, login_time) VALUES (7, '2021-04-14 20:22:07');
INSERT INTO Login_ (customer_id, login_time) VALUES (7, '2021-04-29 15:29:13');
INSERT INTO Login_ (customer_id, login_time) VALUES (7, '2021-05-24 19:45:38');
INSERT INTO Login_ (customer_id, login_time) VALUES (7, '2021-07-02 22:00:46');
INSERT INTO Login_ (customer_id, login_time) VALUES (7, '2021-09-04 08:03:23');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-04-19 15:43:19');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-05-19 18:22:05');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-06-11 16:41:00');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-06-24 14:10:46');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-07-03 15:25:58');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-07-18 03:39:59');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-08-03 07:52:35');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-08-06 04:59:07');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-09-16 18:48:56');
INSERT INTO Login_ (customer_id, login_time) VALUES (8, '2021-10-20 08:02:25');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-06-01 18:52:02');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-06-09 21:28:16');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-07-02 04:46:13');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-07-11 05:48:03');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-07-22 23:24:20');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-09-12 12:53:56');
INSERT INTO Login_ (customer_id, login_time) VALUES (9, '2021-09-14 03:38:18');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-06-26 15:19:00');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-07-23 07:51:30');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-07-31 21:41:55');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-08-06 04:52:25');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-08-24 10:53:57');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-09-02 02:58:14');
INSERT INTO Login_ (customer_id, login_time) VALUES (10, '2021-09-11 10:04:19');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-07-07 18:54:28');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-07-14 02:13:23');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-07-15 15:21:59');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-07-26 07:14:20');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-08-26 14:55:35');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-09-03 11:18:01');
INSERT INTO Login_ (customer_id, login_time) VALUES (11, '2021-09-11 14:22:56');


INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (1, 1, '2020-10-01 13:18:24', LOAD_FILE('address_proof1.png'), LOAD_FILE('passport1.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (2, 2, '2020-12-02 18:28:16', LOAD_FILE('address_proof2.png'), LOAD_FILE('HKID1.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (3, 3, '2020-12-17 11:01:01', LOAD_FILE('address_proof3.png'), LOAD_FILE('HKID2.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (4, 4, '2021-01-04 05:06:17', LOAD_FILE('address_proof4.png'), LOAD_FILE('passport2.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (5, 5, '2021-01-12 04:56:52', LOAD_FILE('address_proof5.png'), LOAD_FILE('HKID3.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (6, 6, '2021-02-25 15:56:15', LOAD_FILE('address_proof6.png'), LOAD_FILE('HKID4.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (7, 7, '2021-02-28 17:12:04', LOAD_FILE('address_proof7.png'), LOAD_FILE('HKID5.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (8, 8, '2021-04-11 03:00:42', LOAD_FILE('address_proof8.png'), LOAD_FILE('passport3.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (9, 9, '2021-05-26 07:32:51', LOAD_FILE('address_proof9.png'), LOAD_FILE('HKID6.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (10, 10, '2021-05-27 11:17:16', LOAD_FILE('address_proof10.png'), LOAD_FILE('passport4.png'));
INSERT INTO Identification (identification_id, customer_id, upload_time, address_proof, identification_document) VALUES (11, 11, '2021-06-01 01:58:39', LOAD_FILE('address_proof11.png'), LOAD_FILE('passport5.png'));

INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (1, '00800-00700', '2021-10-12 15:34:58', 30.00, 'withdraw', 'withdraw 30HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (2, '00800-00900', '2021-10-14 04:02:46', 30.00, 'deposit', 'deposit 30HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (3, '00800-01200', '2021-10-15 08:56:02', 30.00, 'transfer', 'transfer 30HKD to 00800-00900');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (4, '00800-00700', '2021-10-15 13:53:38', 40.00, 'withdraw', 'withdraw 40HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (5, '00800-01700', '2021-10-15 17:01:29', 40.00, 'deposit', 'deposit 40HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (6, '00800-00900', '2021-10-16 00:02:03', 30.52, 'transfer', 'transfer 30HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (7, '00800-01200', '2021-10-16 02:09:46', 20.00, 'withdraw', 'withdraw 20HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (8, '00800-00700', '2021-10-16 17:56:07', 15.00, 'deposit', 'deposit 15HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (9, '00800-00900', '2021-10-17 02:23:42', 22.10, 'transfer', 'transfer 22.10HKD to 00800-00800');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (10, '00800-00900', '2021-10-17 02:39:31', 70.00, 'transfer', 'transfer 70HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (11, '00800-00700', '2021-10-17 04:32:08', 40.00, 'deposit', 'deposit 40HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (12, '00800-01200', '2021-10-17 10:33:10', 22.00, 'withdraw', 'withdraw 22HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (13, '00800-00900', '2021-10-17 23:34:17', 100.00, 'transfer', 'transfer 100HKD to 00800-01200');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (14, '00800-01400', '2021-10-18 08:05:16', 300.00, 'withdraw', 'withdraw 300HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (15, '00800-00700', '2021-10-18 23:30:51', 260.00, 'deposit', 'deposit 260HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (16, '00800-01000', '2021-10-20 11:13:01', 120.00, 'transfer', 'transfer 120HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (17, '00800-00800', '2021-10-20 20:24:33', 49.00, 'withdraw', 'withdraw 40HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (18, '00800-00900', '2021-10-21 00:55:52', 200.00, 'transfer', 'transfer 200HKD to 00800-01000');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (19, '00800-00900', '2021-10-21 18:30:07', 25.50, 'deposit', 'deposit 25.5HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (20, '00800-00900', '2021-10-22 14:43:00', 150.00, 'transfer', 'transfer 150HKD to 00800-01500');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (21, '00800-00700', '2021-10-23 14:18:32', 7.10, 'withdraw', 'withdraw 7.1HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (22, '00800-00900', '2021-10-23 23:49:57', 212.50, 'transfer', 'transfer 212.5HKD to 00800-01200');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (23, '00800-01200', '2021-10-24 06:26:20', 200.00, 'deposit', 'deposit 200HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (24, '00800-01600', '2021-10-25 07:38:07', 245.16, 'transfer', 'transfer 245.16HKD to 00800-00800');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (25, '00800-01400', '2021-10-27 02:50:55', 600.00, 'deposit', 'deposit 600HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (26, '00800-00700', '2021-10-27 15:32:32', 200.00, 'withdraw', 'withdraw 200HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (27, '00800-00911', '2021-10-27 18:27:16', 15.00, 'transfer', 'transfer 15HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (28, '00800-00911', '2021-10-28 03:04:04', 300.00, 'withdraw', 'withdraw 300HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (29, '00800-00900', '2021-10-28 03:16:05', 166.66, 'transfer', 'transfer 166.66HKD to 00800-01100');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (30, '00800-01000', '2021-10-28 21:11:08', 700.00, 'deposit', 'deposit 700HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (31, '00800-00900', '2021-10-29 01:19:59', 1000.00, 'transfer', 'transfer 1000HKD to 00800-01200');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (32, '00800-00800', '2021-10-29 17:26:30', 1000.00, 'withdraw', 'withdraw 1000HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (33, '00800-00900', '2021-10-29 23:13:04', 600.00, 'transfer', 'transfer 600HKD to 00800-01300');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (34, '00800-00700', '2021-11-02 01:33:29', 100.00, 'deposit', 'deposit 100HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (35, '00800-00711', '2021-11-02 20:57:23', 70.50, 'transfer', 'transfer 70.5HKD to 00800-01400');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (36, '00800-00711', '2021-11-03 14:17:30', 250.00, 'withdraw', 'withdraw 20HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (37, '00800-00900', '2021-11-04 06:14:20', 30.00, 'transfer', 'transfer 30HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (38, '00800-01700', '2021-11-04 18:59:13', 600.00, 'withdraw', 'withdraw 600HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (39, '00800-00900', '2021-11-04 21:12:15', 120.00, 'transfer', 'transfer 120HKD to 00800-01100');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (40, '00800-01600', '2021-11-05 03:21:12', 150.00, 'transfer', 'transfer 150HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (41, '00800-00900', '2021-11-05 04:06:08', 180.00, 'transfer', 'transfer 180HKD to 00800-01500');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (42, '00800-01700', '2021-11-05 10:08:36', 400.00, 'deposit', 'deposit 400HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (43, '00800-00800', '2021-11-06 11:59:17', 100.00, 'withdraw', 'withdraw 100HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (44, '00800-00700', '2021-11-07 00:16:39', 100.00, 'withdraw', 'withdraw 1000HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (45, '00800-00700', '2021-11-08 07:28:59', 2000.00, 'deposit', 'deposit 2000HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (46, '00800-00900', '2021-11-09 07:45:00', 250.0, 'transfer', 'transfer 250HKD to 00800-01000');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (47, '00800-01000', '2021-11-10 08:41:13', 100.00, 'withdraw', 'withdraw 100HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (48, '00800-01100', '2021-11-11 08:26:45', 200.00, 'deposit', 'deposit 200HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (49, '00800-00711', '2021-11-11 10:29:47', 200.00, 'deposit', 'deposit 200HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (50, '00800-01400', '2021-11-11 13:04:19', 30.00, 'transfer', 'transfer 30HKD to 00800-00800');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (51, '00800-01300', '2021-11-11 18:18:49', 500.00, 'withdraw', 'withdraw 500HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (52, '00800-01300', '2021-11-11 18:48:57', 30.00, 'transfer', 'transfer 30HKD to 00800-00900');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (53, '00800-00711', '2021-11-12 00:14:02', 40.00, 'transfer', 'transfer 40HKD to 00800-00800');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (54, '00800-01300', '2021-11-12 03:44:59', 50.00, 'transfer', 'transfer 50HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (55, '00800-01100', '2021-11-13 12:57:40', 60.00, 'transfer', 'transfer 60HKD to 00800-00700');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (56, '00800-01200', '2021-11-14 03:49:33', 7000.00, 'deposit', 'deposit 7000HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (57, '00800-01700', '2021-11-14 08:45:55', 800.00, 'withdraw', 'withdraw 800HKD');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (58, '00800-01400', '2021-11-14 23:00:44', 500.00, 'transfer', 'transfer 500HKD to 00800-00900');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (59, '00800-00700', '2021-11-15 00:09:11', 250.50, 'transfer', 'transfer 250.5HKD to 00800-01500');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (60, '00800-01500', '2021-11-16 13:30:58', 400.40, 'transfer', 'transfer 400.4HKD to 00800-01200');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (61, '00800-01200', '2021-11-16 20:16:30', 15.50, 'transfer', 'transfer 15.5HKD to 00800-01300');
INSERT INTO Transaction_ (transaction_id, account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES (62, '00800-01100', '2021-11-16 20:47:22', 14.60, 'transfer', 'transfer 14.6HKD to 00800-01400');


INSERT INTO Withdrawal (transaction_id) VALUES (1);
INSERT INTO Withdrawal (transaction_id) VALUES (4);
INSERT INTO Withdrawal (transaction_id) VALUES (7);
INSERT INTO Withdrawal (transaction_id) VALUES (12);
INSERT INTO Withdrawal (transaction_id) VALUES (14);
INSERT INTO Withdrawal (transaction_id) VALUES (17);
INSERT INTO Withdrawal (transaction_id) VALUES (21);
INSERT INTO Withdrawal (transaction_id) VALUES (26);
INSERT INTO Withdrawal (transaction_id) VALUES (28);
INSERT INTO Withdrawal (transaction_id) VALUES (32);
INSERT INTO Withdrawal (transaction_id) VALUES (36);
INSERT INTO Withdrawal (transaction_id) VALUES (38);
INSERT INTO Withdrawal (transaction_id) VALUES (43);
INSERT INTO Withdrawal (transaction_id) VALUES (44);
INSERT INTO Withdrawal (transaction_id) VALUES (47);
INSERT INTO Withdrawal (transaction_id) VALUES (49);
INSERT INTO Withdrawal (transaction_id) VALUES (57);

INSERT INTO Deposit (transaction_id) VALUES (2);
INSERT INTO Deposit (transaction_id) VALUES (5);
INSERT INTO Deposit (transaction_id) VALUES (8);
INSERT INTO Deposit (transaction_id) VALUES (15);
INSERT INTO Deposit (transaction_id) VALUES (19);
INSERT INTO Deposit (transaction_id) VALUES (23);
INSERT INTO Deposit (transaction_id) VALUES (25);
INSERT INTO Deposit (transaction_id) VALUES (30);
INSERT INTO Deposit (transaction_id) VALUES (34);
INSERT INTO Deposit (transaction_id) VALUES (42);
INSERT INTO Deposit (transaction_id) VALUES (45);
INSERT INTO Deposit (transaction_id) VALUES (48);
INSERT INTO Deposit (transaction_id) VALUES (51);
INSERT INTO Deposit (transaction_id) VALUES (56);

INSERT INTO Transfer_ (transaction_id, to_account) VALUES (3, '00800-00900');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (6, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (9, '00800-00800');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (10, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (13, '00800-01200');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (16, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (18, '00800-01000');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (20, '00800-01500');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (22, '00800-01200');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (24, '00800-00800');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (27, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (29, '00800-01100');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (31, '00800-01200');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (33, '00800-01300');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (35, '00800-01400');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (37, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (39, '00800-01100');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (40, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (41, '00800-01500');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (46, '00800-01000');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (50, '00800-00800');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (52, '00800-00900');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (53, '00800-00800');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (54, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (55, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (58, '00800-00900');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (59, '00800-00700');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (60, '00800-01200');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (61, '00800-01300');
INSERT INTO Transfer_ (transaction_id, to_account) VALUES (62, '00800-01400');