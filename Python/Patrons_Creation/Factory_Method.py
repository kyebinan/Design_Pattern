import tkinter as tk 
from abc import ABC, abstractmethod

class Widget(ABC):
    @abstractmethod
    def get_widget():
        pass

class LabelWidget(Widget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Label(master, **kwargs)

    def get_widget(self):
        return self.widget

class ButtonWidget(Widget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Button(master, **kwargs)

    def get_widget(self):
        return self.widget

class EntryWidget(Widget):
    def __init__(self, master, **kwargs):
        self.widget = tk.Entry(master, **kwargs)

    def get_widget(self):
        return self.widget
    


class WidgetFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_widget(master, **kwargs):
        pass
    
class LabelFactory(WidgetFactory):
    def create_widget(master, **kwargs):
        return LabelWidget(master, **kwargs)

class ButtonFactory(WidgetFactory):
    def create_widget(master, **kwargs):
        return ButtonWidget(master, **kwargs)

class EntryFactory(WidgetFactory):
    def create_widget(master, **kwargs):
        return EntryWidget(master, **kwargs)
        
    
def main():
    root = tk.Tk()
    root.geometry("300x200")

    label = LabelFactory.create_widget(root, text="Hello, World!").get_widget()
    label.pack()

    button = ButtonFactory.create_widget(root, text="Click Me!").get_widget()
    button.pack()

    entry = EntryFactory.create_widget(root).get_widget()
    entry.pack()

    root.mainloop()

if __name__ == "__main__":
    main()