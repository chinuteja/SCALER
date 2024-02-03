SHOW databases;
USE SAKILA;
SHOW TABLES;
SELECT * FROM actor_info;
SELECT * FROM film WHERE description IS NULL;
SELECT * FROM film WHERE description IS NOT NULL;
SELECT * FROM film ORDER BY title ASC, rental_rate DESC;
# for every film get film name language
SELECT film.title,language.name
FROM film
JOIN language
ON film.language_id = language.language_id;
# writing complete table name is diffucult
SELECT F.title,L.name
FROM film AS F
JOIN language AS L
ON F.language_id = L.language_id;
# write a query to display first and last name email of all custormes who rented a movie
SELECT DISTINCT C.first_name,C.last_name,C.email
FROM customer AS C
JOIN rental AS R
ON C.customer_id = R.customer_id;
#list of film titles along their coressponding category names for all movies
SELECT F.title,FC.film_id,FC.category_id,C.name
FROM film as F
JOIN film_category as FC
ON F.film_id = FC.film_id
JOIN category as C
ON C.category_id = FC.category_id;
# display the staff first name , last name and the store address
# of the store they are currenntly working
SELECT SF.first_name,SF.last_name,AD.address
FROM staff AS SF
JOIN store AS ST
ON SF.store_id = ST.store_id
JOIN address AS AD
ON ST.address_id = AD.address_id;