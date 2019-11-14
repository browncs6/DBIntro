-- File to setup things, -- indicates a comment

CREATE TABLE pokemon(name VARCHAR(128) NOT NULL, 
height_ft DECIMAL NOT NULL, weight_lbs DECIMAL NOT NULL,
category VARCHAR(128) NOT NULL, PRIMARY KEY (name));



INSERT INTO pokemon (name, category, height_ft, weight_lbs) VALUES ('Bulbasaur', 'Seed', 2.04, 15.2);


