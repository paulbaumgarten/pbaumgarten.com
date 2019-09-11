title: PostgreSQL getting started

# Download and install

https://www.postgresql.org/download/

# Edit configuration

This configuration change allows you to login to postgres as postgres users (duh!, why would that be not possible by default?)

Edit the file `/etc/postgresql/9.1/main/pg_hba.conf`

Change this line

```txt
local all all peer
```

to:

```text
local all all md5
```

Restart the postgres server with either one of the following commands:

```bash
sudo service postgresql restart
sudo /etc/init.d/postgresql restart
```

# Login as postgres user

If on linux, login as the postgres user using `su - postgres` (automatically created during the installation process). If on macOS, there is no postgres user so just open the console tool directly.

# Creating a database

From the terminal, create your database using `createdb`:

```bash
$ createdb my_database
```

# Open management tool and connect

Open the console tool using `psql`.

```bash
$ psql
```

Connect to the database using `\c`

```postgresql
# \c my_database
```

# Create new user

CREATE USER milestone WITH PASSWORD 'milestone';
GRANT ALL ON DATABASE "my_database" TO milestone;
GRANT ALL ON ALL TABLES IN SCHEMA public TO milestone;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO milestone;

# SQL notes

* PostgreSQL uses only single quotes for values eg `SELECT * FROM foo WHERE bar = 'value';`
* Double quotes are used for field or table names eg `WHERE "last name" = 'Smith'`
* PostgreSQL is case-sensitive for string comparisons
* Database, table, field and columns names in PostgreSQL are case-independent, unless you created them with double-quotes around their name, in which case they are case-sensitive.

# Auto increment

Creates a field `id` as an auto incrementing integer and primary key

```sql
CREATE TABLE foo (id serial PRIMARY KEY, bar text);
```

# Views

```sql
CREATE VIEW staff_having_goals AS
SELECT staffid, firstname || lastname as fullname
FROM Staff
WHERE datefired ISNULL and seniorstaff = TRUE
ORDER BY lastname, firstname
```

# Show databases and tables

\l              # SHOW DATABASES
\dt             # SHOW TABLES
\d myTable      # DESCRIBE myTable


