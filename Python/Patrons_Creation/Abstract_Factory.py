import tkinter as tk 
from abc import ABC, abstractmethod

class ButtonWidget(ABC):
    @abstractmethod
    def get_widget(self):
        pass
    
class WinButtonWidget(ButtonWidget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Button(master, text="Click Me!",  **kwargs)

    def get_widget(self):
        return self.widget
    
class MacButtonWidget(ButtonWidget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Button(master, text="Click Me Please!", **kwargs)

    def get_widget(self):
        return self.widget
    

class LabelWidget(ABC):
    @abstractmethod
    def get_widget(self):
        pass

class WinLabelWidget(LabelWidget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Label(master, text="Hello, Windows 11", **kwargs)

    def get_widget(self):
        return self.widget
    
class MacLabelWidget(LabelWidget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Label(master, text="Hello, MacOs Montery", **kwargs)

    def get_widget(self):
        return self.widget