/**
Q1. SQL_Question_1
Write a SQL query to print department name along with 
department wise average salary. The average salary should be rounded 
to 2 decimal places.
**/
SELECT d.deptname as department_name,ROUND(AVG(e.salary),2) as average_salary
FROM employee e   
LEFT JOIN department d  
ON e.deptid = d.deptid
GROUP BY e.deptid
ORDER BY average_salary;
/**
Q2. Average Employee Salary

Write a query to get the details of the average salary 
of the employees for each department.

Save the new column as 'avg_employee_salary'
Return the result order by avg_employee_salary in descending order and 
department_id in ascending order.
**/
SELECT department_id,AVG(salary) as avg_employee_salary
FROM employees
GROUP BY department_id
ORDER BY avg_employee_salary DESC,department_id ASC;
/**
Q3. Customer Placing the Largest Number of Orders

Write an SQL query to find the customer_number for the customer 
who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have
 placed more orders than any other customer.
 **/
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;
/**
Q4. Classes More Than 5 Students

Write an SQL query to report all the classes that have at least five students.

Return the result table ordered by class in descending order.
**/
SELECT class
FROM courses
GROUP BY class
HAVING count(student) > 4
ORDER BY class;
/**
Q6. Duplicate Emails

Write an SQL query to report all the duplicate emails.

Return the result table ordered by emails.
**/
SELECT email
FROM Person
GROUP BY email
HAVING count(email) > 1
ORDER BY email;
/**
Q2. Income greater than 2000
Write a query to find the cities where employees have a 
minimum income greater than $2000.

Save the new column as 'Minimum_Income'
Round Minimum_Income up to two decimal places.
Return the result order by the City in ascending order.
**/
SELECT city,ROUND(MIN(Income),2) as Minimum_Income
FROM employees
GROUP BY city
HAVING ROUND(MIN(Income),2) > 2000
ORDER BY city;
/**
Q3. Students in Departments

Write a query to report the respective department name and 
number of students majoring in each department for 
all departments in the Department table (even ones with no current students).

Return the result table ordered by student_number in descending order.
 In case of a tie, order them by dept_name alphabetically.
 **/

SELECT d.dept_name,COUNT(s.student_id) as student_number
FROM department d  ## taking left join dept and students to get null also countable
LEFT JOIN student s 
ON s.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY COUNT(s.student_id) DESC,d.dept_name;
/**
Q4. Products Recommendation

Write a query to find the customer_id and customer_name of 
customers who bought products "Bread" and "Milk" but did not buy 
the product "Eggs".

Return the output ordered by customer_name in ascending order
**/
SELECT C.customer_id,C.customer_name
FROM customers C  
JOIN orders O  
ON C.customer_id = O.customer_id
GROUP BY C.customer_id,C.customer_name
HAVING SUM(O.product_name ="Bread")>0 AND SUM(O.product_name ="Milk")>0
AND SUM(O.product_name ="Eggs") = 0
ORDER BY C.customer_name;