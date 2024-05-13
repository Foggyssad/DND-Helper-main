from character_builder import CharacterBuilder
from data_conservation import DataConservation


class EventHandler:
    def __init__(self, master, gui_manager):
        self.gui_manager = gui_manager
        self.master = master
        self.data_conservation = DataConservation(gui_manager)
        self.character_builder = CharacterBuilder()

    def set_windows(self, first_window, second_window, third_window, fourth_window, characters_window):
        self.first_window = first_window
        self.second_window = second_window
        self.third_window = third_window
        self.fourth_window = fourth_window
        self.characters_window = characters_window

    def on_to_third_button_click(self):
        self.third_window.create_window()

    def on_next_button_click(self):
       self.second_window.create_window()

    def submit_character(self):
        self.data_conservation.save_data()
        # Update the character_builder instance in the fourth window
        if self.fourth_window:
            self.fourth_window.character_builder = self.data_conservation.character_builder

        # Create the fourth window
        if self.fourth_window:
            self.fourth_window.create_window()

    def on_save_button_click(self):
        self.data_conservation.save_data()
        self.characters_window.character_builder = self.data_conservation.character_builder
        self.characters_window.create_window()

    def on_edit_character_button_click(self):
        self.data_conservation.save_data()
        self.fourth_window.character_builder = self.data_conservation.character_builder
        print(self.fourth_window.character_builder.name)
        self.fourth_window.create_window()