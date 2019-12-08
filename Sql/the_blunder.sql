/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CAST(ABS(ROUND(AVG(CAST(REPLACE(CAST(Salary as VarChar),"0","") as DECIMAL))-CAST(AVG(Salary) as DECIMAL),0))+1 AS INT)
FROM EMPLOYEES;