CREATE TABLE car_washes (
    car_wash_id serial PRIMARY KEY,
    car_wash_name carchar(50) NOT NULL UNIQUE,
    car_wash_address varchar(50) NOT NULL,
    quantity_of_places  integer
);
