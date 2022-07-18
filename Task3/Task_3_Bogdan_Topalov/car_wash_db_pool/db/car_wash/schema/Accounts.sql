CREATE TABLE IF NOT EXISTS "Accounts"
(
    account_id integer NOT NULL,
    user_id integer,
    email character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    PRIMARY KEY (account_id),
    CONSTRAINT user_id FOREIGN KEY (user_id)
        REFERENCES "Users" (user_id)
);
