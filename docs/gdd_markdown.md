# Game Design Document - Elemental Heroes

## 📖 Indice

1. [Panoramica del Gioco](#1-panoramica-del-gioco)
2. [Meccaniche Principali](#2-meccaniche-principali)
3. [Personaggi Base](#3-personaggi-base)
4. [Sistema Economico](#4-sistema-economico)
5. [Modalità di Gioco](#5-modalità-di-gioco)
6. [Sistemi di Progressione](#6-sistemi-di-progressione)
7. [Monetizzazione](#7-monetizzazione)
8. [Specifiche Tecniche](#8-specifiche-tecniche)
9. [Timeline di Sviluppo](#9-timeline-di-sviluppo)
10. [Metriche di Successo](#10-metriche-di-successo)

---

## 1. Panoramica del Gioco

### 🎮 Informazioni Base
- **Titolo**: Elemental Heroes
- **Genere**: Gacha RPG Mobile/Browser
- **Piattaforme**: Browser (Desktop/Mobile), Future: iOS/Android
- **Target**: 13-35 anni, fan di gacha games
- **Riferimenti**: Brave Frontier, Epic Seven, Genshin Impact

### 🎯 Concept
Un RPG gacha dove i giocatori collezionano eroi elementali attraverso evocazioni, li potenziano e li usano in battaglie strategiche turn-based contro nemici e altri giocatori.

---

## 2. Meccaniche Principali

### 🎲 Sistema Gacha

#### Valute
- **💎 Gems** (Premium) - Acquistabili con denaro reale
- **🪙 Coins** (Base) - Ottenibili tramite gameplay
- **🎫 Tickets** (Speciali) - Reward da eventi

#### Probabilità Standard
| Rarità | Probabilità | Icona |
|--------|-------------|-------|
| 5 ⭐ | 3% | ⭐⭐⭐⭐⭐ |
| 4 ⭐ | 12% | ⭐⭐⭐⭐ |
| 3 ⭐ | 85% | ⭐⭐⭐ |

#### Sistema Pity
- **Garanzia 4⭐**: ogni 10 pull
- **Garanzia 5⭐**: ogni 90 pull
- **Featured Rate-Up**: 50% quando si ottiene 5⭐

#### Costi Pull
- **Single Pull**: 150 gems
- **10x Pull**: 1500 gems
- **Daily Discount**: 100 gems (1 volta/giorno)

### ⚔️ Sistema di Battaglia

#### Formato
- **Turn-based 5v5**
- **Ordine**: Determinato dalla velocità (SPD)
- **Azioni**: Attack, Skill, Guard

#### Elementi e Vantaggi
```
🔥 Fire → 🌱 Earth → ⚡ Thunder → 💧 Water → 🔥 Fire
🌟 Light ↔ 🌑 Dark (danno reciproco aumentato)
```

#### Statistiche Base
- **HP**: Punti vita
- **ATK**: Danno fisico/magico
- **DEF**: Resistenza ai danni
- **SPD**: Velocità di attacco

### 📈 Progressione Personaggi

#### Livelli
- **Livello Max**: 100
- **Fonti EXP**: Battaglie, materiali EXP
- **Crescita**: Stat aumentano per livello

#### Evolution
- **Percorso**: 3⭐ → 4⭐ → 5⭐ → 6⭐
- **Requisiti**: Materiali + duplicate del personaggio
- **Benefici**: Stat aumentate, nuove abilità

#### Equipment
- **4 Slot**: Weapon, Armor, Accessory, Sphere
- **Effetti**: Stat bonus, abilità speciali
- **Upgrade**: Sistema di potenziamento

---

## 3. Personaggi Base

### 🔥 Fire Heroes

#### Ignis (5⭐ - Fire Warrior)
- **Stats**: HP 8500 | ATK 3200 | DEF 2800 | SPD 180
- **Skill**: Flame Slash - Danno fire + burn 3 turni
- **Leader**: +50% ATK alle unità Fire

#### Ember (4⭐ - Fire Mage)
- **Stats**: HP 6800 | ATK 2900 | DEF 2100 | SPD 160
- **Skill**: Fireball - Danno fire ad area
- **Leader**: +30% HP alle unità Fire

#### Pyro (3⭐ - Fire Knight)
- **Stats**: HP 7200 | ATK 2400 | DEF 2600 | SPD 140
- **Skill**: Shield Bash - Danno + stun
- **Leader**: +20% DEF alle unità Fire

### 💧 Water Heroes

#### Aqua (5⭐ - Water Healer)
- **Stats**: HP 7800 | ATK 2200 | DEF 2400 | SPD 200
- **Skill**: Healing Wave - Cura team + remove debuff
- **Leader**: +50% efficacia cure

#### Tide (4⭐ - Water Archer)
- **Stats**: HP 6500 | ATK 3100 | DEF 2000 | SPD 190
- **Skill**: Hydro Arrow - Danno water + slow
- **Leader**: +30% SPD alle unità Water

#### Drop (3⭐ - Water Monk)
- **Stats**: HP 7000 | ATK 2600 | DEF 2300 | SPD 150
- **Skill**: Water Punch - Danno water + knock back
- **Leader**: +20% HP alle unità Water

### 🌱 Earth Heroes

#### Terra (5⭐ - Earth Guardian)
- **Stats**: HP 9200 | ATK 2800 | DEF 3500 | SPD 120
- **Skill**: Earth Wall - Shield team + counter
- **Leader**: +50% DEF alle unità Earth

#### Stone (4⭐ - Earth Berserker)
- **Stats**: HP 8000 | ATK 3000 | DEF 2800 | SPD 130
- **Skill**: Rock Smash - Danno earth + armor break
- **Leader**: +30% ATK alle unità Earth

#### Pebble (3⭐ - Earth Scout)
- **Stats**: HP 6800 | ATK 2700 | DEF 2200 | SPD 170
- **Skill**: Stone Throw - Danno earth + blind
- **Leader**: +20% SPD alle unità Earth

### ⚡ Thunder Heroes

#### Volt (5⭐ - Thunder Assassin)
- **Stats**: HP 7000 | ATK 3500 | DEF 2200 | SPD 220
- **Skill**: Lightning Strike - Danno thunder + paralysis
- **Leader**: +50% SPD alle unità Thunder

#### Spark (4⭐ - Thunder Mage)
- **Stats**: HP 6200 | ATK 3200 | DEF 1900 | SPD 180
- **Skill**: Chain Lightning - Danno thunder rimbalzante
- **Leader**: +30% ATK alle unità Thunder

#### Bolt (3⭐ - Thunder Lancer)
- **Stats**: HP 7500 | ATK 2800 | DEF 2400 | SPD 160
- **Skill**: Thunder Spear - Danno thunder + penetration
- **Leader**: +20% critical rate

### 🌟 Light Heroes

#### Lux (5⭐ - Light Paladin)
- **Stats**: HP 8800 | ATK 2900 | DEF 3200 | SPD 150
- **Skill**: Divine Light - Danno light + heal team
- **Leader**: +50% HP a tutte le unità

#### Shine (4⭐ - Light Priest)
- **Stats**: HP 7200 | ATK 2000 | DEF 2600 | SPD 140
- **Skill**: Purify - Remove debuff + immunity
- **Leader**: +30% DEF a tutte le unità

#### Gleam (3⭐ - Light Archer)
- **Stats**: HP 6600 | ATK 2900 | DEF 2100 | SPD 180
- **Skill**: Light Arrow - Danno light + blind
- **Leader**: +20% ACC a tutte le unità

### 🌑 Dark Heroes

#### Shadow (5⭐ - Dark Necromancer)
- **Stats**: HP 7500 | ATK 3300 | DEF 2300 | SPD 170
- **Skill**: Soul Drain - Danno dark + heal self
- **Leader**: +50% ATK alle unità Dark

#### Void (4⭐ - Dark Assassin)
- **Stats**: HP 6800 | ATK 3400 | DEF 1800 | SPD 200
- **Skill**: Shadow Step - Danno dark + evasion buff
- **Leader**: +30% SPD alle unità Dark

#### Dusk (3⭐ - Dark Warrior)
- **Stats**: HP 7800 | ATK 2700 | DEF 2500 | SPD 130
- **Skill**: Dark Slash - Danno dark + curse
- **Leader**: +20% ATK alle unità Dark

---

## 4. Sistema Economico

### 💰 Valute e Costi

#### Gems (Premium)
- **Pacchetti**: 100 gems (€1) | 500 gems (€5) | 1200 gems (€10)
- **Uso**: Gacha pulls, energy refill, inventory expansion

#### Coins (Base)
- **Fonti**: Battaglie, daily quests, vendita oggetti
- **Uso**: Equipment upgrade, skill enhancement

#### Energy
- **Massimo**: 100 punti
- **Rigenerazione**: 1 punto ogni 6 minuti
- **Costo battaglie**: 5-15 energy per stage

### 🛠️ Materiali di Upgrade

#### Evolution Materials
- **Crystals**: Fire, Water, Earth, Thunder, Light, Dark
- **Universal Crystal**: Super raro, funziona per tutti
- **Duplicates**: Copie del personaggio per evolution

#### Equipment Materials
- **Metal Ore**: Upgrade armi
- **Leather**: Upgrade armature
- **Rare Gems**: High-tier equipment

---

## 5. Modalità di Gioco

### 📚 Story Mode
- **10 Capitoli** con 10 stage ciascuno
- **Difficoltà**: Normal, Hard, Nightmare
- **Rewards**: Gems, materiali, equipment

### 🗓️ Daily Dungeons
- **Lunedì**: Materiali EXP
- **Martedì**: Materiali Evolution
- **Mercoledì**: Materiali Equipment
- **Giovedì**: Coins
- **Venerdì**: Rewards misti
- **Weekend**: Eventi speciali

### 🏟️ Arena PvP
- **Ranked battles** vs altri giocatori
- **Stagioni mensili**
- **Rewards**: Gems, equipment esclusivo, titoli

### 👥 Guild System
- **Creazione/join guild**
- **Guild battles** cooperative
- **Guild shop** con oggetti esclusivi
- **Eventi cooperativi**

---

## 6. Sistemi di Progressione

### 👤 Player Level
- **Livello max**: 150
- **Benefici**: Energy aumenta, team cost aumenta
- **Fonti EXP**: Battaglie, daily login

### 🏆 Achievement System
- **Collect X heroes**
- **Win X battles**
- **Complete story chapters**
- **Rewards**: Gems, titles, frames

### ✅ Daily/Weekly Quests

#### Daily
- Win 3 battles → 50 gems
- Complete daily dungeon → 100 gems
- Use gacha 1 time → materiali

#### Weekly
- Win 20 battles → 200 gems
- Complete all daily quests 5 times → 500 gems
- Evolve 1 character → materiali rari

---

## 7. Monetizzazione

### 🎲 Gacha System
- **Revenue primario**
- **Seasonal banners** con featured heroes
- **Step-up banners** con guaranteed rewards

### 🎫 Battle Pass
- **Free track + Premium track**
- **Durata**: 30 giorni
- **Costo**: 1000 gems
- **Rewards**: Heroes, materiali, cosmetici

### 💝 Pacchetti Speciali
- **Starter pack** (€5)
- **Monthly gem subscription** (€10)
- **Limited time offers**

---

## 8. Specifiche Tecniche

### 🖥️ Requisiti Piattaforma
- **Browser**: Chrome 80+, Firefox 75+, Safari 13+
- **Mobile**: iOS 12+, Android 8+
- **Internet**: Connessione stabile richiesta

### ⚡ Target Performance
- **Load time**: <5 secondi
- **Battle animations**: 60 FPS
- **Memory usage**: <500MB
- **Battery life**: >2 ore gameplay continuo

---

## 9. Timeline di Sviluppo

### 🚀 Phase 1 (Mesi 1-2): Core Systems
- User authentication
- Basic gacha system
- Character collection
- Simple battle system

### ⚔️ Phase 2 (Mesi 3-4): Battle & Progression
- Complete battle system
- Story mode (primi 5 capitoli)
- Evolution system
- Equipment system

### 🎮 Phase 3 (Mesi 5-6): Content & Features
- Remaining story content
- PvP arena
- Guild system
- Events system

### 🎨 Phase 4 (Mesi 7-8): Polish & Launch
- Balance testing
- Performance optimization
- Marketing preparation
- Soft launch

---

## 10. Metriche di Successo

### 📊 Engagement Metrics
- **Daily Active Users** (DAU)
- **Session length**: target 20+ minuti
- **Retention**: D1 >40% | D7 >20% | D30 >10%

### 💰 Monetization Metrics
- **Conversion rate**: >5%
- **ARPU**: >€10
- **LTV**: >€50

### 🎯 Gameplay Metrics
- **Gacha pull frequency**
- **Battle completion rate**
- **Character collection rate**
- **PvP participation rate**

---

## 📝 Note di Sviluppo

### 🔧 Stack Tecnologico
- **Frontend**: React + Redux
- **Backend**: Node.js + Express
- **Database**: MongoDB
- **Deployment**: AWS/Heroku

### 🎨 Asset Requirements
- **Character art**: 20 personaggi iniziali
- **UI elements**: Buttons, frames, backgrounds
- **Battle effects**: Skill animations, elemental effects
- **Audio**: BGM, SFX, voice lines

### 🧪 Testing Plan
- **Unit testing**: Core game mechanics
- **Integration testing**: API endpoints
- **Balance testing**: Character stats, rates
- **Performance testing**: Load times, FPS

---

**Versione**: 1.0  
**Data**: Luglio 2025  
**Prossimo Review**: Dopo Phase 1 completion