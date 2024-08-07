# Write your MySQL query statement below

SELECT Users.name AS name, COALESCE(SUM(Rides.distance), 0) AS travelled_distance
FROM Users
LEFT JOIN Rides ON Users.id = Rides.user_id
GROUP BY Rides.user_id
ORDER BY travelled_distance DESC, Users.name ASC