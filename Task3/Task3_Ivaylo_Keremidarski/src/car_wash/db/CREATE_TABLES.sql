CREATE TABLE car_washes (
    car_wash_id SERIAL PRIMARY KEY,
    car_wash_name VARCHAR(100) NOT NULL UNIQUE,
    car_wash_address VARCHAR(100) NOT NULL,
    quantity_of_places INTEGER NOT NULL
);

CREATE TABLE places (
    place_id SERIAL PRIMARY KEY,
    place_name VARCHAR(100) UNIQUE
);

CREATE TABLE car_wash_places (
    car_wash_place_id SERIAL PRIMARY KEY,
    place_id INTEGER NOT NULL,
    car_wash_id INTEGER NOT NULL,
    is_free BOOL,
    CONSTRAINT fk_place_id
        FOREIGN KEY (place_id)
        REFERENCES places(place_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_car_wash_id
        FOREIGN KEY (car_wash_id)
        REFERENCES car_washes(car_wash_id)
    ON DELETE CASCADE
);

CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(50)
);


CREATE TABLE car_wash_services (
    service_id INTEGER,
    car_wash_id INTEGER,
    PRIMARY KEY (service_id, car_wash_id),
    CONSTRAINT fk_service_id
        FOREIGN KEY (service_id)
        REFERENCES services(service_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_car_wash_id
        FOREIGN KEY (car_wash_id)
        REFERENCES car_washes(car_wash_id)
    ON DELETE CASCADE
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    phone_number VARCHAR(15),
    full_name VARCHAR(30) NOT NULL,
    user_location VARCHAR(50)
);

CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    email VARCHAR(50),
    password VARCHAR(100),
    CONSTRAINT fk_user_id
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
    ON DELETE CASCADE
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    car_wash_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    order_current_status VARCHAR(20),
    order_date_time TIMESTAMP,
    execution TIME,
    CONSTRAINT fk_car_wash_id
        FOREIGN KEY (car_wash_id)
        REFERENCES car_washes(car_wash_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_user_id
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
    ON DELETE CASCADE
);

CREATE TABLE order_details (
    car_wash_place_id INTEGER NOT NULL,
    service_id INTEGER,
    order_id INTEGER,
    price NUMERIC NOT NULL,
    duration INTEGER NOT NULL,
    start_time TIME,
    PRIMARY KEY (service_id, order_id),
    CONSTRAINT fk_car_wash_place_id
        FOREIGN KEY (car_wash_place_id)
        REFERENCES car_washes(car_wash_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_service_id
        FOREIGN KEY (service_id)
        REFERENCES services(service_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_order_id
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
    ON DELETE CASCADE
);
