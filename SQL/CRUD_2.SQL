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

/**
 * HOME WORK
Q5. Product Sales Analysis V

Write an SQL query that reports the spending of each user.

Return the resulting table ordered by spending in descending order. 
In case of a tie, order them by user_id in ascending order.
**/

SELECT user_id,(price*quantity)  as spending
FROM sales WHERE product_id IN (
	SELECT product_id,price FROM product
)
ORDER BY spending DESC, user_id ASC;