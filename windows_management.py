from character_builder import CharacterBuilder
from dictionaries import Dictionaries
from gui_factory import GUIFactory
from calc import Calculations
from update_UI import Update
from data_conservation import DataConservation


class Window:
    def __init__(self, master, gui_manager, second_window, third_window, fourth_window, character_builder):
        self.master = master
        self.factory = GUIFactory()
        self.dictionaries = Dictionaries()
        self.gui_manager = gui_manager
        self.calc = Calculations()
        self.second_window = second_window
        self.third_window = third_window
        self.fourth_window = fourth_window
        self.update = Update(master, gui_manager)
        self.character_builder = character_builder
        self.data_conservation = DataConservation(gui_manager)

    def set_event_handler(self, event_handler):
        self.events = event_handler

    def create_window(self):
        pass

    def clear_window(self):
        for key in list(self.gui_manager.labels.keys()):
            self.gui_manager.remove_label(key)

        for key in list(self.gui_manager.entries.keys()):
            self.gui_manager.remove_entry(key)

        for key in list(self.gui_manager.buttons.keys()):
            self.gui_manager.remove_button(key)

    def create_counter_label(self):
        self.counter_label = self.factory.create_label(self.master, "Remaining Points: 27")
        self.counter_label.grid(row=len(self.gui_manager.labels), columnspan=3, sticky="se")
        self.gui_manager.labels["Counter"] = self.counter_label

    def create_armor_proficiency_label(self):
        character_class = self.gui_manager.entries["Class:"].cget("text")

        armor_proficiency = self.dictionaries.CLASS_ARMOUR_PROFICIENCY.get(character_class, "None")

        armor_proficiency_label = self.gui_manager.create_label(f"Armor Proficiency: {armor_proficiency}")
        self.gui_manager.labels["Armor Proficiency"] = armor_proficiency_label

    def create_hit_points_label(self):
        hit_points = self.calc.calculate_hit_points(self.gui_manager)
        hit_points_label = self.gui_manager.create_label("Hit Points:")
        self.gui_manager.labels["Hit Points label"] = hit_points_label
        self.gui_manager.row_count = 4
        self.gui_manager.column_count = 1
        hit_points_value_label = self.gui_manager.create_label(str(hit_points))
        self.gui_manager.labels["Hit Points value"] = hit_points_value_label

    def create_to_third_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, None, self.third_window, None, None)

        self.to_third_button = self.factory.create_button(self.master, "Go to Third Window",
                                                          command=self.events.on_to_third_button_click)
        self.to_third_button.grid(row=len(self.gui_manager.labels) + 5, columnspan=3, sticky="se")
        self.gui_manager.buttons["To third"] = self.to_third_button

    def create_ac_label(self):

        self.gui_manager.column_count = 0
        self.gui_manager.create_label("Armor Class:")
        self.gui_manager.row_count = 5
        self.gui_manager.column_count = 1
        armour_class = self.gui_manager.create_label("10")
        self.gui_manager.labels["Armor Class Value:"] = armour_class

    def create_submit_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, None, self.third_window, self.fourth_window, None)

        self.submit_button = self.factory.create_button(self.master, "Submit character",
                                                        command=self.events.submit_character)
        self.submit_button.grid(row=len(self.gui_manager.labels) + 2, columnspan=2)  # Adjust row and column
        self.gui_manager.buttons["Submit"] = self.submit_button

    def create_next_button(self):
        from events import EventHandler
        self.events = EventHandler(self.master, self.gui_manager)
        self.events.set_windows(None, self.second_window, None, None, None)

        self.next_button = self.factory.create_button(self.master, "Next", command=self.events.on_next_button_click)
        self.next_button.grid(row=len(self.gui_manager.labels) + 1, columnspan=3, sticky="se")
        self.gui_manager.labels["Next"] = self.next_button

    def create_save_button(self):
        # Example function to create an "Edit" button
        save_button = self.factory.create_button(self.master, "Save", command=self.events.on_save_button_click)
        save_button.grid(row=len(self.gui_manager.labels) + 1, columnspan=2)
        self.gui_manager.buttons["Save"] = save_button


