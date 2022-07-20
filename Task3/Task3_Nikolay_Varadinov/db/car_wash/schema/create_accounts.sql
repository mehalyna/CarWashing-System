CREATE TABLE accounts (
    account_id integer,
    email character varying(50),
    _password character varying(50),
    user_id integer,
    CONSTRAINT accounts_pk PRIMARY KEY (account_id),
    CONSTRAINT users_fk FOREIGN KEY (user_id) REFERENCES users(user_id)
);