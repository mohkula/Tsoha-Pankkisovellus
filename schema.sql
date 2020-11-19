CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT,
 email TEXT, phone INTEGER, address TEXT, mainUser BOOLEAN NOT NULL DEFAULT FALSE);


