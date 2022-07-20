CREATE TABLE users (
    user_id integer
    , phone_number character varying (15)
    , full_name character varying (30) NOT NULL
    , user_location character varying (100)
    , CONSTRAINT users_pk PRIMARY KEY (user_id)
);
