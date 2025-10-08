

-- Departments table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100)
) ENGINE=InnoDB;


CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) 
VALUES 
('Amit', 'Sharma', 'HR', 45000, '2020-05-20'),
('Priya', 'Patel', 'Finance', 60000, '2021-02-10'),
('Ravi', 'Kumar', 'IT', 55000, '2019-08-14'),
('Neha', 'Reddy', 'Marketing', 48000, '2022-01-05'),
('Arjun', 'Singh', 'IT', 62000, '2020-09-12');

SELECT * FROM employees;

SELECT DISTINCT department 
FROM employees;

SELECT first_name, last_name, department, salary
FROM employees
WHERE salary > 50000;

SELECT first_name, last_name, salary, hire_date
FROM employees
WHERE department = 'IT';

SELECT first_name, last_name, department, salary, hire_date
FROM employees
WHERE hire_date > '2020-12-31';


SELECT first_name, last_name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT AVG(salary) AS average_salary
FROM employees;

SELECT 
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employees;

SELECT 
    department,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT 
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;

SELECT 
    department,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT 
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS employees_hired
FROM employees
GROUP BY YEAR(hire_date)
ORDER BY hire_year;




SELECT 
    emp_id,
    CONCAT(first_name, ' ', last_name) AS employee_name,
    department,
    salary,
    hire_date
FROM employees;

ALTER TABLE employees
ADD COLUMN location VARCHAR(50);

SELECT 
    emp_id,
    CONCAT(first_name, ' ', last_name) AS employee_name,
    department,
    location,
    salary,
    hire_date
FROM employees
WHERE location = 'Bangalore';

SELECT 
    emp_id,
    first_name,
    last_name,
    department,
    salary,
    hire_date
FROM 
    employees;


SELECT dept.department AS department_name
FROM (
    SELECT 'HR' AS department
    UNION ALL
    SELECT 'Sales'
    UNION ALL
    SELECT 'IT'
    UNION ALL
    SELECT 'Finance'
) AS dept
LEFT JOIN employees e
ON dept.department = e.department
WHERE e.emp_id IS NULL;

SELECT 
    department,
    COUNT(*) AS employee_count
FROM 
    employees
GROUP BY 
    department;

    SELECT 
    emp_id,
    first_name,
    last_name,
    department,
    salary,
    hire_date
FROM 
    employees
WHERE 
    salary > (SELECT AVG(salary) FROM employees);


INSERT INTO departments (name, location) VALUES ('HR', 'Hyderabad');
INSERT INTO departments (name, location) VALUES ('Finance', 'Mumbai');
INSERT INTO departments (name, location) VALUES ('IT', 'Bangalore');
INSERT INTO departments (name, location) VALUES ('Marketing', 'Chennai');
INSERT INTO departments (name, location) VALUES ('Operations', 'Delhi');


SELECT * FROM departments;

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

SELECT *
FROM employees
ORDER BY hire_date DESC
LIMIT 1;

SELECT *
FROM employees
WHERE salary = (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
);

SELECT *
FROM employees
WHERE department = (
    SELECT department
    FROM employees
    WHERE first_name = 'Amit' AND last_name = 'Sharma'
);

UPDATE employees
SET salary = salary * 1.10
WHERE department = 'IT';

SELECT * FROM employees;

UPDATE employees
SET department = 'Marketing'
WHERE first_name = 'Ravi' AND last_name = 'Kumar';
SELECT * FROM employees;

DELETE FROM employees
WHERE salary < 40000;
SELECT * FROM employees;

ALTER TABLE employees
ADD COLUMN email VARCHAR(100);
UPDATE employees
SET email = CONCAT(LOWER(first_name), '.', LOWER(last_name), '@example.com');
SELECT * FROM employees;
UPDATE employees SET email = 'amit.sharma@company.com' WHERE first_name = 'Amit' AND last_name = 'Sharma';
UPDATE employees SET email = 'priya.patel@company.com' WHERE first_name = 'Priya' AND last_name = 'Patel';
UPDATE employees SET email = 'ravi.kumar@company.com' WHERE first_name = 'Ravi' AND last_name = 'Kumar';
UPDATE employees SET email = 'neha.reddy@company.com' WHERE first_name = 'Neha' AND last_name = 'Reddy';
UPDATE employees SET email = 'arjun.singh@company.com' WHERE first_name = 'Arjun' AND last_name = 'Singh';
SELECT * FROM employees;

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 2;

SELECT d.location AS city, COUNT(e.emp_id) AS employee_count
FROM employees e
JOIN departments d ON e.department = d.name
GROUP BY d.location;

SELECT department, COUNT(*) AS employee_count, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT *
FROM employees
WHERE first_name LIKE 'A%';

SELECT *
FROM employees
WHERE last_name LIKE '%a';

SELECT *
FROM employees
WHERE YEAR(hire_date) = 2020;

SELECT first_name, last_name, DATEDIFF(CURDATE(), hire_date) AS days_since_hired
FROM employees;

SELECT UPPER(first_name) AS first_name_upper, UPPER(last_name) AS last_name_upper
FROM employees;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

SELECT *
FROM employees
WHERE salary BETWEEN 45000 AND 60000;

CREATE VIEW high_salary_employees AS
SELECT *
FROM employees
WHERE salary > 55000;
SELECT * FROM high_salary_employees;

SELECT *
FROM high_salary_employees;

ALTER TABLE departments
MODIFY COLUMN name VARCHAR(100) NOT NULL;
select * from departments;


DROP VIEW IF EXISTS employee_summary;

RENAME TABLE employees TO staff;

CREATE TABLE employees_backup AS
SELECT * FROM employees;
SELECT * FROM employees_backup;

DELETE FROM employees;

DROP TABLE IF EXISTS employees_backup;

CREATE INDEX idx_last_name ON staff(last_name);


DROP INDEX idx_last_name ON staff;