-- Displays MAX temperature of each state (Ordered by State name).

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
