INSERT INTO accounts (account_id, user_id, email)
VALUES (1, 1, 'ivan@ivan.com'),
    (2, 2, 'georgi@georgi.com'),
    (3, 3, 'maria@maria.com');
INSERT INTO carwashes (
        carwash_id,
        _address,
        quantity_of_places,
    )
VALUES (1, 'Sofia 4', 6),
    (2, 'Sofia 5', 8),
    (3, 'Sofia 3', 4);
INSERT INTO carwash_places (
        carwash_place_id,
        is_free,
        place_id,
        carwash_id
    )
VALUES (1, 'True', 1, 1),
    (2, 'True', 2, 1),
    (3, 'True', 3, 1),
    (4, 'True', 4, 1),
    (5, 'True', 5, 1),
    (6, 'True', 6, 1),
    (7, 'True', 1, 2),
    (8, 'True', 2, 2),
    (9, 'True', 3, 2),
    (10, 'True', 4, 2),
    (11, 'True', 5, 2),
    (12, 'True', 6, 2),
    (13, 'True', 7, 2),
    (14, 'True', 8, 2),
    (15, 'True', 1, 3),
    (16, 'True', 2, 3),
    (17, 'True', 3, 3),
    (18, 'True', 4, 3);
INSERT INTO carwash_services (service_id, carwash_id)
VALUES (1, 1),
    (2, 1),
    (3, 1),
    (1, 2),
    (4, 2),
    (1, 3);
INSERT INTO services (service_id, service_name)
VALUES (1, 'Full'),
    (2, 'Inside'),
    (3, 'Outside'),
    (4, 'Pasting'),
    (5, 'Engine wash'),
    (6, 'Saloon wash');
INSERT INTO users (
        user_id,
        phone_number,
        full_name,
        user_location
    )
VALUES (
        1,
        '08880000001',
        'Ivan Petrov',
        'Sofia 1'
    ),
    (
        2,
        '08880000002',
        'Georgi Stoyanov',
        'Sofia 2'
    ),
    (
        3,
        '08880000003',
        'Maria Vlahova',
        'Sofia 3'
    );
