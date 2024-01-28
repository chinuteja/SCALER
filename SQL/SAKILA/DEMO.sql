USE SAKILA;
SHOW TABLES;
SELECT 
    *
FROM
    film_text;
SELECT film_id,title as film_name FROM film_text;

SELECT * FROM film;
SELECT DISTINCT(rating) FROM film;
SELECT DISTINCT rating, release_year FROM film;
SELECT DISTINCT rating,"hello" FROM film;
SELECT DISTINCT title, length  FROM film;
SELECT DISTINCT title, ROUND(length/60,2)  FROM film;
SELECT * FROM film WHERE rating = "PG-13";
SELECT * FROM film WHERE rating != "PG-13" OR rating = "G";
SELECT * FROM film WHERE rating IN ("G","PG","R");