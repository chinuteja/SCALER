/**
JOINS - I
Q1. Joined first
Display the details of the employees who joined the company 
before their managers joined the company.

Return the columns 'employee_id', 'first_name', and 'last_name'.
Return the result ordered by employee_id in ascending order.
**/
SELECT employee_id, first_name, last_name
FROM employees
WHERE hire_date < (
    SELECT MAX(hire_date)
    FROM employees e2
    WHERE employees.manager_id = e2.employee_id
)
ORDER BY employee_id;
/**
Q2. Human Resources
Write a query to find details of the employees who 
work in the 'Human Resources' department.

Return the columns 'employee_id', 'department_id', 'first_name', 
'last_name', 'job_id', and 'department_name'.
Return the result ordered by employee_id in ascending order.
**/

SELECT employee_id, department_id, first_name, last_name, job_id,
  (SELECT department_name FROM departments WHERE department_id = employees.department_id) AS department_name ## getting department name from department table
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE department_name = 'Human Resources'
)
ORDER BY employee_id;
/**Q4. Department in US
Display the details of those employees who have a 
manager working in the department that is US (i.e., country_id) based.
**/
SELECT employee_id,first_name,last_name
FROM employees
WHERE manager_id IN (
SELECT manager_id FROM employees WHERE department_id IN(
    SELECT department_id FROM departments WHERE location_id IN 
        (SELECT location_id FROM locations WHERE locations = "US")
    )
)
ORDER BY employee_id;
/**
Q1. Product Sales Analysis V
Write an SQL query that reports the spending of each user.

Return the resulting table ordered by spending in descending order. 
In case of a tie, order them by user_id in ascending order.
**/
SELECT 
    user_id, 
    SUM((SELECT price FROM product WHERE product_id = sales.product_id) * quantity) AS spending
FROM sales
GROUP BY user_id
ORDER BY spending DESC, user_id ASC;
/**
Show unique first names from the patients table which only occurs 
once in the list.
For example, if two or more people are named 'John' in the 
first_name column then don't include their name in the output list. 
If only 1 person is named 'Leo' then include them in the output.
**/
SELECT DISTINCT first_name FROM patients
GROUP BY first_name
HAVING COUNT(first_name) = 1;
/**
Show patient_id and first_name from patients where their 
first_name start and ends with 's' and is at least 6 characters long.
**/
SELECT patient_id, first_name
FROM patients
WHERE 
    SUBSTRING(first_name, 1, 1) = 'S' 
    AND SUBSTRING(first_name, -1, 1) = 's' 
    AND LEN(first_name) >= 6;
SELECT
  patient_id,
  first_name
FROM patients
where
  first_name like 's%'
  and first_name like '%s'
  and len(first_name) >= 6;

/**
Show patient_id, first_name, last_name from patients whos 
diagnosis is 'Dementia'.
**/
SELECT patient_id,first_name,last_name FROM patients
WHERE patient_id IN (SELECT patient_id FROM admissions WHERE diagnosis = "Dementia");
/**
Display every patient's first_name.
Order the list by the length of each name and then by alphabetically.
**/
SELECT first_name FROM patients
GROUP BY patient_id
ORDER BY LEN(first_name) ASC,first_name;
/**
Show the total amount of male patients and the total amount of female 
patients in the patients table.
Display the two results in the same row.
**/
SELECT 
  (
    SELECT COUNT(patient_id) FROM patients 
    WHERE gender = "M"
  ) as male_count, 
  (
    SELECT COUNT(patient_id) 
    FROM patients 
    WHERE gender = "F"
  ) as female_count;
/**
Show first and last name, allergies from patients which 
have allergies to either 'Penicillin' or 'Morphine'. 
Show results ordered ascending by allergies then by first_name then 
by last_name.
**/
SELECT first_name,last_name
FROM patients
WHERE allergies = "Penicillin" or allergies = "Morphine"
ORDER BY allergies , first_name,last_name;
/**
Show patient_id, diagnosis from admissions. 
Find patients admitted multiple times for the same diagnosis.
**/
SELECT patient_id,diagnosis
FROM admissions
GROUP BY patient_id,diagnosis
HAVING COUNT(*) > 1;
/**
Show the city and the total number of patients in the city.
Order from most to least patients and then by city name ascending.
**/
SELECT city,COUNT(patient_id) AS total_number_patients
FROM patients
GROUP BY city
ORDER BY total_number_patientS ASC,city ASC;
/**
Show first name, last name and role of every person 
that is either patient or doctor.
The roles are either "Patient" or "Doctor"
**/
SELECT first_name, last_name, 'Patient' as role FROM patients
    union all
