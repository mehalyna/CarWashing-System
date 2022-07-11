CREATE TABLE users (
    user_id integer
    , phone_number character varying (15)
    , full_name character varying (30) NOT NULL
    , user_location character varying (100)
    , CONSTRAINT users_pk PRIMARY KEY (user_id)
);

CREATE TABLE carwashes (
    carwash_id integer
    , carwash_name character varying (15)
    , _address character varying
    , quantity_of_places smallint
    , CONSTRAINT carwashes_pk PRIMARY KEY (carwash_id)
);

CREATE TABLE services (
    service_id integer
    , service_name character varying (100)
    , CONSTRAINT services_pk PRIMARY KEY (service_id)
);

CREATE TABLE places (
    place_id integer
    , place_name character varying (30)
    , CONSTRAINT places_pk PRIMARY KEY (place_id)
);

CREATE TABLE carwash_services (
    service_id integer
    , carwash_id integer
    , CONSTRAINT carwash_services_pk PRIMARY KEY (service_id, carwash_id)
    , CONSTRAINT services_fk0 FOREIGN KEY (service_id) REFERENCES services(service_id)
    , CONSTRAINT carwashes_fk1 FOREIGN KEY (carwash_id) REFERENCES carwashes(carwash_id)
);

CREATE TABLE carwash_places (
    carwash_place_id integer
    , is_free boolean
    , place_id integer
    , carwash_id integer
    , CONSTRAINT carwash_places_pk  PRIMARY KEY (carwash_place_id)
    , CONSTRAINT places_fk0 FOREIGN KEY (place_id) REFERENCES places(place_id)
    , CONSTRAINT carwashes_fk1 FOREIGN KEY (carwash_id) REFERENCES carwashes(carwash_id)
);

CREATE TABLE accounts (
    account_id integer
    , email character varying(50)
    , _password character varying(50)
    , user_id integer
    , CONSTRAINT accounts_pk PRIMARY KEY (account_id)
    , CONSTRAINT users_fk FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE orders (
    order_id integer
    , order_curent_status character varying (20)
    , order_date_time timestamp
    , execution time
    , user_id integer
    , carwash_id integer
    , CONSTRAINT orders_pk PRIMARY KEY (order_id)
    , CONSTRAINT users_fk0 FOREIGN KEY (user_id) REFERENCES users(user_id)
    , CONSTRAINT carwashes_fk1 FOREIGN KEY (carwash_id) REFERENCES carwashes(carwash_id)
);

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
