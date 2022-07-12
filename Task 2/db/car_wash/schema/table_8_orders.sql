CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
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
