SHOW DATABASES ;
CREATE DATABASE IF NOT EXISTS 'hbtn_0c_0';
DROP DATABASE IF EXISTS 'hbtn_0c_0';
SHOW TABLES;

CREATE TABLE IF NOT EXISTS 'first_table' (
'id' INT,
'name' VARCHAR (256)
);

SHOW CREATE TABLE 'first_table';

SELECT * FROM 'first_table';

INSERT INTO 'first_table' ('id' , 'name') VALUES ( 89 , "Best School");

SELECT COUNT(*)
FROM 'first_table'
WHERE 'id' = 89;

CREATE TABLE IF NOT EXISTS 'second_table' (
    'id' INT
    'name' VARCHAR(256)
    'score' INT
);
INSERT INTO 'second_table' ('id', 'name' , 'score') VALUES (1, 'John', 10);
INSERT INTO 'second_table' ('id', 'name' , 'score') VALUES (2, 'Alex', 3);
INSERT INTO 'second_table' ('id', 'name' , 'score') VALUES (3, 'Bob', 14);
INSERT INTO 'second_table' ('id', 'name' , 'score') VALUES (4, 'George', 8);

SELECT 'id' , 'name'
FROM 'second_table'
ORDER BY 'score' DESC ;

SELECT 'id' , 'name'
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC ;

UPDATE 'second_table'
SET 'score' = 10
WHERE 'name' = 'Bob';

DELETE FROM 'second_table'
WHERE 'score' <= 5 ; 

