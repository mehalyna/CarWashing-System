CREATE TABLE order_details (
    service_id integer
    , order_id integer
    , price float
    , duration integer
    , start_time time
    , carwash_place_id integer
    , CONSTRAINT order_details_pk PRIMARY KEY (service_id, order_id)
    , CONSTRAINT services_fk0 FOREIGN KEY (service_id) REFERENCES services(service_id)
    , CONSTRAINT orders_fk1 FOREIGN KEY (order_id) REFERENCES orders(order_id)
    , CONSTRAINT carwash_places_fk2 FOREIGN KEY (carwash_place_id) REFERENCES carwash_places(carwash_place_id)
);
