-- Total events by type
SELECT event_type, COUNT(*) 
FROM user_events
GROUP BY event_type
ORDER BY COUNT(*) DESC;

-- Daily active users
SELECT DATE(event_time) AS day, COUNT(DISTINCT user_id)
FROM user_events
GROUP BY day
ORDER BY day;

-- Events by device
SELECT metadata->>'device' AS device, COUNT(*)
FROM user_events
GROUP BY device
ORDER BY COUNT(*) DESC;

-- Purchases per user
SELECT user_id, COUNT(*) AS purchases
FROM user_events
WHERE event_type = 'purchase'
GROUP BY user_id
ORDER BY purchases DESC
LIMIT 10;
