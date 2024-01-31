/**
 * Q1. Top 5 popular movies
 * 
 * Find the movie titles, taglines, and directors for the top 5 popular movies.

Return the columns 'original_title', 'tagline', and 'director'.

 * 
**/

SELECT original_title,tagline,director
FROM movies
ORDER BY popularity DESC
LIMIT 5;
/**
Q2. Low Fat & Recyclable Products
Write a query to find the ids of products that are both low-fat and recyclable.
Return the result table ordered by product_id in ascending order.
**/
SELECT product_id
FROM products
WHERE low_fats = "Y" AND recyclable = "Y"
ORDER BY product_id;

/**
Q3. Germany
Write a query to fetch customer details like customerName, 
phone, addressLine1, city, state, and postalCode who are not from Germany.

Return the result ordered by customerName in ascending order.
**/
SELECT customerName,phone,addressLine1,city,state,postalCode
FROM customers
WHERE country NOT LIKE "Germany" ORDER BY customerName;

/**
Q4. Patients With a Condition
Write an SQL query to report the patient_id who have Type I Diabetes. 
Type I Diabetes always starts with DIAB1 prefix.

Return the results ordered by patient_id in ascending order.
**/
SELECT patient_id,conditions FROM patients
WHERE conditions LIKE "DIAB1%" OR conditions LIKE "%DIAB1%"
ORDER BY patient_id;
########## HOME WORK###########
/**
 * HOME WORK
Q2. Problems that are low quality
Write a query to report the IDs of the low-quality problems.

A problem is low-quality if the like percentage of the problem 
(the number of likes divided by the total number of votes) is strictly less 
than 60%.

Return the result table ordered by problem_id in ascending order.
**/


SELECT product_id
FROM problems
WHERE (likes/(likes+dislikes))*100 < 60
ORDER BY product_id;

/**
Q5. Product Sales Analysis V
Write an SQL query that reports the spending of each user.

Return the resulting table ordered by spending in descending order. 
In case of a tie, order them by user_id in ascending order
**/

SELECT S.user_id,SUM(P.price*S.quantity) as spending
FROM sales as S 
JOIN product as P  
ON S.product_id = P.product_id
GROUP BY S.user_id
ORDER BY spending DESC,user_id ASC;

/**
Q3. Human Resources
Write a query to find details of the employees who work in the 
'Human Resources' department.

Return the columns 'employee_id', 'department_id', 'first_name', 'last_name', 'job_id', and 'department_name'.
Return the result ordered by employee_id in ascending order.
**/
SELECT e.emplyee_id,e.department_id,e.first_name,e.last_name,e.job_id,d.department_name
FROM employees as e 
JOIN departments as d
ON e.department_id = d.department_id
WHERE d.department_name = "Human Resources";
/**
Q6. Three months
Display the details of those employees who were hired between 
the given date '1998-01-01' and three months after from the given date.

Return the columns 'employee_id', 'first_name', 'last_name', 'salary', 'department_name', 'hire_date', 'city'.
Return the result ordered by employee_id in ascending order.
**/
SELECT E.employee_id, E.first_name, E.last_name, E.salary, 
        D.department_name, E.hire_date, L.city
FROM employees as E 
JOIN departments as D   
ON E.department_id = D.department_id
JOIN locations as L
ON D.location_id = L.location_id
WHERE E.hire_date BETWEEN "1998-01-01" AND DATE_ADD("1998-01-01",INTERVAL 90 DAY)
ORDER BY E.employee_id;
/**
Q4. Article Views II
Write a query to find all the people who viewed more 
than one article on the same date.

Save the viewer_id as the id.
Return the result sorted by id in ascending order.
**/

SELECT DISTINCT v1.viewer_id AS id
FROM views AS v1
JOIN views AS v2 ON v1.viewer_id = v2.viewer_id
WHERE v1.view_date = v2.view_date AND v1.article_id <> v2.article_id
ORDER BY id;

/**
Q1. Cities starting with vowels
Write a query to get the list of city names starting with vowels (i.e., a, e, i, o, or u) from station table.

The result should not contain duplicate values.

Return the result table ordered by city in ascending order.
**/
SELECT DISTINCT city 
FROM station
WHERE city LIKE "a%" OR city LIKE "e%" OR city LIKE "i%" OR city LIKE "o%" OR city LIKE "u%" 
ORDER BY city;
##### optimized soliuiton

SELECT DISTINCT(city)
FROM station
WHERE SUBSTR(city, 1, 1) IN ('A', 'E' , 'I', 'O', 'U')
ORDER BY city;
/**
Q7. Job like sales
Display the details of the employees who had job titles like 'sales'
 in the past and the min_salary is greater than or equal to 6000.

Return the columns 'employee_id', 'department_name', 'job_id', 'job_title', and 'min_salary'.
Return the employee's current information for the columns 'employee_id', 
    and 'department_name'.
Return the employee's past information for the columns 'job_id', '
    job_title', and 'min_salary'.
Return the output ordered by employee_id and min_salary in ascending order.
**/

SELECT e.employee_id,d.department_name,jh.job_id,j.job_title,j.min_salary
FROM employees as e  
JOIN departments as d
ON e.department_id = d.department_id
JOIN job_history as jh  
ON e.employee_id = jh.employee_id AND d.department_id = jh.department_id
JOIN jobs as j  
ON jh.job_id = j.job_id
WHERE j.min_salary >= 6000 AND j.job_title LIKE "Sales %"
ORDER BY e.employee_id ASC,j.min_salary ASC;

/**
Q4. Department in US
Display the details of those employees who have a manager working in the 
department that is US (i.e., country_id) based.

Note:

Return the columns employee_id, first_name, and last_name.
Return the result ordered by employee_id in ascending order.
**/
select e1.employee_id, e1.first_name, e1.last_name
    from employees e1
    join employees e2
        on e1.manager_id = e2.employee_id
    join departments d 
        on d.department_id = e2.department_id
    join locations l
        on d.location_id = l.location_id
    where l.country_id = 'US'
    order by e1.employee_id;
/**
Q2. Same manager
Extract the details of the employees who work under the same manager.

Return the details along with the manager's full name 
(first name, last name separated by space) as 'Manager' 
and the employee's full name (first name, last name separated by space) 
as 'Employee'.

Order the output based on manager_id and 'Employee' in ascending order.

Return the columns 'manager_id', 'Manager', 'Employee'.
Use the employees table.
**/
SELECT e1.manager_id,CONCAT(e2.first_name," ",e2.last_name) as Manager,
CONCAT(e1.first_name," ",e1.last_name) as Employee
FROM employees as e1
JOIN employees as e2
ON e1.manager_id = e2.employee_id
ORDER BY e1.manager_id ASC,Employee;
/**
Q1. Joined first
Display the details of the employees who joined the 
company before their managers joined the company.

Return the columns 'employee_id', 'first_name', and 'last_name'.
Return the result ordered by employee_id in ascending order.
**/

SELECT e1.employee_id,e1.first_name,e1.last_name
FROM employees as e1
JOIN employees as e2
ON e1.manager_id = e2.employee_id
WHERE e1.hire_date < e2.hire_date
ORDER BY e1.employee_id ;