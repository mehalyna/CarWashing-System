CREATE TABLE carwashes(
    carwash_id SERIAL PRIMARY KEY NOT NULL
    , carwash_name VARCHAR(50) NOT NULL
    , carwash_address VARCHAR(100) NOT NULL
    , quantity_of_places INTEGER NOT NULL
);
