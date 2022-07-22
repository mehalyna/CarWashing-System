INSERT INTO car_washes (car_wash_id, car_wash_name, car_wash_address, quantity_of_places)
VALUES ('Ace Car Wash', '402 Kroger Way', 3),
       ('Shinetastic', '3 Chelsea Dr', 3),
       ('Quick Clean', '1521 E Alexis Rd', 1);
       
INSERT INTO places (place_id, place_name)
VALUES ('Room 1'),
       ('Room 2'),
       ('Room 3'),
       ('Room 4'),
       ('Room 5'),
       ('Room 6'),
       ('Room 7');

INSERT INTO car_wash_places (place_id, car_wash_id, is_free)
VALUES (1, 1, False),
       (2, 1, True),
       (3, 1, True),
       (4, 2, False),
       (5, 2, True),
       (6, 2, False),
       (7, 3, True);

INSERT INTO services (service_name)
VALUES ('Extirior Cleaning'),
       ('Interior Cleaning'),
       ('Full Cleaning');

INSERT INTO car_wash_services (service_id, car_wash_id)
VALUES (1, 1),
       (2, 1),
       (3, 1),
       (1, 2),
       (2, 2),
       (3, 2),
       (1, 3),
       (2, 3),
       (3, 3);

INSERT INTO users (phone_number, full_name, user_location)
VALUES ('+19159969739', 'David Smith', 'Pittsburgh, Pennsylvania'),
       ('+17864206154', 'Maria Garcia', 'San Antonio, Texas'),
       ('+14148929343', 'James Johnson', 'Nashville, Tennessee');

INSERT INTO accounts (user_id, email, password)
VALUES (1, 'davidsmith@gmail.com', 'secret123'),
       (2, 'garciam@gmail.com', 'losiento7'),
       (3, 'doublej@gmail.com', 'qwerty77');

INSERT INTO orders (car_wash_id, user_id, order_current_status, order_date_time, execution)
VALUES (1, 1, 'New', now(), now()),
       (2, 2, 'New', now(), now()),
       (3, 3, 'New', now(), now());

INSERT INTO order_details (car_wash_place_id, service_id, order_id, price, duration, start_time)
VALUES (1, 1, 1, 5.99, 1, now()),
       (5, 2, 2, 4.99, 1, now()),
       (7, 3, 3, 9.99, 2, now());
