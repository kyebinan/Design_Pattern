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
        return WinButtonWidget(master, **kwargs)

    def create_label(master, **kwargs):
        return WinLabelWidget(master, **kwargs)


class MacFactory(GUIFactory):

    def create_button(master, **kwargs):
        return MacButtonWidget(master, **kwargs)

    def create_label(master, **kwargs):
        return MacLabelWidget(master, **kwargs)


class Application:
    def __init__(self, factory, **kwargs):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.factory = factory
        self.button = self.factory.create_button(self.root)
        self.label = self.factory.create_label(self.root)

    def mainloop(self):
        self.button.get_widget().pack()
        self.label.get_widget().pack()
        self.root.mainloop()




def main():
    AppWin = Application(WinFactory)
    AppWin.mainloop()
    AppMac = Application(MacFactory)
    AppMac.mainloop()
    pass

if __name__ == "__main__":
    main()