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