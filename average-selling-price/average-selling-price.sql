# Write your MySQL query statement below

with product_price_sold AS (
    SELECT u.product_id, SUM(u.units) as units,SUM(u.units * p.price) as prices
    FROM UnitsSold u
    LEFT JOIN Prices p
    ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date and p.end_date 
    GROUP BY u.product_id
)

SELECT p.product_id,ROUND(SUM(p.prices/p.units),2) as average_price
FROM  product_price_sold p
GROUP BY p.product_id