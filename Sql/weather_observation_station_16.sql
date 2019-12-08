/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select cast(min(LAT_N)as numeric(38,4))
from STATION
where LAT_N>38.7780;