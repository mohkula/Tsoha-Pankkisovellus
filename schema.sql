	CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, email TEXT, phone BIGINT, address TEXT, mainUser BOOLEAN NOT NULL DEFAULT FALSE, active BOOLEAN DEFAULT FALSE);

 CREATE TABLE cards (id SERIAL PRIMARY KEY, customer_id INTEGER, account_id INTEGER , card_number BIGINT, expirationDate DATE DEFAULT now() , active BOOLEAN DEFAULT FALSE);



 CREATE TABLE bankAccounts (id SERIAL PRIMARY KEY, customer_id INTEGER , account_number TEXT, openingDate DATE DEFAULT now(), balance INTEGER DEFAULT 0, active BOOLEAN DEFAULT FALSE);



CREATE TABLE orders(id SERIAL PRIMARY KEY, type INTEGER , customer_id INTEGER NOT NULL DEFAULT 0, username TEXT, orderingDate DATE DEFAULT now());


CREATE TABLE cardWarnings(id SERIAL PRIMARY KEY, card_id INTEGER NOT NULL, type INTEGER NOT NULL, date DATE DEFAULT now(),active BOOLEAN DEFAULT FALSE);