CREATE DATABASE IF NOT EXISTS carwashDB
    WITH
    OWNER = bogdan
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

\i schema/users.sql
\i schema/accounts.sql
\i schema/carwashes.sql
\i schema/pLaces.sql
\i schema/carwash_places.sql
\i schema/services.sql
\i schema/carwash_services.sql
\i schema/orders.sql
\i schema/order_details.sql
