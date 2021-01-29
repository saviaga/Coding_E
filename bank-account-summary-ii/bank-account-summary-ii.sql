# Write your MySQL query statement below



with sum_transactions AS (
    SELECT account, SUM(amount) as balance
    FROM Transactions
    GROUP BY account
    HAVING balance > 10000
)

SELECT u.name, b.balance
FROM Users u
INNER JOIN sum_transactions b
USING (account)
