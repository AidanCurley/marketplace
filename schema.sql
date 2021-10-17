SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS storefront;
DROP TABLE IF EXISTS catalogue;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS paypal;

CREATE TABLE card(
  number CHAR(16) PRIMARY KEY NOT NULL,
  sort_code CHAR(6) NOT NULL,
  type VARCHAR(16) NOT NULL,
  expiry_date DATE NOT NULL,
  cvv CHAR(3) NOT NULL
);

CREATE TABLE paypal(
  number CHAR(4) PRIMARY KEY,
  balance FLOAT(6,2)
);

CREATE TABLE customer (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR (20) UNIQUE NOT NULL,
  password CHAR(6) NOT NULL,
  f_name VARCHAR(30) NOT NULL,
  surname VARCHAR(30) NOT NULL,
  address VARCHAR(50) NOT NULL,
  email VARCHAR(20) NOT NULL,
  phone CHAR(11),
  card_number CHAR(16),
  paypal_number CHAR(4),
  FOREIGN KEY (card_number) REFERENCES card(number),
  FOREIGN KEY (paypal_number) REFERENCES paypal(number)
);

CREATE TABLE product(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(20),
  stock_count INT
);

CREATE TABLE storefront (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  logo VARCHAR (30) NOT NULL
);

CREATE TABLE catalogue(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  product_id INT,
  seller_id INT,
  price FLOAT(6,2),
  FOREIGN KEY (product_id) REFERENCES product(id),
  FOREIGN KEY (seller_id) REFERENCES seller(id)
);

CREATE TABLE seller (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR (20) UNIQUE NOT NULL,
  password CHAR(6) NOT NULL,
  f_name VARCHAR(30) NOT NULL,
  surname VARCHAR(30) NOT NULL,
  address VARCHAR(50) NOT NULL,
  email VARCHAR(20) NOT NULL,
  phone CHAR(11),
  storefront_id INTEGER NOT NULL
);


INSERT INTO `customer` VALUES (1,'cust1','123456','John','Johnson','1 Carr St., Leeds, UK','john@hotmail.com','07912312312','1234123412341234','1111'),
  (2,'cust2','123456','James','Jameson','2 Spitfire St., Leeds, UK','james@hotmail.com','07912312312','5678567856785678','2222'),
  (3,'cust3','123456','Mike','Mitchell','22 Slatchett Row, Liverpool, UK','mike@hotmail.com','07999999999','1000100010001000','2222');
INSERT INTO `seller` VALUES (1,'sell1','123456','Billy','Bobson','12 Comercial St., London, UK','bb@hotmail.com','07912312312',1),
  (2,'sell2','123456','Sarah','Smith','12 Spartan Ave., London, UK','sarah@hotmail.com','07912312312',2);
INSERT INTO `storefront` VALUES (1,'logo1'),
  (2,'logo2');
INSERT INTO `catalogue` (product_id, seller_id, price) VALUES (1, 1, 5.99), (2, 1, 2.50), (3, 1, 4.99), (4, 1, 5.50), (5, 1, 3.50), (6, 1, 3.49),
  (7, 1, 5.99), (1, 2, 4.50);
INSERT INTO `product` (name, stock_count) VALUES ('dog biscuits', 15),('flea powder', 20),('collar', 20),
  ('nail file', 20),('vitamins', 20),('shampoo', 15),('tick remover', 10);
INSERT INTO `card` VALUES ('1234123412341234','302010','VISA', '2028-7-04', '123'),
  ('5678567856785678','112233', 'VISA', '2023-1-01', '999'),
  ('1000100010001000','110033', 'MASTERCARD', '2025-12-12', '555');
INSERT INTO `paypal` VALUES ('1111', 1000.00),
  ('2222', 1000.00);