select first_name, last_name, 'Doctor' from doctors;
/**
Show all allergies ordered by popularity. Remove NULL values from query.
**/
SELECT allergies
FROM patients
WHERE allergies IS NOT NULL
GROUP BY allergies
ORDER BY COUNT(patient_id) DESC;
/**
Show all patient's first_name, last_name, and
 birth_date who were born in the 1970s decade. 
 Sort the list starting from the earliest birth_date.
**/
SELECT first_name,last_name, birth_date
FROM patients
WHERE YEAR(birth_date) >= 1970 and YEAR(birth_date) <= 1979
ORDER BY birth_date;
/**
We want to display each patient's full name in a single column. 
Their last_name in all upper letters must appear first, 
then first_name in all lower case letters. 
Separate the last_name and first_name with a comma. 
Order the list by the first_name in decending order
EX: SMITH,jane
**/
SELECT CONCAT(UPPER(last_name),",",LOWER(first_name))
FROM patients
ORDER BY first_name DESC;
/**
Show the province_id(s), sum of height; 
where the total sum of its patient's height is greater than or equal to 7,000.
**/
SELECT province_id,SUM(height)
FROM patients
GROUP BY province_id
having SUM(height) >= 7000;
/**
Show the difference between the largest weight and smallest 
weight for patients with the last name 'Maroni'
**/
SELECT max(weight)-min(weight) FROM patients WHERE last_name = 'Maroni';
/**
Show all columns for patient_id 542's most recent admission_date.
**/
select * from admissions where patient_id = 542 order by admission_date DESC LIMIT 1;
SELECT *
FROM admissions
WHERE
  patient_id = '542'
  AND admission_date = (
    SELECT MAX(admission_date)
    FROM admissions
    WHERE patient_id = '542'
  );
/**
Show patient_id, attending_doctor_id, and diagnosis for admissions 
that match one of the two criteria:
1. patient_id is an odd number and attending_doctor_id is either 1, 5, or 19.
2. attending_doctor_id contains a 2 and the length of patient_id is 3 
characters.
**/
SELECT patient_id,attending_doctor_id,diagnosis
FROM admissions WHERE 
(
     (patient_id%2 != 0 AND attending_doctor_id IN (1,5,19))
        OR (attending_doctor_id like "%2" AND LEN(patient_id)=3)
);
/**
Show first_name, last_name, and the total number
 of admissions attended for each doctor.

Every admission has been attended by a doctor.

**/
SELECT d.first_name,d.last_name,COUNT(a.patient_id) AS admissions_total
FROM admissions a 
LEFT JOIN doctors d
ON a.attending_doctor_id = d.doctor_id
GROUP BY a.attending_doctor_id; 

SELECT
  first_name,
  last_name,
  count(*)
from
  doctors p,
  admissions a
where
  a.attending_doctor_id = p.doctor_id
group by p.doctor_id;

SELECT
    (SELECT first_name FROM doctors WHERE doctor_id = a.attending_doctor_id) AS first_name,
    (SELECT last_name FROM doctors WHERE doctor_id = a.attending_doctor_id) AS last_name,
    COUNT(*) AS admission_count
FROM
    admissions a
GROUP BY
    a.attending_doctor_id;
/**
Show all of the patients grouped into weight groups.
Show the total amount of patients in each weight group.
Order the list by the weight group decending.

For example, if they weight 100 to 109 they are placed in the 100 weight group,
110-119 = 110 weight group, etc.
**/
select count(*) AS patient_count,
floor(weight/10)*100 AS weight_group
FROM patients
group by weight_group
order by weight_group desc;
/**
Show patient_id, weight, height, isObese from the patients table.

Display isObese as a boolean 0 or 1.

Obese is defined as weight(kg)/(height(m)2) >= 30.

weight is in units kg.

height is in units cm.
**/
SELECT
    patient_id,
    weight,
    height,
    CASE
        WHEN weight /power(height/100.0,2) >= 30 THEN 1
        ELSE 0
    END AS isObese
FROM
    patients;
