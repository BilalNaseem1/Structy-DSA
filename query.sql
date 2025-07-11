-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | customer_id   | int     |
-- | name          | varchar |
-- | visited_on    | date    |
-- | amount        | int     |
-- +---------------+---------+
-- In SQL,(customer_id, visited_on) is the primary key for this table.
-- This table contains data about customer transactions in a restaurant.
-- visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
-- amount is the total paid by a customer.
 

-- You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

-- Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

-- Return the result table ordered by visited_on in ascending order.

-- The result format is in the following example.






select * from (

select visited_on
        , sum(amount) over(order by visited_on rows between 6 preceding and current row) as amount
        , round(
        avg(amount) over(order by visited_on rows between 6 preceding and current row) 
         , 2) as average_amount
         from (
            select visited_on, sum(amount) as amount
            from 'customer.csv'
            group by visited_on
         )
)
where visited_on >= (
    
select min(visited_on) + interval '6 days' as visited_on
        from 'customer.csv'
)
order by visited_on


