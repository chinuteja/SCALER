/**
 Assignemnt - 1
Q1. Department (No emp)
Problem Statement:

Write a query to display the details of all those departments 
that don't have any working employees.

Return the columns 'department_id', and 'department_name'.
Return the results ordered by 'department_id' in ascending order.
**/

SELECT d.department_id,d.department_name
FROM departments AS d
LEFT JOIN employees AS e
ON d.department_id = e.department_id
WHERE e.employee_id IS NULL
ORDER BY d.department_id;
/**
Q2. Manager left

Write a query to find the employee_id of the employees whose salary is
 strictly less than $15000 and whose manager left the company.

When a manager leaves the company, their information is deleted 
from the employees table, but the reports still have their manager_id 
set to the manager that left.

Note: Return the result ordered by employee_id in ascending order.
**/
select employee_id from employees emp where emp.salary < 15000
and manager_id  not in (select employee_id from employees)
order by employee_id asc;

/**
Q4. Employees & Offices
Write a SQL query to get all the possible combinations of 
employees and offices.

Return the output ordered by employeeNumber and officeCode in ascending order.
**/
SELECT e.employeeNumber,e.firstName,e.lastName,o.officeCode,o.city 
FROM employees AS e
CROSS JOIN offices AS o
ORDER BY e.employeeNumber,o.officeCode;

/**
Q5. Combine Two Tables
Write an SQL query to report the city of each person in the Person table. 
If the address of a personId is not present in the Address table, 
report null instead.

Return the result table in order of city names.
**/
SELECT a.city
FROM person as p
LEFT JOIN address as a
ON p.personId = a.personId
ORDER BY a.city;
/**
Q1. Employee Bonus Query
Write a query to report the name of each employee with a bonus of less 
than 1000.

Return the bonus as 'NULL' if an employee doesn’t have a bonus of less 
than 1000.
Return the result table sorted w.r.t. name of the employees in ascending order.
**/
SELECT e.name, b.bonus
FROM employee e
LEFT JOIN Bonus b 
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL
ORDER BY e.name ASC;

/**
Q3. Handles No Customers
Write a SQL query to find the employee details who handles no customers.

Note:

Use the given customers table.
Return the output ordered by employeeNumber in ascending order.
The salesRepEmployeeNumber column to the employeeNumber who made 
sales to the customers.
**/
SELECT e.employeeNumber,e.firstName,e.lastName
FROM employees as e 
LEFT JOIN customers as c 
ON e.employeeNumber = c.salesRepEmployeeNumber
WHERE c.salesRepEmployeeNumber IS NULL;

/**
Q3. Ad-Free Sessions
Write a query to report all the sessions that did not get shown any ads.

Return the resultant table ordered by session_id in ascending order.
**/
SELECT DISTINCT p.session_id
FROM Playback as p  
LEFT JOIN Ads as a   
ON p.customer_id = a.customer_id
WHERE a.timestamp NOT BETWEEN p.start_time AND p.end_time
OR a.ad_id IS NULL
ORDER BY p.session_id;


SELECT DISTINCT p.session_id
FROM Playback as p  
LEFT JOIN Ads as a   
ON p.customer_id = a.customer_id
WHERE a.timestamp < p.start_time OR a.timestamp > p.end_time
OR a.ad_id IS NULL
ORDER BY p.session_id;
/**
Q2. Manager left
Write a query to find the employee_id of the employees whose salary is
 strictly less than $15000 and whose manager left the company.

When a manager leaves the company, their information is 
deleted from the employees table, but the reports still have their 
manager_id set to the manager that left.

Note: Return the result ordered by employee_id in ascending order.
**/

SELECT a.employee_id
FROM employees as a
JOIN employees as b
ON a.manager_id = b.employee_id
WHERE a.salary < 15000
AND a.manager_id IS NOT NULL AND b.employee_id IS NULL
ORDER BY a.employee_id;