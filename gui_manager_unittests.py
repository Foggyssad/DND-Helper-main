import unittest
from unittest.mock import MagicMock, patch
from gui_factory import GUIFactory
import tkinter as tk
from gui_manager import GUIManager


class TestGUIManager(unittest.TestCase):

    def setUp(self):
        self.master = MagicMock()
        self.gui_manager = GUIManager(self.master)
        self.gui_manager.factory = MagicMock(spec=GUIFactory)

    def test_create_label_entry(self):
        self.gui_manager.factory.create_label.return_value = MagicMock()
        self.gui_manager.factory.create_entry.return_value = MagicMock()

        entry = self.gui_manager.create_label_entry("Test Label", "Default Text")

        self.assertIn("Test Label", self.gui_manager.labels)
        self.assertIn("Test Label", self.gui_manager.entries)
        self.gui_manager.factory.create_label.assert_called_once_with(self.master, "Test Label")
        self.gui_manager.factory.create_entry.assert_called_once_with(self.master)
        entry.insert.assert_called_once_with("end", "Default Text")
        entry.grid.assert_called_once_with(row=0, column=1, padx=5)

    def test_create_entry(self):
        self.gui_manager.factory.create_entry.return_value = MagicMock()

        entry = self.gui_manager.create_entry("Default Text")

        self.assertIn("Default Text", self.gui_manager.entries)
        self.gui_manager.factory.create_entry.assert_called_once_with(self.master, "Default Text")
        entry.grid.assert_called_once_with(row=0, column=0, sticky='w')

    def test_create_label(self):
        self.gui_manager.factory.create_label.return_value = MagicMock()

        label = self.gui_manager.create_label("Test Label")

        self.assertIn("Test Label", self.gui_manager.labels)
        self.gui_manager.factory.create_label.assert_called_once_with(self.master, "Test Label")
        label.grid.assert_called_once_with(row=0, column=0)

    def test_create_dropdown_entry(self):
        self.gui_manager.factory.create_label.return_value = MagicMock()
        self.gui_manager.factory.create_dropdown.return_value = MagicMock()
        options = ["Option 1", "Option 2"]
        command = MagicMock()

        dropdown = self.gui_manager.create_dropdown_entry("Test Dropdown", options, "Option 1", command)

        self.assertIn("Test Dropdown", self.gui_manager.labels)
        self.assertIn("Test Dropdown", self.gui_manager.entries)
        self.gui_manager.factory.create_label.assert_called_once_with(self.master, "Test Dropdown")
        self.gui_manager.factory.create_dropdown.assert_called_once()
        dropdown.grid.assert_called_once_with(row=0, column=1)
        dropdown.config.assert_called_once_with(anchor='w')

    def test_create_button(self):
        self.gui_manager.factory.create_button.return_value = MagicMock()
        command = MagicMock()

        button = self.gui_manager.create_button("Test Button", command)

        self.assertIn("Test Button", self.gui_manager.buttons)
        self.gui_manager.factory.create_button.assert_called_once_with(self.master, "Test Button", command)
        button.grid.assert_called_once_with(row=0, column=0)

    def test_add_label(self):
        label = MagicMock()
        self.gui_manager.add_label("Test Label", label)
        self.assertIn("Test Label", self.gui_manager.labels)
        self.assertEqual(self.gui_manager.labels["Test Label"], label)

    def test_add_entry(self):
        entry = MagicMock()
        self.gui_manager.add_entry("Test Entry", entry)
        self.assertIn("Test Entry", self.gui_manager.entries)
        self.assertEqual(self.gui_manager.entries["Test Entry"], entry)

    def test_add_button(self):
        button = MagicMock()
        self.gui_manager.add_button("Test Button", button)
        self.assertIn("Test Button", self.gui_manager.buttons)
        self.assertEqual(self.gui_manager.buttons["Test Button"], button)

    def test_remove_label(self):
        label = MagicMock()
        self.gui_manager.add_label("Test Label", label)
        self.gui_manager.remove_label("Test Label")
        label.grid_forget.assert_called_once()

    def test_remove_entry(self):
        entry = MagicMock()
        self.gui_manager.add_entry("Test Entry", entry)
        self.gui_manager.remove_entry("Test Entry")
        entry.grid_forget.assert_called_once()

    def test_remove_button(self):
        button = MagicMock()
        self.gui_manager.add_button("Test Button", button)
        self.gui_manager.remove_button("Test Button")
        button.grid_forget.assert_called_once()


if __name__ == '__main__':
    unittest.main()
