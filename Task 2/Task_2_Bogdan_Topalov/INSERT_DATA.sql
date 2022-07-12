INSERT INTO "Users" (
	user_id, phone_number, full_name, user_location)
	VALUES 
		(1, '0888888888', 'Bogdan Topalov', 'Somewhere'),
		(2, '0777777777', 'Ivan Ivanov', 'North Pole'),
		(3, '0666666666', 'Maria Ivanova', 'South Pole');
		

INSERT INTO "Accounts" (
	account_id, user_id, email, password)
	VALUES 
		(1, 1, 'alabala@abv.bg', '0123456789'),
		(2, 2, 'portokala@abv.bg', 'password'),
		(3, 3, 'mar4eto@abv.bg', 'hard_pasword_123');


INSERT INTO "Carwashes" (
	carwash_id, carwash_name, address, quantity_of_places)
	VALUES 
		(1, 'The Best Carwash', 'Sofia', 5);


INSERT INTO "Places" (
	place_id, place_name)
	VALUES 
		(1, 'Place #1'),
		(2, 'Place #2'),
		(3, 'Place #3'),
		(4, 'Place #4'),
		(5, 'Place #5');


INSERT INTO "Carwash_Places" (
	carwash_place_id, place_id, carwash_id, is_free)
	VALUES 
		(1, 1, 1, false),
		(2, 2, 1, true),
		(3, 3, 1, true),
		(4, 4, 1, false),
		(5, 5, 1, true);


INSERT INTO "Services" (
	service_id, service_name)
	VALUES 
		(1, 'Full clean'),
		(2, 'Outside clean'),
		(3, 'Inside clean');


INSERT INTO "Carwash_Services" (
	service_id, carwash_id)
	VALUES 
		(1, 1),
		(2, 1),
		(3, 1);


INSERT INTO "Orders" (
	order_id, carwash_id, user_id, order_current_status, order_date_time, execution)
	VALUES 
		(1, 1, 1, 'In Progress', '2022-07-11 15:30:01', '2022-07-11');


INSERT INTO "Order_Details" (
	carwash_place_id, service_id, order_id, price, duration, start_time)
	VALUES 
		(1, 2, 1, 25, 10, '2022-07-11 15:35:00');
