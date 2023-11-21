-- JOINS

SELECT * from twitter.users;
SELECT * from twitter.tweets;
SELECT * from twitter.follows;
SELECT * from twitter.faves;

-- get all the users tha made tweets
SELECT tweet, first_name FROM users
JOIN tweets
ON tweets.user_id = users.id;

-- get all the users whether they made tweets or not
SELECT tweet, first_name FROM users
LEFT JOIN tweets
ON tweets.user_id = users.id;

-- get all the tweets a users has made with known id
SELECT * FROM users
LEFT JOIN tweets
ON tweets.user_id = users.id
WHERE users.id = 1;
-- get all the tweets the first users has made (unknown id)
SELECT * FROM users
LEFT JOIN tweets
ON tweets.user_id = users.id
WHERE users.id = (SELECT id FROM users
LIMIT 1)
ORDER BY tweets.created_at DESC
LIMIT 1
OFFSET 1;

-- many to many
-- get a user and the tweets they favs
SELECT * FROM users
LEFT JOIN faves
ON faves.user_id = users.id
LEFT JOIN tweets
ON tweets.id = faves.tweet_id;




