-- BD_01_ManagingData_CreatingADatabaseNotebook
-- 1
CREATE DATABASE powergrid;

-- 2
USE powergrid;

-- 3
CREATE TABLE power_consumption (
   vc_row_id int,
   voltage int,
   current int,
   power int,
   company_name varchar(255),
   date_recorded date
);

-- 4a
INSERT INTO power_consumption (vc_row_id, voltage, current)
VALUES (1, 15, 5);
-- 4b
INSERT INTO power_consumption (vc_row_id, voltage, current)
VALUES (2, 15, 10), (3, 10, 15), (4, 4, 4), (5, 6, 7);

-- 5a
SELECT vc_row_id, voltage, current 
FROM power_consumption;

-- 5b
SELECT * from power_consumption;

-- 5c
SELECT * from power_consumption
WHERE vc_row_id = 3;

-- 6
SELECT vc_row_id, voltage, SQRT(voltage)
FROM power_consumption;

-- 7
SELECT COUNT(vc_row_id) FROM power_consumption 
WHERE voltage = 10;

-- 7b
SELECT AVG(voltage) FROM power_consumption;


-- 8
SELECT COUNT(voltage) AS ten_volts, 
AVG(current) AS current_average
FROM power_consumption
WHERE voltage = 10;

-- 9a
SELECT COUNT(voltage) AS ten_volts FROM power_consumption
WHERE voltage = 10;

-- 9b
SELECT COUNT(voltage) AS ten_volts FROM power_consumption
WHERE voltage = 15;

-- 9c
SELECT COUNT(voltage) AS ten_volts FROM power_consumption
WHERE voltage = 4;

-- 9d
SELECT COUNT(voltage) AS ten_volts FROM power_consumption
WHERE voltage = 6;

-- 9e
SELECT voltage, COUNT(`vc_row_id`) AS num_companies FROM power_consumption GROUP BY voltage ;


-- 10
UPDATE power_consumption
SET voltage = 99
WHERE vc_row_id = 1;

-- 11
CREATE TABLE power_consumption (
   vc_row_id int AUTO_INCREMENT,
   voltage int,
   current int,
   power int,
   company_name varchar(255),
   date_recorded date,
  PRIMARY KEY (vc_row_id)
);

-- 11b
-- if you get an error, it's because this table already exists.
-- delete the table first, create the table and insert data (about 5 records)
DROP TABLE power_consumption;

INSERT INTO power_consumption (voltage, current)
VALUES (20, 5);

--11c
-- Now give it a go. Create the second table to hold the company information and insert 
-- some data (about 5 records)  with auto-incremented primary key constraints.
-- This table should have columns: company_row_id, company_name, email, telephone.


-- 11d .. if  the company_information table is created properly, this query should work
INSERT INTO company_information (company_name, email, telephone)
VALUES ("Barclays Bank", "helpline@barclays.com", "+27 234 567 8910");

-- 12
-- Exercise: Re-create the power_consumption table referencing the 
-- company_row_id column from the compnay_information table. 
-- Yow will need to create the company_information table first.
-- Assign about 4 rows with company_row_id


-- 14
UPDATE power_consumption
SET power = voltage * current;

-- 15a
SELECT * from power_consumption
LEFT JOIN company_information
ON power_consumption.company_row_id = company_information.company_row_id;

-- 15b
SELECT * from power_consumption
RIGHT JOIN company_information
ON power_consumption.company_row_id = company_information.company_row_id;

-- 15c
SELECT * from power_consumption
INNER JOIN company_information
ON power_consumption.company_row_id = company_information.company_row_id


-- 16
SELECT AVG(voltage) as average_voltage FROM power_consumption;
SELECT * FROM power_consumption WHERE voltage > 9;

-- 16b
SELECT * FROM power_consumption 
WHERE voltage > (
    SELECT AVG(voltage) AS average_voltage FROM power_consumption
);
