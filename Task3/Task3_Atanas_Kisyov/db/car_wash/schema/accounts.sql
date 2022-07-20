CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    email VARCHAR(50),
    password VARCHAR(100),
    CONSTRAINT fk_user_id
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
    ON DELETE CASCADE
);