DROP TABLE IF EXISTS workout_log;

CREATE TABLE workout_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  duration INTEGER NOT NULL,  -- in minutes
  distance REAL NOT NULL,     -- in kilometers
  route_nickname TEXT,
  average_heart_rate INTEGER,
  max_heart_rate INTEGER
);