/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select distinct top 1 city,LEN(city) from station order by len(city);select distinct top 1 city,LEN(city) from station order by len(city) desc;