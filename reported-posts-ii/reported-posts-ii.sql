# Write your MySQL query statement below

with remvd_rep as (
SELECT  a.action_date, a.post_id as alL_posts,r.post_id as removed_posts 
    FROM Actions a
    LEFT JOIN Removals r
    ON a.post_id=r.post_id
    WHERE a.action = 'report' AND a.extra = 'spam'
    
), 
removed_by_all_per_day as (
    SELECT action_date,(COUNT(DISTINCT removed_posts)/COUNT(DISTINCT alL_posts)) as daily_avg 
    FROM remvd_rep 
    GROUP BY action_date
)

SELECT ROUND(sum(daily_avg)/count(action_date)*100,2) as "average_daily_percent"
FROM removed_by_all_per_day