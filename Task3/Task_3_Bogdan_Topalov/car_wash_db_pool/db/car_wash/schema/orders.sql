CREATE TABLE IF NOT EXISTS "Orders"
(
    order_id integer,
    carwash_id integer,
    user_id integer,
    order_current_status character varying(15),
    order_date_time timestamp without time zone,
    execution date,
    PRIMARY KEY (order_id),
    CONSTRAINT carwash_id FOREIGN KEY (carwash_id)
        REFERENCES "Carwashes" (carwash_id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES "Users" (user_id)
);
