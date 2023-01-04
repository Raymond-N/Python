SELECT name, id FROM names;

INSERT INTO names (name) VALUES ('Raymond Natividad');

INSERT INTO names (name) VALUES ('Karina Moreno'), ('Mila Natividad'), ('Anthony Villacis');

UPDATE names SET name = 'LeBron James' WHERE id = 2;

DELETE FROM names WHERE id = 4;