CREATE TABLE order_details(
    service_id INTEGER REFERENCES services(service_id) ON DELETE CASCADE
    , order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE
    , carwash_id INTEGER REFERENCES carwashes(carwash_id) ON DELETE CASCADE
    , price FLOAT NOT NULL
    , duration INTEGER NOT NULL
    , start_time TIME NOT NULL
    , PRIMARY KEY(service_id, order_id)
);