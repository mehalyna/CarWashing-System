CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY NOT NULL
    , carwash_id INTEGER REFERENCES carwashes(carwash_id) ON DELETE CASCADE
    , user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE
    , order_current_status VARCHAR(50) NOT NULL
    , order_date_time TIMESTAMP NOT NULL
    , execution DATE NOT NULL
);