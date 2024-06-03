/* YOUR QUERY GOES HERE
   Example: SELECT * FROM EMPLOYEE; 
   You are given a table having the marks of one student in every test (Tests are held every day).
   You have to output the tests in which the student has improved his performance. 
   For a student to improve his performance he has to score more than the previous test.
   NOTE : The output should contain one column by the name ‘TestId’ .

Table : Tests ( {TestID, INT}, {Marks, INT} )

SELECT Tests.TestId 
FROM Tests
JOIN Tests AS prev_Test
ON prev_Test.TestId = Tests.TestId-1
WHERE  Tests.Marks > prev_Test.Marks

*/
SELECT      A.TestId
FROM        Tests A
INNER JOIN  Tests B 
ON A.TestId-1 = B.TestId AND A.Marks > B.Marks;

/*
Tests.TestID Tests.Marks T.TestID T.Marks   
101				59			100		91
102				10			101		59
103				10			102		10
104				36			103		10
*/