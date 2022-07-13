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
