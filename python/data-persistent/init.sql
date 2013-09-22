--------------------------------------------------------
-- Sina Weibo snapshot SQLite database initialization --
--------------------------------------------------------

BEGIN EXCLUSIVE TRANSACTION;

-- Feed and Account can be appended and updated

CREATE TABLE IF NOT EXISTS Account (
       id INTEGER,
       screen_name TEXT,
       display_name TEXT,
       gender TEXT,
       PRIMARY KEY (id)
);

-- User relation should be completely renewed

DROP TABLE IF EXISTS Follower; 
CREATE TABLE Follower (
       id INTEGER,
       PRIMARY KEY (id),
       FOREIGN KEY (id) REFERENCES Account(id)
);

DROP TABLE IF EXISTS Following;
CREATE TABLE Following (
       id INTEGER,
       PRIMARY KEY (id),
       FOREIGN KEY (id) REFERENCES Account(id)
);

CREATE VIEW IF NOT EXISTS Friend AS
       SELECT Following.id
       FROM Following JOIN Follower
       	    ON Following.id = Follower.id;

-- user group

CREATE TABLE IF NOT EXISTS UserGroup (
       gid INTEGER,
       gname TEXT,
       description TEXT
);

CREATE TABLE IF NOT EXISTS inGroup (
       uid INTEGER REFERENCES Account(id),
       gid INTEGER REFERENCES UserGroup(gid)
);

-- concerned content

CREATE TABLE IF NOT EXISTS ConcernedContent (
       id INTEGER,
       concern_level INTEGER,
       uid INTEGER,
       content TEXT
);

CREATE TABLE IF NOT EXISTS Comment (
       uid INTEGER REFERENCES Account(id),
       cid INTEGER REFERENCES ConcernedContent(id),
       comment TEXT,
       retweet INTEGER,
       context TEXT
);

COMMIT TRANSACTION
