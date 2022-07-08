CREATE DATABASE carwashdb;

\c carwashdb

CREATE TABLE carwashes(
    carwash_id SERIAL PRIMARY KEY NOT NULL
    , carwash_name VARCHAR(50) NOT NULL
    , carwash_address VARCHAR(255) NOT NULL
    , quantity_of_places INTEGER NOT NULL
);

CREATE TABLE services(
    service_id SERIAL PRIMARY KEY NOT NULL
    , service_name VARCHAR(50) NOT NULL
);

CREATE TABLE carwash_services(
    service_id INTEGER REFERENCES services (service_id) ON DELETE CASCADE
    , carwash_id INTEGER REFERENCES carwashes (carwash_id) ON DELETE CASCADE
    , PRIMARY KEY (service_id, carwash_id)
);

CREATE TABLE places(
    place_id SERIAL PRIMARY KEY NOT NULL
    , place_name VARCHAR(50) NOT NULL
);

CREATE TABLE carwash_places(
    carwash_place_id SERIAL PRIMARY KEY NOT NULL
    , place_id INTEGER REFERENCES places(place_id) ON DELETE CASCADE
    , carwash_id INTEGER REFERENCES carwashes(carwash_id) ON DELETE CASCADE
    , is_free BOOLEAN NOT NULL
);

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY NOT NULL
    , phone_number VARCHAR(15) NOT NULL
    , full_name VARCHAR(150) NOT NULL
    , user_location VARCHAR(100) NOT NULL
);

CREATE TABLE accounts(
    account_id SERIAL PRIMARY KEY NOT NULL
    , user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE
    , email VARCHAR(50) NOT NULL
    , password VARCHAR(50) NOT NULL
);

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY NOT NULL
    , carwash_id INTEGER REFERENCES carwashes(carwash_id) ON DELETE CASCADE
    , user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE
    , order_current_status VARCHAR(50) NOT NULL
    , order_date_time TIMESTAMP NOT NULL
    , execution DATE NOT NULL
);

CREATE TABLE order_details(
    service_id INTEGER REFERENCES services(service_id) ON DELETE CASCADE
    , order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE
    , carwash_id INTEGER REFERENCES carwashes(carwash_id) ON DELETE CASCADE
    , price FLOAT NOT NULL
    , duration INTEGER NOT NULL
    , start_time TIME NOT NULL
    , PRIMARY KEY(service_id, order_id)
);