/**
Show patient_id, first_name, last_name, and attending doctor's specialty.
Show only the patients who has a diagnosis as 'Epilepsy' and 
the doctor's first name is 'Lisa'

Check patients, admissions, and doctors tables for required information.
**/
SELECT p.patient_id,p.first_name,p.last_name,d.specialty
FROM patients p  
LEFT JOIN admissions a  
ON p.patient_id = a.patient_id
JOIN doctors d  
ON a.attending_doctor_id = d.doctor_id
WHERE a.diagnosis = 'Epilepsy' AND d.first_name = "Lisa";
/**
All patients who have gone through admissions, 
can see their medical documents on our site. 
Those patients are given a temporary password after their first admission.
 Show the patient_id and temp_password.

The password must be the following, in order:
1. patient_id
2. the numerical length of patient's last_name
3. year of patient's birth_date
**/
SELECT DISTINCT p.patient_id,CONCAT(patient_id,LEN(p.last_name),YEAR(p.birth_date)) AS temp_password
FROM patients p 
JOIN admissions a 
ON p.patient_id = a.patient_id;
/**
Each admission costs $50 for patients without insurance, 
and $10 for patients with insurance. 
All patients with an even patient_id have insurance.

Give each patient a 'Yes' if they have insurance, and a
 'No' if they don't have insurance. 
 Add up the admission_total cost for each has_insurance group.
**/
SELECT
    CASE
        WHEN patient_id % 2 = 0 THEN 'Yes'
        ELSE 'No'
    END AS has_insurance,
    SUM(
        CASE
            WHEN patient_id % 2 = 0 THEN 10
            ELSE 50
        END
    ) AS case_after_insurance
FROM
    admissions
GROUP BY
    has_insurance;
/**
Show the provinces that has more patients identified as 'M' than 'F'. 
Must only show full province_name
**/
SELECT pr.province_name
FROM patients p 
LEFT JOIN province_names pr ON p.province_id = pr.province_id
GROUP BY p.province_id
HAVING COUNT(DISTINCT CASE WHEN p.gender = 'M' THEN p.patient_id END) >
       COUNT(DISTINCT CASE WHEN p.gender = 'F' THEN p.patient_id END);
 
SELECT pr.province_name
FROM patients AS pa
  JOIN province_names AS pr ON pa.province_id = pr.province_id
GROUP BY pr.province_name
HAVING
  SUM(gender = 'M') > SUM(gender = 'F');
/**
We are looking for a specific patient. 
Pull all columns for the patient who matches the following criteria:
- First_name contains an 'r' after the first two letters.
- Identifies their gender as 'F'
- Born in February, May, or December
- Their weight would be between 60kg and 80kg
- Their patient_id is an odd number
- They are from the city 'Kingston'
**/
SELECT * FROM patients
WHERE gender = "F" AND MONTH(birth_date) IN (2,5,12)
      AND weight BETWEEN 60 AND 80 AND city = "Kingston"
      AND patient_id%2 != 0 AND first_name LIKE "__r%";


/**
Show the percent of patients that have 'M' as their gender. 
Round the answer to the nearest hundreth number and in percent form.
**/
SELECT 
   CONCAT(ROUND(SUM(gender='M') / CAST(COUNT(*) AS float), 4) * 100, '%')
FROM patients;

SELECT CONCAT(
    ROUND(
      (
        SELECT COUNT(*)
        FROM patients
        WHERE gender = 'M'
      ) / CAST(COUNT(*) as float),
      4
    ) * 100,
    '%'
  ) as percent_of_male_patients
FROM patients;
/**
For each day display the total amount of admissions on that day. 
Display the amount changed from the previous date.
**/

SELECT
 admission_date,
 COUNT(admission_date) AS admission_day,
 COUNT(admission_date) - LAG(COUNT(admission_date)) OVER(ORDER BY admission_date) AS admission_count_change 
FROM admissions
GROUP BY admission_date;
/**
Sort the province names in ascending order in such a way that the province 
'Ontario' is always on top.
**/
SELECT province_name
FROM province_names
ORDER BY
  CASE
    WHEN province_name = 'Ontario' THEN 0
    ELSE 1
  END,
province_name ASC;

select province_name
from province_names
order by
  province_name = 'Ontario' desc,
  province_name;
/**
We need a breakdown for the total amount of admissions 
each doctor has started each year. Show the doctor_id, doctor_full_name, 
specialty, year, total_admissions for that year.
**/
SELECT A.attending_doctor_id,CONCAT(D.first_name," ",D.last_name),D.specialty,
    YEAR(admission_date) AS year,COUNT(*) AS total_admissions
FROM admissions A  
JOIN doctors D 
ON A.attending_doctor_id = D.doctor_id
GROUP BY A.attending_doctor_id,year;
