-- Creates the table force_name if it does not exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE Default 1,
    name VARCHAR(256) NOT NULL
);