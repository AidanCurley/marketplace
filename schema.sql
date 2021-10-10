SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS storefront;
DROP TABLE IF EXISTS catalogue;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS paypal;

CREATE TABLE card(
  number CHAR(16) PRIMARY KEY,
  sort_code CHAR(6),
  cvv CHAR(3)
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
  price FLOAT(6,2),
  FOREIGN KEY (product_id) REFERENCES product(id)
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
  storefront_id INTEGER NOT NULL,
  catalogue_id INTEGER NOT NULL,
  FOREIGN KEY (catalogue_id) REFERENCES catalogue(id),
  FOREIGN KEY (storefront_id) REFERENCES storefront(id)
);


INSERT INTO `customer` VALUES ('1','cust1','123456','John','Johnson','1 Carr St., Leeds, UK','john@hotmail.com','07912312312','1234123412341234','1111'),
  ('2','cust2','123456','James','Jameson','2 Spitfire St., Leeds, UK','james@hotmail.com','07912312312','5678567856785678','2222'),
  ('3','cust3','123456','Mike','Mitchell','22 Slatchett Row, Liverpool, UK','mike@hotmail.com','07999999999','1000100010001000','2222');
INSERT INTO `seller` VALUES ('1','sell1','123456','Billy','Bobson','12 Comercial St., London, UK','bb@hotmail.com','07912312312','1','1'),
  ('2','sell2','123456','Sarah','Smith','12 Spartan Ave., London, UK','sarah@hotmail.com','07912312312','2','2');
INSERT INTO `storefront` VALUES ('1','logo1'),
  ('2','logo2');
INSERT INTO `catalogue` VALUES ('1','1','5.99'),
  ('2','2','4.99'),
  ('3','3','5.99'),
  ('4','2','0.99'),
  ('5','5','10.99'),
  ('6','6','6.99'),
  ('7','7','2.99');
INSERT INTO `product` VALUES ('1','dog biscuits', '15'),('2','flea powder', '20'),('3','collar', '20'),
  ('4','nail file', '20'),('5','vitamins', '10'),('6','shampoo', '20'),('7','tick remover', '20');
INSERT INTO `card` VALUES ('1234123412341234','302010','123'),
  ('5678567856785678','112233','999'),
  ('1000100010001000','110033','555');
INSERT INTO `paypal` VALUES ('1111','1000.00'),
  ('2222','1000.00');
