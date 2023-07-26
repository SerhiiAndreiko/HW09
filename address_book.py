
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
    
    def get_record(self, key):
        return self.data[key]

    def remove_record(self, key):
        del self.data[key]

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        result = map(str, self.data.values())
        return "\n".join(result)
    
class Field:
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None,) -> None:
        self.name = name
        self.phones = []
        self.add_phone(phone)

    def add(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.add_phone(field)
            
    def remove(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.remove_phone(field)
   
    def add_phone(self, phone: Phone) -> None:
        if (phone):
            if (isinstance(phone, list)):
                for ph in phone:
                    if ph not in self.phones:
                        self.phones.append(ph)
            elif phone not in self.phones:
                self.phones.append(phone)
            return True
            
    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        if old_phone and new_phone:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)

    def remove_phone(self, phone: Phone) -> None:
        self.phones.remove(phone)
        return True

    def get_phones(self) -> str:
        return ";".join([ str(ph) for ph in self.phones])

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        cols = [f"name: {self.name}"]
        phone = self.phones
        if len(phone):
            cols.append(f"phones: {self.get_phones()}")    
        return ", ".join(cols)


