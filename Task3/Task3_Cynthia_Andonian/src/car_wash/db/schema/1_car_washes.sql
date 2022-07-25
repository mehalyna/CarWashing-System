CREATE TABLE car_washes (
    car_wash_id SERIAL PRIMARY KEY,
    car_wash_name VARCHAR(100) NOT NULL UNIQUE,
    car_wash_address VARCHAR(100) NOT NULL,
    quantity_of_places INTEGER NOT NULL
);
