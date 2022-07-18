CREATE TABLE car_wash_places (
    car_wash_place_id INTEGER PRIMARY KEY,
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
