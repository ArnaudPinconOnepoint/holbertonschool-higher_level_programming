-- Creates the table force_name if it does not exist

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT Default 1,
    name VARCHAR(256) NOT NULL
);