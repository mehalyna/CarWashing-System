CREATE DATABASE IF NOT EXISTS carwashDB
    WITH
    OWNER = bogdan
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

\i schema/Users.sql
\i schema/Accounts.sql
\i schema/Carwashes.sql
\i schema/PLaces.sql
\i schema/Carwash_Places.sql
\i schema/Services.sql
\i schema/Carwash_Services.sql
\i schema/Orders.sql
\i schema/Order_Details.sql
