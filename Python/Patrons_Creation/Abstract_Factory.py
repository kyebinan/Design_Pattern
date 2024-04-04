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
    

class GUIFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_button(master, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def create_label(master, **kwargs):
        pass


class WinFactory(GUIFactory):

    def create_button(master, **kwargs):
        pass

    
    def create_label(master, **kwargs):
        pass


class MacFactory(GUIFactory):

    def create_button(master, **kwargs):
        pass

    
    def create_label(master, **kwargs):
        pass


class Application:
    def __init__(self, master, **kwargs):
        pass




def main():
    # root = tk.Tk()
    # root.geometry("300x200")

    # label = LabelFactory.create_widget(root, text="Hello, World!").get_widget()
    # label.pack()

    # button = ButtonFactory.create_widget(root, text="Click Me!").get_widget()
    # button.pack()

    # entry = EntryFactory.create_widget(root).get_widget()
    # entry.pack()

    # root.mainloop()
    pass

if __name__ == "__main__":
    main()