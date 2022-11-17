-- This script creates the table unique_id on MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (UNIQUE(id INT DEFAULT 1), name VARCHAR(256));
