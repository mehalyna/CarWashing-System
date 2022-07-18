CREATE TABLE users(
    user_id SERIAL PRIMARY KEY NOT NULL
    , phone_number VARCHAR(15) NOT NULL
    , full_name VARCHAR(50) NOT NULL
    , user_location VARCHAR(100) NOT NULL
);
