-- Table: players
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    gems INTEGER DEFAULT 0,
    coins INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: heroes
CREATE TABLE heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    element TEXT NOT NULL,  -- es. Fire, Water, Earth, etc.
    rarity INTEGER NOT NULL,  -- es. da 1 a 5 stelle
    base_hp INTEGER,
    base_attack INTEGER,
    base_defense INTEGER,
    base_speed INTEGER
);

-- Table: player_heroes (i personaggi posseduti dai giocatori)
CREATE TABLE player_heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    hero_id INTEGER NOT NULL,
    level INTEGER DEFAULT 1,
    experience INTEGER DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (hero_id) REFERENCES heroes(id)
);

-- Table: gacha_history (log delle evocazioni)
CREATE TABLE gacha_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    hero_id INTEGER,
    pulled_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (hero_id) REFERENCES heroes(id)
);
