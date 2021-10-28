SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS catalogue;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS onlinepayment;
DROP TABLE IF EXISTS voucher;
DROP TABLE IF EXISTS transaction;

CREATE TABLE card(
  number CHAR(16) PRIMARY KEY NOT NULL,
  sort_code CHAR(6) NOT NULL,
  type VARCHAR(16) NOT NULL,
  expiry_date DATE NOT NULL,
  cvv CHAR(3) NOT NULL,
  customer_number INT NOT NULL,
  FOREIGN KEY (customer_number) REFERENCES customer(id)
);

CREATE TABLE onlinepayment(
  name VARCHAR (20),
  number CHAR(4),
  balance FLOAT(6,2),
  customer_number INT NOT NULL,
  FOREIGN KEY (customer_number) REFERENCES customer(id),
  PRIMARY KEY (name, number)
);

CREATE TABLE customer (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR (20) UNIQUE NOT NULL,
  password CHAR(6) NOT NULL,
  f_name VARCHAR(30) NOT NULL,
  surname VARCHAR(30) NOT NULL,
  address VARCHAR(50) NOT NULL,
  email VARCHAR(30) NOT NULL,
  phone CHAR(11)
);

CREATE TABLE product(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(20),
  stock_count INT
);

CREATE TABLE catalogue(
  product_id INT,
  seller_id INT,
  price FLOAT(6,2),
  FOREIGN KEY (product_id) REFERENCES product(id),
  FOREIGN KEY (seller_id) REFERENCES seller(id),
  PRIMARY KEY (product_id, seller_id)
);

CREATE TABLE seller (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR (20) UNIQUE NOT NULL,
  password CHAR(6) NOT NULL,
  f_name VARCHAR(30) NOT NULL,
  surname VARCHAR(30) NOT NULL,
  address VARCHAR(50) NOT NULL,
  email VARCHAR(30) NOT NULL,
  phone CHAR(11),
  storefront VARCHAR(30)
);

CREATE TABLE voucher (
  id CHAR(4) PRIMARY KEY,
  expiry_date DATE NOT NULL,
  amount FLOAT(6,2)
);

CREATE TABLE transaction(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  customer_id INT NOT NULL,
  amount FLOAT(6,2) NOT NULL,
  payment_details VARCHAR(100) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer(id)
);


INSERT INTO `customer` VALUES (1,'cust1','123456','Ollie','Buckley','1 Carr St., Leeds, UK','ollie@hotmail.com','07911111111'),
  (2,'cust2','118118','James','Jameson','2 Spitfire St., Leeds, UK','james@hotmail.com','07912312312'),
  (3,'cust3','abc123','Michael','Jackson','2 Moonwalk Ave., New York, USA','annieruok@hotmail.com','07999911188');
INSERT INTO `seller` VALUES (1,'sell1','mypass','Billy','Bobson','12 Comercial St., London, UK','bb@hotmail.com','07999999999',"myLogo.png"),
  (2,'sell2','secret','Sarah','Smith','12 Spartan Ave., London, UK','sarah@hotmail.com','07900000000',"myShop.png");
INSERT INTO `catalogue` (product_id, seller_id, price) VALUES (1, 1, 5.99), (2, 1, 2.59), (3, 1, 4.99), (4, 1, 5.45), (5, 1, 3.59), (6, 1, 3.49),
  (7, 1, 5.99), (8, 2, 4.29), (1, 2, 4.29);
INSERT INTO `product` (name, stock_count) VALUES ('biscuits', 15),('powder', 20),('collar', 20),
  ('file', 20),('vitamins', 20),('shampoo', 15),('blanket', 10),('litter', 10);
INSERT INTO `card` VALUES ('1234123412341234','302010','VISA', '2028-07-04', '123', 1),
  ('5678567856785678','112233', 'VISA', '2023-01-01', '999', 2),
  ('1000100010001000','110033', 'MASTERCARD', '2025-12-12', '555', 3);
INSERT INTO `onlinepayment` VALUES ('PayPal','1111', 50.00, 1),
  ('Paypal','2222', 1000.00, 2), ('Monzo','3333', 100.00, 3);
INSERT INTO `voucher` VALUES ('1111', '2022-01-01', 50.00),
  ('2222', '2020-01-01', 100.00), ('3333', '2022-01-01', 5.00);