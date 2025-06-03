CREATE EXTENSION vector;	
CREATE TABLE famousPlacesIndia (id SERIAL PRIMARY KEY,place TEXT NOT NULL,description TEXT,vectors VECTOR(3072));
SELECT * FROM famousPlacesIndia