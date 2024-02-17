USE SAKILA;
SELECT * FROM film;
DROP INDEX idx_title ON film;
SELECT * FROM film;
CREATE INDEX idx_description on film(description(5));