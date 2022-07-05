### 1. Insert some data in car_wash table with SQL


```postgres
INSERT INTO car_wash (
    car_wash_id
    , car_wash_name
    , address
    , quantity_of_places) 
    VALUES (
        1
        , 'Some Car Wash'
        , 'Some street and city'
        , 1);
```

```postgres
INSERT INTO car_wash (
    car_wash_id
    , car_wash_name
    , address
    , quantity_of_places
    ) 
    VALUES (
        2
        , 'Some Other Car Wash'
        , 'Different street and city'
        , 1);
```

```postgres
INSERT INTO car_wash (
    car_wash_id
    , car_wash_name
    , address
    , quantity_of_places
    ) 
    VALUES (
        3
        , 'Car Wash at the end of the universe'
        , 'At the end of the universe'
        , 1);
```

### 2. Select data from the table

```bash
postgres=# SELECT * FROM car_wash;
 car_wash_id |            car_wash_name            |          address           | quantity_of_places 
-------------+-------------------------------------+----------------------------+--------------------
           1 | Some Car Wash                       | Some street and city       |                  1
           2 | Some Other Car Wash                 | Different street and city  |                  1
           3 | Car Wash at the end of the universe | At the end of the universe |                  1
(3 rows)
```

```bash
postgres=# SELECT car_wash_name FROM car_wash WHERE car_wash_id = 3;
            car_wash_name            
-------------------------------------
 Car Wash at the end of the universe
(1 row)
```
