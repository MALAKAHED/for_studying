--------------------------------
-- Database for a company 
--------------------------------

-- employee table 
CREATE TABLE IF NOT EXISTS employee (
    id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    birth_day DATE,
    sex VARCHAR(1),
    selary INT,
    super_id INT,
    Branch_ID INT
);

-- branch table with it's PK & FK
CREATE TABLE IF NOT EXISTS branch (
branch_ID INT PRIMARY KEY,
branch_name VARCHAR(50),
mgr_id INT,
mgr_start_date DATE,
FOREIGN KEY (mgr_id) REFERENCES employee(id) ON DELETE SET NULL
);

--adding FK to the employee table 
ALTER TABLE employee 
ADD FOREIGN KEY (Branch_ID) 
REFERENCES branch(branch_ID)
ON DELETE SET NULL 

ALTER TABLE employee 
ADD FOREIGN KEY (super_id)
REFERENCES employee(id)
ON DELETE SET NULL

-- creating the client table with it;s PK & FK 
CREATE TABLE IF NOT EXISTS client (
client_id INT PRIMARY KEY , 
client_name VARCHAR (50),
Branch_ID INT
FOREIGN KEY (branch_ID)
REFERENCES branch(branch_ID)
ON DELETE SET NULL 
);

-- creating works_with table with it's PK & FK 
CREATE TABLE IF NOT EXISTS works_with (
emp_ID INT PRIMARY KEY,
client_id INT PRIMARY KEY,
total_sales INT

FOREIGN KEY (emp_ID)
REFERENCES employee(id)
ON DELETE CASCADE

FOREIGN KEY (client_id)
REFERENCES client(client_id)
ON DELETE CASCADE
);

-- creating branch_supplier with it's PK & FK 
CREATE TABLE IF NOT EXISTS branch_supplier (
branch_ID INT PRIMARY KEY,
supplier_name VARCHAR (50) PRIMARY KEY,
Supply_type VARCHAR(50)

FOREIGN KEY (branch_ID)
REFERENCES branch(branch_ID)
ON DELETE CASCADE
);

------------
    -- key word for defferent genders
        -- SELECT DISTINCT sex
        -- FROM employee
------------


