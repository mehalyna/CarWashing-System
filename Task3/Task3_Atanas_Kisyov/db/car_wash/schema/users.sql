CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    phone_number VARCHAR(15),
    full_name VARCHAR(30) NOT NULL,
    user_location VARCHAR(50)
);