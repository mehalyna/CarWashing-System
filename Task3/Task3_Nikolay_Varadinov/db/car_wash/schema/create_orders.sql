CREATE TABLE orders (
    order_id integer,
    order_curent_status character varying (20),
    order_date_time timestamp,
    execution time,
    user_id integer,
    carwash_id integer,
    CONSTRAINT orders_pk PRIMARY KEY (order_id),
    CONSTRAINT users_fk0 FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT carwashes_fk1 FOREIGN KEY (carwash_id) REFERENCES carwashes(carwash_id)
);