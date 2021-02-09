# Write your MySQL query statement below

with friendshops_user1 AS (
    SELECT user1_id as user1, user2_id as user2 
        FROM Friendship 
    UNION ALL
    SELECT user2_id as user1, user1_id as user2
        FROM Friendship 
    ),
    
    join_friends_likes as (
    SELECT * 
        FROM friendshops_user1 f
        INNER JOIN  Likes l
        ON f.user2 = l.user_id
        WHERE f.user1 = 1                
    )

SELECT  DISTINCT(page_id)  as recommended_page
FROM  join_friends_likes
WHERE page_id NOT IN (SELECT page_id 
                    FROM Likes
                        WHERE user_id=1
                    )
    
    

