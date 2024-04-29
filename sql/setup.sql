CREATE TABLE students (studentName VARCHAR(255), email VARCHAR(255), studentID INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(studentID));

INSERT INTO students (studentName, email) values ("first student", "firststudent@mydbs.ie"); 
INSERT INTO students (studentName, email) values ("second student", "secondstudent@mydbs.ie ");
SELECT * FROM students;
