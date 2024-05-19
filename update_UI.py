from gui_factory import GUIFactory
from calc import Calculations
from dictionaries import Dictionaries


class Update:
    def __init__(self, master, gui_manager):
        self.remaining_points = 27
        self.master = master
        self.factory = GUIFactory()
        self.dictionaries = Dictionaries()
        self.calc = Calculations()
        self.gui_manager = gui_manager

    def update_armour_dropdown(self, *args):
        self.gui_manager.remove_label("Armour:")
        self.gui_manager.remove_entry("Armour:")

        armour_type = self.gui_manager.entries["Armour Type:"].cget("text")
        armours = self.dictionaries.ARMOUR_TYPES.get(armour_type, ["None"])
        self.gui_manager.row_count = 2
        self.gui_manager.column_count = 0
        self.gui_manager.create_dropdown_entry("Armour:", armours, command=self.update_armour_class_value)

        self.calc.calculate_armour_class(self.gui_manager)
        self.update_armour_class_value()
        self.gui_manager.row_count = 1
        self.gui_manager.column_count = 2

    def update_armour_class_value(self, *args):
        character_ac = self.calc.calculate_armour_class(self.gui_manager)

        self.gui_manager.labels["Armor Class Value:"].config(text=str(character_ac))

    def update_counter(self, *args):
        selected_race = self.gui_manager.entries["Race:"].cget("text")
        race_modifiers = self.dictionaries.RACE_STAT_MODIFIERS.get(selected_race,
                                                                   {})
        selected_values = [int(self.gui_manager.entries[stat].cget("text")) for stat in
                           ["Strength:", "Dexterity:", "Constitution:",
                            "Intelligence:", "Wisdom:", "Charisma:"]]
        total_cost = 0
        stats_cost = self.dictionaries.POINT_COSTS.copy()
        for value in selected_values:
            total_cost += stats_cost[value]
        self.remaining_points = 27 - total_cost

        if "Remaining Points:" not in self.gui_manager.labels:
            self.gui_manager.labels["Remaining Points:"] = self.factory.create_label(self.master, "")
            self.gui_manager.labels["Remaining Points:"].grid(row=1, column=2)

        self.gui_manager.labels["Remaining Points:"].config(text=f"Remaining Points: {self.remaining_points}")

        self.update_modified_labels(selected_values, race_modifiers)

    def update_modified_labels(self, selected_values, race_modifiers):
        for stat in ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]:
            modified_stat = selected_values[
                ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"].index(stat)]
            modifier = race_modifiers.get(stat, 0)
            modified_stat += modifier

            label_key = "Modified " + stat
            label = self.gui_manager.labels[label_key]
            label.config(text=f"Modified {stat} {modified_stat}")

    def get_skill_proficiencies(self):
        skill_proficiencies_text = self.gui_manager.labels["Skill Proficiencies:"].cget("text")
        skills = skill_proficiencies_text.replace("Skill Proficiencies: ", "").split(", ")
        return skills

    def update_skill_labels(self, skill_labels):
        selected_values = [int(self.gui_manager.labels["Modified " + stat].cget("text").split(": ")[1]) for stat in
                           ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]]
        skill_proficiencies = self.get_skill_proficiencies()

        for skill, label in skill_labels.items():
            stat = self.dictionaries.CLASS_SKILL[skill]

            stat_index = ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"].index(stat)
            stat_modifier = self.calc.calculate_modifier(selected_values[stat_index])

            proficiency_bonus = 2 if skill in skill_proficiencies else 0

            total_modifier = stat_modifier + proficiency_bonus

            label.config(text=f"{skill}: {'+' if total_modifier >= 0 else ''}{total_modifier}")

    def update_proficiencies(self, *args):
        for label_key in ["Skill Proficiencies:", "Tool Proficiencies:"]:
            self.gui_manager.remove_label(f"{label_key}")

        selected_background = self.gui_manager.entries["Background:"].cget("text")
        selected_class = self.gui_manager.entries["Class:"].cget("text")

        skill_proficiencies = []
        tool_proficiencies = []

        background_proficiencies = self.dictionaries.BACKGROUND_PROFICIENCIES

        class_proficiencies = self.dictionaries.CLASS_PROFICIENCY

        if selected_background in background_proficiencies:
            skill_proficiencies.extend(background_proficiencies[selected_background]["Skill Proficiencies"])
            tool_proficiencies.extend(background_proficiencies[selected_background]["Tool Proficiencies"])

        if selected_class in class_proficiencies:
            skill_proficiencies.extend(class_proficiencies[selected_class]["Skill Proficiencies"])
            tool_proficiencies.extend(class_proficiencies[selected_class]["Tool Proficiencies"])

        row = self.gui_manager.row_count
        column = self.gui_manager.column_count

        self.gui_manager.labels["Skill Proficiencies:"] = self.factory.create_label(self.master,
                                                                                    "Skill Proficiencies: " + ", ".join(
                                                                                        skill_proficiencies))
        self.gui_manager.labels["Skill Proficiencies:"].grid(row=row, column=column, sticky='w')

        self.gui_manager.labels["Tool Proficiencies:"] = self.factory.create_label(self.master,
                                                                                   "Tool Proficiencies: " + ", ".join(
                                                                                       tool_proficiencies))
        self.gui_manager.labels["Tool Proficiencies:"].grid(row=row + 1, column=column, sticky='w')

    def update_skills_prof(self, skill_labels):
        self.update_proficiencies()
        self.update_skill_labels(skill_labels)

    def update_skills_prof_race(self, skill_labels):
        self.update_counter()
        self.update_proficiencies()
        self.update_skill_labels(skill_labels)
        self.update_armour_class_value()

    def update_armour_dropdown_for_fourth(self, selected_armour_type=None, selected_armour=None):
        self.gui_manager.remove_label("Armour:")
        self.gui_manager.remove_entry("Armour:")

        if selected_armour_type is None:
            selected_armour_type = self.gui_manager.entries["Armour Type:"].cget("text")

        armours = self.dictionaries.ARMOUR_TYPES.get(selected_armour_type, ["None"])
        self.gui_manager.row_count = 5
        self.gui_manager.column_count = 0
        self.gui_manager.create_dropdown_entry("Armour:", armours, default_value=selected_armour, command=self.update_armour_class_value)

        self.calc.calculate_armour_class(self.gui_manager)

    def update_armour_dropdown_conj_func(self, selected_armour_type=None, selected_armour=None):
        self.update_armour_dropdown_for_fourth(selected_armour_type, selected_armour)
        self.update_armour_class_value()
        self.gui_manager.row_count = 6
        self.gui_manager.column_count = 2

    def update_based_on_stats_before_mod(self, skill_labels=None):
        self.update_counter()
        self.update_skill_labels(skill_labels)
        self.update_armour_class_value()
