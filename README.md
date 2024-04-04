# Design Patterns Practice

## SOLID Principles

SOLID is an acronym for five design principles that make software more understandable, flexible, and maintainable. Like everything in life, indiscriminately applying these principles can do more harm than good. Applying these principles to a program's architecture might make it more complicated than it needs to be. I don't believe there is any successful software in which all these principles are applied at the same time. One should try to adhere to them as much as possible but always remain pragmatic and not take everything written here as gospel truth.

### Single Responsibility Principle
A class should have only one reason to change. Try to ensure that a class is responsible for just one part of your software's functionality, and encapsulate that responsibility entirely within the class. The main goal of this principle is to reduce complexity. You don't need to invent a sophisticated concept for a program that's about 200 lines of code. Write a dozen neat methods, and everything will be fine.

### Open/Closed Principle
Classes should be open for extension but closed for modification. The main idea of this principle is to prevent creating bugs in existing code when you add new features. A class is open if you can extend it, create a subclass, or do anything else with it (add new attributes or methods, redefine the base behavior, etc.). Some programming languages allow you to limit the extension of a class using keywords, like `final`. With this, the class is no longer open. A class is closed (also called complete) if it's 100% ready to be used by other classes (its interface is clearly defined and will not change in the future).

### Liskov Substitution Principle
When you extend a class, remember that you should be able to pass objects of the subclass in place of objects of the parent class without breaking the code.

### Interface Segregation Principle
Clients should not be forced to depend on methods they do not use.

### Dependency Inversion Principle
High-level classes should not depend on low-level classes. Both should depend on abstractions. An abstraction should not depend on details. Details should depend on abstractions.

## CATALOG OF DESIGN PATTERNS

## I. CREATIONAL DESIGN PATTERNS

### 1.FACTORY METHOD
Factory Method is a creative design pattern that defines an interface to create objects in a parent class, but delegates the choice of object types to be created to subclasses.

### 2.ABSTRACT FACTORY
Abstract Factory is a design pattern that allows to create families of related objects without specifying their concrete class.

