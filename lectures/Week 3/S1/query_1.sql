INSERT INTO users (name,email,password) VALUES ('John Doe','j@j.com','123456');
INSERT INTO users (name,email,password) VALUES ('Jane Doe','d@d.com','123456');
INSERT INTO users (name,email,password) VALUES ('Jack Doe','b@b.com','123456');
INSERT INTO users (name,email,password) VALUES ('James Doe','a@a.com','123456');
SELECT * FROM users;
SELECT id,name FROM users;

SELECT * FROM users WHERE id = 3;


UPDATE users SET name = 'new name', email = 'n@n.com', password = '123456' WHERE id = 2;
-- SET SQL_SAFE_UPDATES = 1;
DELETE FROM users WHERE id = 5;

INSERT INTO posts (content,user_id) VALUES ('Hello World',1), ('This is test',2), ('This is test also',3);
INSERT INTO posts (content,user_id) VALUES ('This is test',2);
SELECT * FROM posts;

SELECT * FROM users JOIN posts ON users.id = posts.user_id;
SELECT * FROM users INNER JOIN posts ON users.id = posts.user_id;
SELECT * FROM users LEFT JOIN posts ON users.id = posts.user_id;
SELECT * FROM posts LEFT JOIN users ON users.id = posts.user_id;
SELECT * FROM users RIGHT JOIN posts ON users.id = posts.user_id;

SELECT * FROM posts JOIN users ON posts.user_id = users.id WHERE users.id = 7;


INSERT INTO likes (user_id, post_id) VALUES (1,1), (1,2), (1,3), (2,1), (2,3);

SELECT * FROM likes;


SELECT posts.content, users.name FROM posts
JOIN likes ON posts.id = likes.post_id
JOIN users ON users.id = likes.user_id
WHERE posts.id = 3;


-- GET Number of likes for posts

SELECT posts.content, COUNT(*) AS number_of_likes FROM likes
LEFT JOIN posts ON posts.id = likes.post_id
GROUP BY content;