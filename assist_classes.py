from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Це обов'язкове поле, воно не може бути пустим.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен складатися з рівно 10 цифр.")
        super().__init__(value)
    
    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone) 
    
    def remove_phone(self, phone_number):
        phone = Phone(phone_number)
        try:
            self.phones.remove(phone)
        except ValueError:
            return(f"Номер {phone_number} не знайдено.")

    def edit_phone(self, old_phone_number, new_phone_number):
        old_phone = Phone(old_phone_number)  
        new_phone = Phone(new_phone_number)
        for i, phone in enumerate(self.phones):
            if phone == old_phone:
                self.phones[i] = new_phone
                return
        raise ValueError(f"Не знайдено запису для {old_phone_number}")
    
    def find_phone(self, phone_number):
        phone = Phone(phone_number)
        for ph in self.phones:
            if ph == phone:
                return ph
        return None

    def __str__(self):
        return f"Ім'я контакту: {self.name.value}, Номери: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        if name in self.data:
            return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Виведення: Contact name: John, phones: 1112223333; 5555555555
print(john)  

# Видалення номеру телефону у записі John
remove = john.remove_phone("1112223333")


# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

