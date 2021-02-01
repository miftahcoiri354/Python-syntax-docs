# **Tutorial Setup TimescaleDB in PostgreSQL**

Link Installation : [TimescaleDB setup for Windows](https://www.open-plant.com/knowledge-base/timescaledb-setup-for-windows-10/)

Link Installation : [Installing TimescaleDB on Windows](https://techexpert.tips/windows/installing-timescaledb-windows/)

1. **You need to install PostgreSQL (includes the Npgsql v3.2.6-2**
2. **Before:** You need to turn off (stop) the `postgresql-x64-11` from your system service
3. **Then:** run the `TimescaleDB` setup using run as administrator and copy the following path, and yes to all access:
```
C:\Program Files\PostgreSQL\12\data\postgresql.conf
```
4. Then activate the postgresql-x64-12 use your system service
5. Open your SQL Shell and enter the psql shell, and type the following command to check the TimescaleDB already installed in your PC.
```
> SELECT * FROM pg_available_extensions WHERE name='timescaledb';

    name     | default_version | installed_version |                              comment
-------------+-----------------+-------------------+-------------------------------------------------------------------
 timescaledb | 2.0.0           |                   | Enables scalable inserts and complex queries for time-series data
(1 row)
```
```
> CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

WARNING:
WELCOME TO
 _____ _                               _     ____________
|_   _(_)                             | |    |  _  \ ___ \
  | |  _ _ __ ___   ___  ___  ___ __ _| | ___| | | | |_/ /
  | | | |  _ ` _ \ / _ \/ __|/ __/ _` | |/ _ \ | | | ___ \
  | | | | | | | | |  __/\__ \ (_| (_| | |  __/ |/ /| |_/ /
  |_| |_|_| |_| |_|\___||___/\___\__,_|_|\___|___/ \____/
               Running version 2.0.0
For more information on TimescaleDB, please visit the following links:

 1. Getting started: https://docs.timescale.com/getting-started
 2. API reference documentation: https://docs.timescale.com/api
 3. How TimescaleDB is designed: https://docs.timescale.com/introduction/architecture

Note: TimescaleDB collects anonymous reports to better understand and assist our users.
For more information and how to disable, please see our docs https://docs.timescaledb.com/using-timescaledb/telemetry.

CREATE EXTENSION
```
```
> \dx

                                      List of installed extensions
    Name     | Version |   Schema   |                            Description
-------------+---------+------------+-------------------------------------------------------------------
 adminpack   | 2.0     | pg_catalog | administrative functions for PostgreSQL
 plpgsql     | 1.0     | pg_catalog | PL/pgSQL procedural language
 timescaledb | 2.0.0   | public     | Enables scalable inserts and complex queries for time-series data
(3 rows)
```