"""Создание класса "Телефонная книга" с атрибутами "имя", "номер телефона".
Реализовать методы для добавления и удаления контакта, изменения данных контакта,
 вывода информации о всех контактах, а также поиска контакта по имени.
"""
# импортируем класс
class Phonebook:
    contacts = []
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @classmethod
    def add_contact(cls, contact):
        cls.contacts.append(contact)

    @classmethod
    def remove_contact(cls, contact):
        if contact in cls.contacts:
            cls.contacts.remove(contact)
        else:
            print('Контакт не найден')

    def change_phone(self, new_number):
        self.number = new_number

    @classmethod
    def print_contacts(cls):
        for contact in cls.contacts:
            print(f'Имя: {contact.name}, Телефон: {contact.number}')

    @classmethod
    def search_contact(cls, name):
        result = 'Контакт не найден'
        for contact in cls.contacts:
            if contact.name == name:
               result = f'Имя: {contact.name}, Телефон: {contact.number}'
        print(result)



# создаем объекты контактов
contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact1)
Phonebook.add_contact(contact2)
Phonebook.add_contact(contact3)
#Phonebook.remove_contact(contact3)
Phonebook.print_contacts()
print("\n")
# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()
print("\n")
# ищем контакт по имени
Phonebook.search_contact("Петр Петров")

Phonebook.remove_contact(contact3)
print("\n")
Phonebook.print_contacts()