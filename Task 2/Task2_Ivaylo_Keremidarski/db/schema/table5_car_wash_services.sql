
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
