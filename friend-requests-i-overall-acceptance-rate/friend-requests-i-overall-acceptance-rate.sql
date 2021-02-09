# Write your MySQL query statement below
/*
overall acceptance rate of requests = number of acceptance / the number of requests
*/



SELECT ifnull(round((count(distinct requester_id,accepter_id)/count(distinct sender_id,send_to_id)),2),0.00) as accept_rate
FROM FriendRequest,RequestAccepted
