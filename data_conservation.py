import json
from character_builder import CharacterBuilder, Character


class DataConservation:
    def __init__(self, gui_manager):
        self.character_builder = CharacterBuilder()
        self.gui_manager = gui_manager

    def save_data(self):
        gui_manager = self.gui_manager
        character_builder = self.character_builder

        # Populate existing CharacterBuilder instance with entered data
        self.set_basic_data(character_builder, gui_manager)
        self.set_additional_data(character_builder, gui_manager)

        self.save_to_file("character_sheet.json")

    def set_basic_data(self, character_builder, gui_manager):
        character_builder.set_name(gui_manager.entries["Name:"].get())
        character_builder.set_race(gui_manager.entries["Race:"].cget("text"))
        character_builder.set_character_class(gui_manager.entries["Class:"].cget("text"))

        modified_stats = {}
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat_value = int(gui_manager.labels["Modified " + stat].cget("text").split(": ")[1])
            modified_stats[stat] = modified_stat_value
        character_builder.set_stats(modified_stats)

        character_builder.set_level(int(gui_manager.entries["Level:"].cget("text")))

    def set_additional_data(self, character_builder, gui_manager):
        character_builder.set_background(gui_manager.entries["Background:"].cget("text"))
        character_builder.set_armour_type(gui_manager.entries["Armour Type:"].cget("text"))
        print(f"Armour Type from gui: {gui_manager.entries["Armour Type:"].cget("text")}")
        print(f"Armour Type from builder: {character_builder.armour_type}")
        character_builder.set_armour(gui_manager.entries["Armour:"].cget("text"))
        print(f"Armour from gui: {gui_manager.entries["Armour:"].cget("text")}")
        print(f"Armour from builder: {character_builder.armour}")
        character_builder.set_inventory(gui_manager.entries["Armour:"].cget("text"))
        character_builder.set_armor_class(gui_manager.labels["Armor Class Value:"].cget("text"))
        character_builder.set_skill_proficiencies(gui_manager.labels["Skill Proficiencies:"].cget("text"))
        character_builder.set_tool_proficiencies(gui_manager.labels["Tool Proficiencies:"].cget("text"))
        if "Hit Points value" in gui_manager.entries:
            hit_points_text = gui_manager.entries["Hit Points value"].get()
            print(f"Hit points value from entries: {hit_points_text}")
        else:
            print("entry 'Hit points value' was not found")
            hit_points_text = gui_manager.labels["Hit Points value"].cget("text")
        hit_points_value = hit_points_text.strip()  # No need to replace here, just strip any extra spaces
        character_builder.set_hit_points(hit_points_value)
        print(f"Hit Points from GUI: {hit_points_text}")
        character_builder.set_hit_points(hit_points_text)
        print(f"Hit Points from character_builder: {character_builder.hit_points}")
        character_builder.set_history(gui_manager.entries["History:"].get())
        print(f"History from character_builder: {character_builder.history}")
        character_builder.set_hair(gui_manager.entries["Hair:"].get())
        character_builder.set_skin(gui_manager.entries["Skin:"].get())
        character_builder.set_eyes(gui_manager.entries["Eyes:"].get())
        character_builder.set_height(gui_manager.entries["Height:"].get())
        character_builder.set_weight(gui_manager.entries["Age:"].get())
        character_builder.set_age(gui_manager.entries["Skin:"].get())
        character_builder.set_gender(gui_manager.entries["Gender:"].get())
        character_builder.set_alignment(gui_manager.entries["Alignment:"].get())

    def save_to_file(self, filename):
        # Save updated CharacterBuilder instance to a JSON file
        with open(filename, 'w') as file:
            json.dump(self.character_builder.__dict__, file)

    def load_character_from_json(self, json_file, character_builder):
        with open(json_file, 'r') as file:
            data = json.load(file)

        setters = {
            'name': character_builder.set_name,
            'race': character_builder.set_race,
            'character_class': character_builder.set_character_class,
            'stats': character_builder.set_stats,
            'level': character_builder.set_level,
            'hit_points': character_builder.set_hit_points,
            'skill_proficiencies': character_builder.set_skill_proficiencies,
            'tool_proficiencies': character_builder.set_tool_proficiencies,
            'inventory': character_builder.set_inventory,
            'armor_class': character_builder.set_armor_class,
            'background': character_builder.set_background,
            'history': character_builder.set_history,
            'hair': character_builder.set_hair,
            'skin': character_builder.set_skin,
            'eyes': character_builder.set_eyes,
            'height': character_builder.set_height,
            'weight': character_builder.set_weight,
            'age': character_builder.set_age,
            'gender': character_builder.set_gender,
            'alignment': character_builder.set_alignment,
            'armour_type': character_builder.set_armour_type,
            'armour': character_builder.set_armour
        }

        for key, setter in setters.items():
            setter(data.get(key))

        modified_stats = {}
        for stat in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            modified_stat_value = int(data["stats"][stat])
            modified_stats[stat] = modified_stat_value
        character_builder.set_stats(modified_stats)
        print(character_builder.stats)
