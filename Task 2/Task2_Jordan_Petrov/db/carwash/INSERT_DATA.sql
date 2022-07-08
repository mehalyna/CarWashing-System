\c carwashdb

INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Izio', '54 Northfield Drive', 40);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Omba', '4256 Thackeray Avenue', 1);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Twinder', '98369 Sachtjen Pass', 78);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Roombo', '8039 Memorial Place', 92);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Shufflester', '00 Arizona Point', 56);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Meevee', '65 Pleasure Plaza', 19);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Podcat', '4 Darwin Hill', 78);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Jayo', '094 Merrick Avenue', 56);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Twitterwire', '4873 Colorado Terrace', 39);
INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) VALUES ('Gabcube', '410 Fuller Parkway', 33);

INSERT INTO services (service_name) VALUES ('matrix');
INSERT INTO services (service_name) VALUES ('Multi-layered');
INSERT INTO services (service_name) VALUES ('interactive');
INSERT INTO services (service_name) VALUES ('dynamic');
INSERT INTO services (service_name) VALUES ('Diverse');
INSERT INTO services (service_name) VALUES ('impactful');
INSERT INTO services (service_name) VALUES ('Proactive');
INSERT INTO services (service_name) VALUES ('asynchronous');
INSERT INTO services (service_name) VALUES ('asynchronous');
INSERT INTO services (service_name) VALUES ('Innovative');

INSERT INTO carwash_services (service_id, carwash_id) VALUES (6, 8);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (10, 9);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (6, 1);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (10, 8);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (1, 10);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (4, 9);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (10, 5);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (6, 9);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (2, 3);
INSERT INTO carwash_services (service_id, carwash_id) VALUES (9, 7);

INSERT INTO places (place_name) VALUES ('Douglas, Carroll and Morissette');
INSERT INTO places (place_name) VALUES ('Friesen, Kautzer and Gorczany');
INSERT INTO places (place_name) VALUES ('Franecki LLC');
INSERT INTO places (place_name) VALUES ('VonRueden LLC');
INSERT INTO places (place_name) VALUES ('Glover, Emard and Davis');
INSERT INTO places (place_name) VALUES ('Renner, Greenholt and Satterfield');
INSERT INTO places (place_name) VALUES ('Hammes Group');
INSERT INTO places (place_name) VALUES ('Bauch, Flatley and Hermiston');
INSERT INTO places (place_name) VALUES ('Kreiger Group');
INSERT INTO places (place_name) VALUES ('Langworth-Rowe');

INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (8, 1, true);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (2, 6, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (7, 3, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (5, 9, true);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (8, 7, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (7, 6, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (8, 8, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (8, 6, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (4, 7, false);
INSERT INTO carwash_places (place_id, carwash_id, is_free) VALUES (4, 6, true);

INSERT INTO users (phone_number, full_name, user_location) VALUES ('473-491-4641', 'Eada Elkins', '996 Karstens Crossing');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('268-223-4133', 'Gennifer Alvarado', '9693 Utah Circle');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('697-104-1027', 'Marian Grebert', '195 Loomis Pass');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('785-960-3220', 'Valaria Eskriet', '5 Bunker Hill Drive');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('156-356-9947', 'Wynn Faccini', '2238 Charing Cross Circle');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('374-662-3659', 'Ellynn Dorrington', '9 Crowley Junction');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('827-220-2903', 'Maridel Cottesford', '73 Coolidge Point');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('293-356-0325', 'Niles Kayser', '447 Sheridan Crossing');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('501-882-1380', 'Travis Detheridge', '54174 Union Junction');
INSERT INTO users (phone_number, full_name, user_location) VALUES ('112-408-3808', 'Clarissa Sesons', '2 Carberry Point');


INSERT INTO accounts (user_id, email, password) VALUES (1, 'lalenin0@ebay.com', '4Tostzz');
INSERT INTO accounts (user_id, email, password) VALUES (2, 'bworgan1@arizona.edu', '8RqCvC');
INSERT INTO accounts (user_id, email, password) VALUES (3, 'iportis2@taobao.com', 'UO5cj3oDj');
INSERT INTO accounts (user_id, email, password) VALUES (4, 'mgoburn3@linkedin.com', '3ANnjHYiv');
INSERT INTO accounts (user_id, email, password) VALUES (5, 'santonchik4@sbwire.com', 'qeB6h5xE4F');
INSERT INTO accounts (user_id, email, password) VALUES (6, 'dhacaud5@sun.com', 'PkOUYYIW');
INSERT INTO accounts (user_id, email, password) VALUES (7, 'adevers6@va.gov', 'vz8BISbrio9');
INSERT INTO accounts (user_id, email, password) VALUES (8, 'bsaker7@dot.gov', 'bZ93Np21HCZz');
INSERT INTO accounts (user_id, email, password) VALUES (9, 'abrompton8@yellowpages.com', 'XEwrqbFJXyZ3');
INSERT INTO accounts (user_id, email, password) VALUES (10, 'bmartinelli9@walmart.com', 'lBVQZrcXp88');


INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (8, 6, 'in_progress', '2015-06-09 12:45', '2020-06-15');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (8, 9, 'finished', '2012-05-02 15:28', '2016-05-11');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (10, 6, 'waiting', '2017-04-23 16:59', '2012-07-31');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (4, 7, 'waiting', '2016-09-29 09:10', '2016-10-10');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (2, 5, 'in_progress', '2019-11-29 10:52', '2008-09-17');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (6, 6, 'finished', '2009-10-06 12:00', '2013-06-08');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (6, 4, 'in_progress', '2022-02-19 13:15', '2017-11-22');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (6, 3, 'finished', '2014-10-16 11:45', '2010-06-27');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (9, 9, 'in_progress', '2012-10-24 13:28', '2016-10-01');
INSERT INTO orders (carwash_id, user_id, order_current_status, order_date_time, execution) VALUES (8, 5, 'waiting', '2017-05-14 14:55', '2010-05-10');

