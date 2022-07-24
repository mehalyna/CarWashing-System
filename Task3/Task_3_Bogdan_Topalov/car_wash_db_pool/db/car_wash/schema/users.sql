CREATE TABLE IF NOT EXISTS "Users"
(
    user_id integer NOT NULL,
    phone_number character varying(15) NOT NULL,
    full_name character varying(150) NOT NULL,
    user_location character varying(100) NOT NULL,
    PRIMARY KEY (user_id)
)
