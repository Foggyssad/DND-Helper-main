class Dictionaries:
    CLASS_ARMOUR_PROFICIENCY = {
        "Fighter": "All armor, shields",
        "Bard": "Light armor",
        "Druid": "Light armor, medium armor, shields",
        "Monk": "None",
        "Ranger": "Light armor. medium armor, shields",
        "Sorcerer": "None",
        "Warlock": "Light armor",
        "Wizard": "None",
        "Rogue": "Light armor",
        "Cleric": "Light armor, medium armor, shields",
        "Barbarian": "Light armor, medium armor, shields",
        "Paladin": "All armor, shields"
    }

    CLASS_SKILL = {
            "Acrobatics": "Dexterity:",
            "Animal Handling": "Wisdom:",
            "Arcana": "Intelligence:",
            "Athletics": "Strength:",
            "Deception": "Charisma:",
            "History": "Intelligence:",
            "Insight": "Wisdom:",
            "Intimidation": "Charisma:",
            "Investigation": "Intelligence:",
            "Medicine": "Wisdom:",
            "Nature": "Intelligence:",
            "Perception": "Wisdom:",
            "Performance": "Charisma:",
            "Persuasion": "Charisma:",
            "Religion": "Intelligence:",
            "Sleight of Hand": "Dexterity:",
            "Stealth": "Dexterity:",
            "Survival": "Wisdom:"
        }

    CLASS_PROFICIENCY = {
            "Barbarian": {
                "Skill Proficiencies": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception",
                                        "Survival"], "Tool Proficiencies": []},
            "Bard": {
                "Skill Proficiencies": ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History",
                                        "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception",
                                        "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth",
                                        "Survival"], "Tool Proficiencies": ["Three musical instruments"]},
            "Cleric": {"Skill Proficiencies": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
                       "Tool Proficiencies": []},
            "Druid": {
                "Skill Proficiencies": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception",
                                        "Religion", "Survival"], "Tool Proficiencies": ["Herbalism kit"]},
            "Fighter": {"Skill Proficiencies": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight",
                                                "Intimidation", "Perception", "Survival"], "Tool Proficiencies": []},
            "Monk": {"Skill Proficiencies": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
                     "Tool Proficiencies": ["One type of artisan's tools", "One musical instrument"]},
            "Paladin": {
                "Skill Proficiencies": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
                "Tool Proficiencies": []},
            "Ranger": {"Skill Proficiencies": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature",
                                               "Perception", "Stealth", "Survival"], "Tool Proficiencies": []},
            "Rogue": {"Skill Proficiencies": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation",
                                              "Investigation", "Perception", "Performance", "Persuasion",
                                              "Sleight of Hand", "Stealth"], "Tool Proficiencies": ["Thieves' Tools"]},
            "Sorcerer": {
                "Skill Proficiencies": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
                "Tool Proficiencies": []},
            "Warlock": {
                "Skill Proficiencies": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature",
                                        "Religion"], "Tool Proficiencies": []},
            "Wizard": {"Skill Proficiencies": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
                       "Tool Proficiencies": []}
        }

    BACKGROUND_PROFICIENCIES = {
        "Acolyte": {"Skill Proficiencies": ["Insight", "Religion"], "Tool Proficiencies": []},
        "Criminal": {"Skill Proficiencies": ["Deception", "Stealth"], "Tool Proficiencies": ["Thieves' Tools"]},
        "Folk Hero": {"Skill Proficiencies": ["Animal Handling", "Survival"],
                      "Tool Proficiencies": ["One type of artisan's tools", "vehicles (land)"]},
        "Haunted One": {"Skill Proficiencies": ["Choose two from Arcana, Investigation, Religion, and Survival"],
                        "Tool Proficiencies": []},
        "Noble": {"Skill Proficiencies": ["History", "Persuasion"],
                  "Tool Proficiencies": ["One type of gaming set"]},
        "Sage": {"Skill Proficiencies": ["Arcana", "History"], "Tool Proficiencies": []},
        "Soldier": {"Skill Proficiencies": ["Athletics"], "Tool Proficiencies": ["Vehicle (land)"]}
    }

    CLASS_HIT_DICE = {
        "Fighter": 10,
        "Wizard": 6,
        "Rogue": 8,
        "Cleric": 8,
        "Barbarian": 12,
        "Bard": 8,
        "Druid": 8,
        "Monk": 8,
        "Ranger": 10,
        "Sorcerer": 6,
        "Warlock": 8,
        "Paladin": 10
    }

    RACE_STAT_MODIFIERS = {
        "Aarakocra": {"Dexterity:": +2, "Wisdom:": +1},
        "Dragonborn": {"Strength:": +2, "Charisma:": +1},
        "Dwarf": {"Constitution:": +2},
        "Elf": {"Dexterity:": +2},
        "Genasi": {"Constitution:": +2},
        "Half-Orc": {"Strength:": +2, "Constitution:": +1},
        "Aasimar": {"Dexterity:": +2, "Wisdom:": +1}
    }

    ARMOUR_TYPES = {
        "Light": ["Padded", "Leather", "Studded Leather"],
        "Medium": ["Hide", "Chain Shirt", "Scale Mail", "Breastplate", "Half Plate"],
        "Heavy": ["Ring Mail", "Chain Mail", "Splint", "Plate"]
    }

    ARMOUR_AC = {
        "Padded": 11,
        "Leather": 11,
        "Studded Leather": 12,
        "Hide": 12,
        "Chain Shirt": 13,
        "Scale Mail": 14,
        "Breastplate": 14,
        "Half Plate": 15,
        "Ring Mail": 14,
        "Chain Mail": 16,
        "Splint": 17,
        "Plate": 18
    }

    POINT_COSTS = {
        8: 0,
        9: 1,
        10: 2,
        11: 3,
        12: 4,
        13: 5,
        14: 7,
        15: 9
    }
