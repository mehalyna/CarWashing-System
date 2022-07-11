CREATE TABLE carwash_places(
    carwash_place_id SERIAL PRIMARY KEY NOT NULL
    , place_id INTEGER REFERENCES places(place_id) ON DELETE CASCADE
    , carwash_id INTEGER REFERENCES carwashes(carwash_id) ON DELETE CASCADE
    , is_free BOOLEAN NOT NULL
);