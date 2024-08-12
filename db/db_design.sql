--PART 2
--Part 2 of the assignment is to build the database, insert all data, and write SQL queries to answer use case questions.
--We will be using DBT to insert our initial seed data, and write SQL statement to transform it.
--Instead of a database, we will use Snowflake to store the data.

--Part 2 Total Points: 20

--After building and populating your database, you will write SQL queries to answer the questions below.
--Include your SQL code and results in your submitted file.

--1) (1 PT) Which courses are currently included (active) in the program? Include the course mnemonic and course name for each.
SELECT NAME, mnemonic from Courses WHERE ACTIVE = 'TRUE';

--2) (1 PT) Which courses were included in the program, but are no longer active? Include the course mnemonic and course name for each.
SELECT NAME, mnemonic from Courses WHERE ACTIVE = 'FALSE';

--3) (1 PT) Which instructors are not current employees?
SELECT instructors from Instructors WHERE ACTIVE = 'FALSE';

--4) (1 PT) For each course (active and inactive), how many learning outcomes are there?
SELECT COUNT(*) AS course_count FROM Courses;

--5) (2 PTS) Are there any courses with no learning outcomes? If so, provide their mnemonics and names.
SELECT mnemonics, name FROM Courses wHERE description_short = NULL;

--6) (2 PTS) Which courses include SQL as a learning outcome? Include the learning outcome descriptions, course mnemonics, and course names in your solution.
SELECT description_short,mnemonics,name FROM Courses WHERE description_short LIKE '%SQL%';

--7) (1 PT) Who taught course ds5100 in Summer 2021?
SELECT instructor FROM Course_Assignment WHERE Term = 'SUMMER2021' AND = mnemonic 'ds5100';

--8) (1 PT) Which instructors taught in Fall 2021? Order their names alphabetically, making sure the names are unique.
SELECT instructor FROM Course_Assignment WHERE Term = 'FALL2021' ORDER BY instructor ASC;

--9) (1 PT) How many courses did each instructor teach in each term? Order your results by term and then instructor.
SELECT
    Term,
    Instructor,
    COUNT(Course) AS course_count
FROM
    Course_Assignment
GROUP BY
    Term,
    Instructor
ORDER BY
    Term ASC,
    Instructor ASC;

--10a) (2 PTS) Which courses had more than one instructor for the same term? Provide the mnemonic and term for each. Note this occurs in courses with multiple sections.

Copy code
SELECT
    Course,
    Term,
    COUNT(Instructor) AS instructor_count
FROM
    Course_Assignment
GROUP BY
    Course,
    Term
HAVING
    COUNT(Instructor) > 1;

--10b) (1 PT) For courses with multiple sections, provide the term, course mnemonic, and instructor name for each. Hint: You can use your result from 10a in a subquery or WITH clause.
SELECT
    ca.Term,
    ca.Course,
    ca.Instructor
FROM
    Course_Assignment ca
WHERE
    ca.Course IN (
        SELECT Course
        FROM Course_Assignment
        GROUP BY Course, Term
        HAVING COUNT(*) > 1
    )
ORDER BY
    ca.Term ASC,
    ca.Course ASC,
    ca.Instructor ASC;


--Note: Question 10 is good preparation for SQL interview questions.
