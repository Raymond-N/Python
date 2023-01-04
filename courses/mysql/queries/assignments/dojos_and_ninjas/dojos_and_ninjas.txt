INSERT INTO dojos (name) VALUES ('Los Angeles'), ('Nashville'), ('Seattle');

SELECT * FROM dojos;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos;

INSERT INTO dojos (name) VALUES ('San Francisco'), ('New York'), ('Chicago');

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Raymond', 'Natividad', 29, 4), ('Karina', 'Moreno', 25, 4), ('Anthony', 'Villacis', 32, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('LeBron', 'James', 36, 5), ('Anthony', 'Davis', 30, 5), ('Russel', 'Westbrook', 32, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Mezly', 'Lopez', 29, 6), ('Gustavo', 'Moreno', 35, 6), ('Savannah', 'Tinker', 22, 6);

SELECT * FROM ninjas;

SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT * FROM ninjas WHERE dojo_id = 6;

SELECT dojo_id FROM ninjas WHERE id = 9;