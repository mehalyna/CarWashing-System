CREATE TABLE accounts(
    account_id SERIAL PRIMARY KEY NOT NULL
    , user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE
    , email VARCHAR(50) NOT NULL
    , password VARCHAR(50) NOT NULL
);