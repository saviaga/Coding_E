# Write your MySQL query statement below

# Write your MySQL query statement below

SELECT  s.ad_id, IFNULL(ROUND((SUM(s.nclick)/(SUM(s.nclick)+SUM(s.nviews)))*100,2),0) as ctr
FROM (SELECT ad_id, action, 
    CASE WHEN action='Clicked' THEN 1 ELSE 0 END  as nclick,
    CASE WHEN action='Viewed' THEN 1 ELSE 0 END as nviews
    FROM Ads
    ) AS s
GROUP BY s.ad_id
ORDER BY  ctr DESC, s.ad_id


