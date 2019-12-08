/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CAST(SUM(LAT_N) AS NUMERIC(38,2)), CAST(SUM(LONG_W) AS NUMERIC(38,2))
FROM STATION;
