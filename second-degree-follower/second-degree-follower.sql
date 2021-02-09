# Write your MySQL query statement below

SELECT a.follower as follower, COUNT(DISTINCT b.follower) as num
FROM follow a
LEFT JOIN follow b
ON a.follower = b.followee
GROUP BY a.follower
HAVING num > 0