class FirstWindow(Window):
    def __init__(self, master, gui_manager, second_window, character_builder):
        super().__init__(master, gui_manager, second_window, third_window=None, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        self.gui_manager.create_label_entry("Name:")
        self.gui_manager.row_count = 0
        self.gui_manager.column_count = 2
        self.gui_manager.create_button("Import", command=self.events.on_import_button_click)
        self.gui_manager.row_count = 3
        self.gui_manager.create_button("Next", command=self.events.on_next_button_click)
        self.gui_manager.column_count = 0
        self.gui_manager.row_count = 1
        self.gui_manager.create_dropdown_entry("Race:", ["Aarakocra", "Dragonborn", "Dwarf", "Elf", "Genasi",
                                                         "Half-Orc", "Aasimar"],
                                               command=self.update.update_counter)

        self.gui_manager.create_dropdown_entry("Class:",
                                               ["Fighter", "Wizard", "Rogue", "Cleric", "Barbarian", "Bard",
                                                "Druid", "Monk", "Ranger", "Sorcerer", "Warlock", "Paladin"],
                                               command=None)
        self.gui_manager.create_dropdown_entry("Level:", [str(i) for i in range(1, 21)],
                                               command=self.update.update_counter)

        for i, stat in enumerate(["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]):
            # Create entry for original stats
            self.gui_manager.create_dropdown_entry(stat, [str(i) for i in range(8, 16)],
                                                   command=self.update.update_counter)

            modified_label = self.factory.create_label(self.master, "Modified " + stat + f"{str(8)}")
            modified_label.grid(row=i + 4, column=2)  # Start from the fourth row, to the right of original stats
            self.gui_manager.labels["Modified " + stat] = modified_label  # Add the label to the labels dictionary

        self.update.update_counter()


class SecondWindow(Window):
    def __init__(self, master, gui_manager, third_window, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=third_window, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        super().clear_window()
        self.gui_manager.reset_row_count()

        self.gui_manager.create_dropdown_entry("Background:",
                                               ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage",
                                                "Soldier"],
                                               command=self.update.update_proficiencies)  # Create background dropdown
        self.gui_manager.column_count = 2
        self.update.update_proficiencies()
        self.gui_manager.column_count = 0
        self.gui_manager.create_dropdown_entry("Armour Type:", ["Light", "Medium", "Heavy", "None"],
                                               command=self.update.update_armour_dropdown)
        self.gui_manager.row_count = 5
        super().create_ac_label()
        self.gui_manager.row_count = 2
        self.update.update_armour_dropdown()
        self.gui_manager.column_count = 0
        self.gui_manager.row_count = 3
        super().create_armor_proficiency_label()
        super().create_hit_points_label()
        super().create_to_third_button()
        self.gui_manager.column_count = 2
        self.gui_manager.row_count = 1


class ThirdWindow(Window):
    def __init__(self, master, gui_manager, fourth_window, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=None, fourth_window=fourth_window,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)

    def create_window(self):
        super().clear_window()
        self.gui_manager.reset_row_count()

        fields = [
            "History:", "Hair:", "Skin:", "Eyes:", "Height:", "Weight:", "Age:", "Gender:", "Alignment:"
        ]

        for field in fields:
            self.gui_manager.create_label_entry(field)

        super().create_submit_button()


class FourthWindow(Window):
    def __init__(self, master, gui_manager, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=None, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)
        self.character_builder = character_builder
        self.skill_labels = {}

    def create_window(self):
        super().clear_window()

        self.gui_manager.reset_row_count()

        characteristics = ["name", "race", "character_class", "hit_points", "inventory", "background", "level", "history", "hair",
                           "skin", "eyes", "height", "weight", "age", "gender", "alignment"]

        self.gui_manager.column_count = 4
        for skill in self.dictionaries.CLASS_SKILL:
            label_text = f"{skill}: +0"
            label = self.gui_manager.create_label(label_text)
            self.skill_labels[skill] = label

        self.gui_manager.reset_row_count()
        for characteristic in characteristics:
            label_text = characteristic.replace('_', ' ').title() + ":"
            default_text = getattr(self.character_builder, characteristic, "")
            if characteristic == "background":
                self.gui_manager.create_dropdown_entry("Background:", ["Acolyte", "Criminal", "Folk Hero", "Haunted One", "Noble", "Sage",
                                                "Soldier"], default_value=str(default_text), command=lambda event: self.update.update_skills_prof(self.skill_labels))
                self.gui_manager.column_count = 2
                self.update.update_proficiencies()
                self.gui_manager.column_count = 0
            elif characteristic == "race":
                self.gui_manager.create_dropdown_entry("Race:", ["Aarakocra", "Dragonborn", "Dwarf", "Elf", "Genasi",
                                                                 "Half-Orc", "Aasimar"], default_value=str(default_text),
                                                       command=lambda event: self.update.update_skills_prof_race(self.skill_labels))
            elif characteristic == "character_class":
                self.gui_manager.create_dropdown_entry("Class:", ["Fighter", "Wizard", "Rogue", "Cleric", "Barbarian", "Bard",
                                                "Druid", "Monk", "Ranger", "Sorcerer", "Warlock", "Paladin"], default_value=str(default_text),
                                                       command=lambda event: self.update.update_skills_prof(self.skill_labels))
            elif characteristic == "hit_points":
                self.gui_manager.create_label(label_text)
                self.gui_manager.row_count = 3
                self.gui_manager.column_count = 1
                entry = self.gui_manager.create_entry(default_text)
                self.gui_manager.entries["Hit Points value"] = entry
                self.gui_manager.column_count = 0
            elif characteristic == "inventory":
                default_text = self.character_builder.armour_type
                default_text_ = self.character_builder.armour

                if default_text is None:
                    default_text = "None"

                self.gui_manager.row_count = 4
                self.gui_manager.create_dropdown_entry("Armour Type:", ["Light", "Medium", "Heavy", "None"], default_value=str(default_text),
                                                       command=self.update.update_armour_dropdown_conj_func)
                self.update.update_armour_dropdown_for_fourth(default_text, default_text_)
                ac = int(self.calc.calculate_armour_class(self.gui_manager))
                self.gui_manager.create_label("Armour Class:")
                self.gui_manager.row_count = 6
                self.gui_manager.column_count = 1
                value_label = self.gui_manager.create_label(ac)
                self.gui_manager.column_count = 0
                self.gui_manager.labels["Armor Class Value:"] = value_label
            elif characteristic == "level":
                self.gui_manager.create_label(label_text)
                self.gui_manager.row_count = 8
                self.gui_manager.column_count = 1
                label = self.gui_manager.create_label(default_text)
                self.gui_manager.entries["Level:"] = label
                self.gui_manager.column_count = 0
            else:
                self.gui_manager.create_label_entry(label_text, default_text)

        self.gui_manager.reset_row_count()
        self.gui_manager.row_count = 10
        self.gui_manager.column_count = 2
        for stat in ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]:
            if self.events.tracker is False:
                modified_stat_value = int(self.gui_manager.labels["Modified " + stat].cget("text").split(": ")[1])
                label = self.gui_manager.create_label(f"Modified {stat} {modified_stat_value}")
                self.gui_manager.labels[f"Modified {stat}"] = label
            else:
                modified_stat_value = self.character_builder.stats[stat]
                label = self.gui_manager.create_label(f"Modified {stat} {modified_stat_value}")
                self.gui_manager.labels[f"Modified {stat}"] = label

        self.gui_manager.row_count = 0
        self.gui_manager.column_count = 2
        if self.events.tracker is False:
            for stat in ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]:
                self.gui_manager.create_dropdown_entry(stat, [str(i) for i in range(8, 16)],
                                                       default_value=self.gui_manager.entries[stat].cget("text"),
                                                       command=lambda event: self.update.update_based_on_stats_before_mod(self.skill_labels))
        else:
            for stat in ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]:
                if stat in self.character_builder.stats_before_mod:
                    default_value = str(
                        self.character_builder.stats_before_mod[stat])
                    self.gui_manager.create_dropdown_entry(
                        stat,
                        [str(i) for i in range(8, 16)],
                        default_value=default_value,
                        command=lambda event: self.update.update_based_on_stats_before_mod(self.skill_labels)
                    )
        self.update.update_based_on_stats_before_mod(self.skill_labels)

        self.update.update_skill_labels(self.skill_labels)
        self.gui_manager.column_count = 3
        self.gui_manager.row_count = 6
        self.gui_manager.create_label("Remaining Points:")
        self.update.update_counter()
        self.gui_manager.row_count = 6
        self.gui_manager.column_count = 2
        self.gui_manager.row_count = 17
        self.gui_manager.create_button("Save", command=self.events.on_save_button_click)
        self.gui_manager.row_count = 6


class CharactersWindow(Window):
    def __init__(self, master, gui_manager, character_builder):
        super().__init__(master, gui_manager, second_window=None, third_window=None, fourth_window=None,
                         character_builder=character_builder)
        self.factory = GUIFactory()
        self.update = Update(master, gui_manager)
        self.character_builder = character_builder

    def create_window(self):
        super().clear_window()
        self.gui_manager.reset_row_count()
        self.gui_manager.create_label("Character 1:")
        name_label = self.gui_manager.create_label("Name:")
        self.gui_manager.labels["Name"] = name_label
        self.gui_manager.column_count = 1
        self.gui_manager.row_count = 1
        self.gui_manager.create_label(self.character_builder.name)
        self.gui_manager.column_count = 0
        self.gui_manager.create_button("Edit Character", command=self.events.on_edit_character_button_click)
