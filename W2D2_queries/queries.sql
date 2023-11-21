-- this is a comment
/* this is a multline comment */
--  =============================== students table ===============================
SELECT * FROM w2d1_erd_schema.students;
SELECT f_name, l_name FROM w2d1_erd_schema.students;

-- INSERT
/* INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value'); */
-- INSERT 1 ROW
INSERT INTO students (f_name, l_name) 
VALUES("Ahmed", NULL);
-- INSERT Multiple ROW
INSERT INTO students (f_name, l_name) 
VALUES("Ahmed", "Mohsni"),
	("Jane", "Doe"),
    ("Alaa", "BenMoussa");
    --  =============================== subject table ===============================
    
SELECT * FROM subjects;
-- create new subjects
INSERT INTO subjects(subject_name, duration)
VALUES("Intro to SQL", 2),
	("Python", 45);

-- UPDATE 
/* UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; */
UPDATE subjects 
SET subject_name = "C#", duration = 30
WHERE id =3;

-- DELETE
 -- DELETE FROM table_name WHERE condition;
-- SET SQL_SAFE_UPDATES = 0;

-- DELETE FROM subjects;

INSERT INTO subjects(subject_name, duration)
VALUES("AI", 365);
-- SELECT subject_name that has more than 5 days duration
SELECT subject_name FROM subjects
WHERE duration > 5;

-- retrieve subjects by their duration in ASC order
SELECT * FROM subjects
ORDER BY duration ASC;

-- (ERROR) DELETE the last row in the subjects 
/* MySQL does not allow a table that is being updated/deleted
in the outer query to be selected from in any sub-query of the statement. */
DELETE FROM subjects
WHERE id=( SELECT subjects.id FROM subjects
ORDER BY id DESC
LIMIT 1); 

-- (FIX) DELETE the last row in the subjects
DELETE subjects1.* FROM subjects as subjects1
LEFT JOIN (SELECT id FROM subjects ORDER BY id DESC LIMIT 1) as subjects2
ON subjects1.id = subjects2.id WHERE  subjects1.id = subjects2.id;
-- RETIEVE ALL THE ROWS
SELECT * FROM subjects;


-- OFFSET
SELECT UPPER(f_name)
FROM students
LIMIT 2
OFFSET 4;

-- COUNT students
SELECT COUNT(id) from students;

