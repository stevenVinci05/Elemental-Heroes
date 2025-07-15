import sqlite3

# Connessione al database (o creazione se non esiste)
conn = sqlite3.connect("elemental_heroes.db")
cur = conn.cursor()

# Creazione tabelle
cur.executescript("""
DROP TABLE IF EXISTS heroes;

CREATE TABLE heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    element TEXT NOT NULL,
    rarity INTEGER NOT NULL,
    base_hp INTEGER,
    base_attack INTEGER,
    base_defense INTEGER,
    base_speed INTEGER,
    skill TEXT,
    leader_skill TEXT
);
""")

# Lista degli eroi da inserire
heroes = [
    # Fire
    ("Ignis", "Fire", 5, 8500, 3200, 2800, 180, "Flame Slash - Danno fire + burn 3 turni", "+50% ATK alle unità Fire"),
    ("Ember", "Fire", 4, 6800, 2900, 2100, 160, "Fireball - Danno fire ad area", "+30% HP alle unità Fire"),
    ("Pyro", "Fire", 3, 7200, 2400, 2600, 140, "Shield Bash - Danno + stun", "+20% DEF alle unità Fire"),
    # Water
    ("Aqua", "Water", 5, 7800, 2200, 2400, 200, "Healing Wave - Cura team + remove debuff", "+50% efficacia cure"),
    ("Tide", "Water", 4, 6500, 3100, 2000, 190, "Hydro Arrow - Danno water + slow", "+30% SPD alle unità Water"),
    ("Drop", "Water", 3, 7000, 2600, 2300, 150, "Water Punch - Danno water + knock back", "+20% HP alle unità Water"),
    # Earth
    ("Terra", "Earth", 5, 9200, 2800, 3500, 120, "Earth Wall - Shield team + counter", "+50% DEF alle unità Earth"),
    ("Stone", "Earth", 4, 8000, 3000, 2800, 130, "Rock Smash - Danno earth + armor break", "+30% ATK alle unità Earth"),
    ("Pebble", "Earth", 3, 6800, 2700, 2200, 170, "Stone Throw - Danno earth + blind", "+20% SPD alle unità Earth"),
    # Thunder
    ("Volt", "Thunder", 5, 7000, 3500, 2200, 220, "Lightning Strike - Danno thunder + paralysis", "+50% SPD alle unità Thunder"),
    ("Spark", "Thunder", 4, 6200, 3200, 1900, 180, "Chain Lightning - Danno thunder rimbalzante", "+30% ATK alle unità Thunder"),
    ("Bolt", "Thunder", 3, 7500, 2800, 2400, 160, "Thunder Spear - Danno thunder + penetration", "+20% critical rate"),
    # Light
    ("Lux", "Light", 5, 8800, 2900, 3200, 150, "Divine Light - Danno light + heal team", "+50% HP a tutte le unità"),
    ("Shine", "Light", 4, 7200, 2000, 2600, 140, "Purify - Remove debuff + immunity", "+30% DEF a tutte le unità"),
    ("Gleam", "Light", 3, 6600, 2900, 2100, 180, "Light Arrow - Danno light + blind", "+20% ACC a tutte le unità"),
    # Dark
    ("Shadow", "Dark", 5, 7500, 3300, 2300, 170, "Soul Drain - Danno dark + heal self", "+50% ATK alle unità Dark"),
    ("Void", "Dark", 4, 6800, 3400, 1800, 200, "Shadow Step - Danno dark + evasion buff", "+30% SPD alle unità Dark"),
    ("Dusk", "Dark", 3, 7800, 2700, 2500, 130, "Dark Slash - Danno dark + curse", "+20% ATK alle unità Dark")
]

# Inserimento eroi
cur.executemany("""
INSERT INTO heroes (name, element, rarity, base_hp, base_attack, base_defense, base_speed, skill, leader_skill)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", heroes)

# Salvataggio e chiusura
conn.commit()
conn.close()
