CREATE TABLE IF NOT EXISTS "Order_Details"
(
    carwash_place_id integer,
    service_id integer,
    order_id integer,
    price numeric,
    duration integer,
    start_time timestamp without time zone,
    PRIMARY KEY (service_id, order_id),
    CONSTRAINT carwash_place_id FOREIGN KEY (carwash_place_id)
        REFERENCES public."Carwash_Places" (carwash_place_id) MATCH SIMPLE,
    CONSTRAINT service_id FOREIGN KEY (service_id)
        REFERENCES public."Services" (service_id) MATCH SIMPLE,
    CONSTRAINT order_id FOREIGN KEY (order_id)
        REFERENCES public."Orders" (order_id) MATCH SIMPLE
);
