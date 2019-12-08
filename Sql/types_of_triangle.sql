/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT 
CASE WHEN A + B > C AND A+C>B AND B+C>A 
THEN CASE 
    WHEN A = B AND B = C 
    THEN 'Equilateral' 
    WHEN A = B OR B = C OR A = C 
    THEN 'Isosceles' 
    WHEN A != B OR B != C OR A != C 
    THEN 'Scalene' END ELSE 'Not A Triangle' END 
FROM TRIANGLES;