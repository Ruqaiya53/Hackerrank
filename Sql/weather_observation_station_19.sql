/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CAST(SQRT(POWER((MIN(LAT_N)-MAX(LAT_N)),2)+POWER((MIN(LONG_W)-MAX(LONG_W)),2))AS NUMERIC(38,4))
FROM STATION;