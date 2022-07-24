CREATE TABLE carwash_services(
    service_id INTEGER REFERENCES services (service_id) ON DELETE CASCADE
    , carwash_id INTEGER REFERENCES carwashes (carwash_id) ON DELETE CASCADE
    , PRIMARY KEY (service_id, carwash_id)
);
