/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select top 1 cast(LONG_W as numeric(38,4))
from STATION
where LAT_N>38.7780
order by LAT_N asc;