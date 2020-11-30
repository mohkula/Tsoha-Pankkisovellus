	CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT,
 email TEXT, phone INTEGER, address TEXT, mainUser BOOLEAN NOT NULL DEFAULT FALSE);

 CREATE TABLE cards (id SERIAL PRIMARY KEY, customer_id INTEGER, account_id INTEGER , card_number BIGINT, expirationDate DATE DEFAULT now());



 CREATE TABLE bankAccounts (id SERIAL PRIMARY KEY, customer_id INTEGER , account_number TEXT, openingDate DATE DEFAULT now(), balance INTEGER DEFAULT 0);



