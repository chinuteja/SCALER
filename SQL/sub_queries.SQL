/**
Q1. No Job history
Display all the details of the employees 
who did not work at any job in the past.

Return all the columns from the employee's table.
Return the result ordered by employee_id in ascending order.
**/
SELECT * FROM employees
WHERE employee_id NOT IN 
(SELECT employee_id FROM job_history);
/**
Q2. Customers order
Write a query to find all the customers who have not ordered anything.

Return the name of the customers as 'Customers'.
**/
SELECT Name AS Customers FROM customers
WHERE Id NOT IN (
	SELECT Cust_id FROM orders
);
/**
Q4. Department name
Problem Description:

Find the details of the employees who are working in the 
departments 'Administration', 'Marketing', and 'Human Resources'.

Return the columns 'employee_id', 'full_name'(first and last name 
separated by space), and 'salary'.
Return the result ordered by employee_id in ascending order.
**/
SELECT employee_id,full_name,salary FROM employees
WHERE department_id IN (
	SELECT department_id FROM departments
	WHERE department_name IN ('Administration', 'Marketing', 'Human Resources')
) ORDER BY employee_id;
/**
Q3. 4 or More employees
Write a query to display the "full_name" 
(first name and last name separated by space) of a manager who manages 4 or more employees.

Note:

Return the result ordered by full_name in ascending order.
The column manager_id in the employees table represents the employee_id 
of the manager.
**/
SELECT CONCAT(first_name," ",last_name) as full_name FROM employees
WHERE employee_id IN (

	SELECT manager_id FROM employees
	GROUP BY manager_id
	HAVING COUNT(employee_id) >= 4
)
ORDER BY full_name;
/**
Q2. Candidates Skills

Given a list of candidates and their skills, 
you're asked to find the candidates best suited for an open 
Data Science job. We want to find candidates who are proficient
 in 'Python', 'Tableau', and 'MySQL'.

Write a query to list the candidates who possess all three required 
skills for the job.

Note: There are no duplicates in the candidates table.

Return the result ordered by candidate_id in ascending order.
**/
SELECT DISTINCT candidate_id FROM candidates
WHERE candidate_id IN (
	SELECT candidate_id FROM candidates
    WHERE skill IN ('Python', 'Tableau','MySQL')
	GROUP BY candidate_id
	HAVING COUNT(DISTINCT skill) = 3
);

/**
Q3. Seattle
Display the details of all the employees whose department 
location is in Seattle.

Return the columns 'employee_id', 'first_name', 'last_name', and job_id'.
Return the table ordered by employee_id in ascending order.
**/
SELECT e.employee_id,e.first_name,e.last_name,e.job_id
FROM employees e
JOIN departments d 
ON e.department_id = d.department_id
JOIN locations l  
ON d.location_id = l.location_id
WHERE l.city = "Seattle"; 


##### solve using subquerys

SELECT employee_id, first_name, last_name, job_id 
FROM employees 
WHERE 
  department_id IN (
    SELECT department_id
    FROM departments  
    WHERE location_id IN (
        SELECT location_id   
        FROM  locations      
        WHERE city = "Seattle"  
      )
  );

/**
Q4. Employee 107

Write a query to find the details of the other employees who work in the 
same job as the employee with employee_id as 107.
Create a new column "full_name" by concatenating the first_name and last_name columns, separated by space.
Return the columns 'full_name', 'salary', 'department_id', and 'job_id'.
Return the output ordered by full_name in ascending order.
**/
SELECT CONCAT(first_name," ",last_name) as full_name, salary,department_id,job_id
FROM employees
WHERE job_id IN
(
	SELECT job_id FROM employees
	WHERE employee_id = 107
)
ORDER BY full_name;
/**
Q5. 3rd highest
Write a SQL query to find all the details of those 
employees who earn the third-highest salary.

Return all the columns from the employees table.

**/
SELECT * FROM employees WHERE salary = (
SELECT DISTINCT salary
FROM employees 
ORDER BY salary DESC
LIMIT 1 OFFSET 2);



/**
Q1. Request Confirmation Messages
Write a query to find the IDs of the users that requested a 
confirmation message twice within a 24-hour window.
**/
select distinct c1.user_id
from confirmations c1
join confirmations c2
on c1.user_id = c2.user_id
and timestampdiff(second, c2.time_stamp, c1.time_stamp) <= 86400
and timestampdiff(second, c2.time_stamp, c1.time_stamp) > 0
ORDER BY c1.user_id;
/**
Q5. Consecutive Available
Write an SQL query to report all the consecutive available seats in the cinema.

Return the result table ordered by seat_id.

The test cases are generated so that more than two seats are consecutively available.
**/
SELECT seat_id
FROM cinema
WHERE free=1 AND
(seat_id+1 IN
(SELECT seat_id FROM cinema WHERE free=1)
OR
seat_id-1 IN (SELECT seat_id FROM cinema WHERE free=1));