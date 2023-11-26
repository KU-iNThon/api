CREATE TABLE `groups`(
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description TEXT NOT NULL,
    max_people INTEGER NOT NULL DEFAULT 10
) engine=InnoDB;

CREATE TABLE users(
    id VARCHAR(20) NOT NULL UNIQUE,
    nickname VARCHAR(30) NOT NULL,
    pw VARCHAR(30) NOT NULL,
    region VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) engine=InnoDB;

CREATE TABLE recruits(
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    tags TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES `groups`(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) engine=InnoDB;

CREATE TABLE participants(
    user_id VARCHAR(20) NOT NULL,
    group_id INTEGER NOT NULL,
    role VARCHAR(10) NOT NULL,
    PRIMARY KEY (group_id, user_id),
    FOREIGN KEY (group_id) REFERENCES `groups`(id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CHECK (role in ("admin", "user"))
) engine=InnoDB;

CREATE TABLE notices(
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    group_id INTEGER NOT NULL,
    user_id VARCHAR(20) NOT NULL,
    title VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES `groups`(id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE ON DELETE CASCADE
) engine=InnoDB;

CREATE TABLE tasks(
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    group_id INTEGER NOT NULL,
    title VARCHAR(20) NOT NULL,
    start_Date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    FOREIGN KEY (group_id) REFERENCES `groups`(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (group_id, id)
) engine=InnoDB;


CREATE TABLE participants_tasks(
    task_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,
    user_id VARCHAR(20) NOT NULL,
    status VARCHAR(10) NOT NULL,
    PRIMARY KEY (task_id, group_id, user_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (group_id) REFERENCES `groups`(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK (status in ("PENDING", "ACCEPTED"))
) engine=InnoDB;

CREATE TABLE comments(
    id INTEGER NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(20) NOT NULL,
    group_id INTEGER NOT NULL,
    notice_id INTEGER,
    task_id INTEGER,
    text TEXT NOT NULL,
    wrote_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (group_id) REFERENCES `groups`(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (group_id, user_id, id),
    CHECK (notice_id IS NOT NULL OR task_id IS NOT NULL)
) engine=InnoDB;
