CREATE TABLE accounts(
    account_id SERIAL PRIMARY KEY NOT NULL
    , email VARCHAR(50) NOT NULL
    ,user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE
    , password VARCHAR(50) NOT NULL
);
