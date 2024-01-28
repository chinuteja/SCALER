/**
 * Assignment - 1
 * Write an SQL query to fetch the names of the 
 * customer that are not referred by the customer with id = 102.
 * 
**/

SELECT name FROM customer WHERE id != 102 ;
/**
 * Assignment - 2
 * Write an SQL query to report the unique customers 
 * with postive revenue in the year 2021.
**/

SELECT DISTINCT customer_id FROM customers WHERE year = 2021 AND revenue > 0;
/**
 * ASSIGNEMNT - 5
Write a query to get all the details of all the employees from 
job_history except for the employee with id 101
Return all the fields.
Return the result ordered by employee_id and job_id in ascending order.
**/
SELECT * FROM job_history WHERE employee_id != 101 ORDER BY employee_id ASC,job_id ASC;
/**
 * HOMEWORK - 1
Write a query to display the titles of the movies that are released (i.e., release_year) after 2014 and have an average vote rating (i.e.,vote_average) greater than 7.

Return the column 'original_title'.
Return the result ordered by original_title in ascending order.
**/

SELECT original_title FROM movies 
	WHERE release_year > 2014 AND vote_average > 7 
	ORDER BY original_title ASC;
/**
 * Assignment - 4
Write a query to calculate the salary of all 
employees after an increment of 20%. 
Save the newly calculated salary column as 'New_salary'.
**/
SELECT * , ROUND(salary * 1.2) AS New_salary
    FROM employees
    ORDER BY emp_id ASC ;
/**
 * ASSIGNMENT - 4
Write a query to calculate the sub_total for each order, 
return the details of the orderNumber, productCode, and sub_total
Round off the sub_total up to two decimal places.
Order the output by the orderNumber in ascending order and then by sub_total in descending order.
**/
SELECT orderNumber,productCode,ROUND(quantityOrdered*priceEach,2) as sub_total
    FROM orderdetails
    ORDER BY orderNumber ASC, sub_total DESC;