from abc import ABC, abstractmethod
import tkinter as tk


class GUIComponent(ABC):
    @abstractmethod
    def create(self, master, **kwargs):
        pass


class LabelComponent(GUIComponent):
    def create(self, master, text=None, **kwargs):
        return tk.Label(master, text=text, **kwargs)


class EntryComponent(GUIComponent):
    def create(self, master, default_text="", **kwargs):
        entry = tk.Entry(master, **kwargs)
        entry.insert(0, default_text)
        return entry


class DropdownComponent:
    def create(self, master, options=None, command=None, variable=None, **kwargs):
        if variable is None:
            variable = tk.StringVar(master)
            variable.set(options[0])  # Set default value only if variable is not provided

        dropdown = tk.OptionMenu(master, variable, *options, command=command)
        dropdown.config(width=10)
        return dropdown


class ButtonComponent(GUIComponent):
    def create(self, master, text=None, command=None, **kwargs):
        return tk.Button(master, text=text, command=command, **kwargs)
