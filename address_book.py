
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
        self.phone = phone

    def add_phone(self, phone: Phone) -> bool:
            if phone and self.phone is None:
                self.phone = phone
                return True
            return False
    # def add(self, field: Field) -> bool:
    #     if isinstance(field, Phone):
    #         return self.add_phone(field)
    #     else:
    #         return False
            
    def remove(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.remove_phone(field)
        else:
            return False
    
            
    def change_phone(self, new_phone: Phone) -> None:
        self.phone = new_phone


    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phone == other.phone
        return False

    def remove_phone(self, phone: Phone) -> None:
        if phone in self.phone:
            del self.phone[phone]
            return True
        return False
    
    def get_phone(self) -> str:
        return str(self.phone)

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        return f"name: {self.name}, phone: {self.get_phone()}"



