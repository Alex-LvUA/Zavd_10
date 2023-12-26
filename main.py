from collections import UserDict
"""
Консольна програма записує телефонні номери у словник, реалізована з технологією класів.
"""
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW="\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value



class Phone(Field):
   def __init__(self, value):
        if int(value) and len(value)==10:
            self.value = value
        else:
            raise ValueError





class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone_s):
      try:
           self.phones.append(Phone(phone_s))
      except ValueError as e:
          if len(str(e))>0:
             print(f'{RED}{e}{YELLOW} -у номері телефона мають бути тільки цифри {RESET}')
          else:
             print(f'{RED}{phone_s}{YELLOW}  номер телефона має складатись з 10 цифр{RESET}')

    def edit_phone(self, old_phone, new_phone):
        n=0
        f=True
        for phone in self.phones:
            if phone.value==old_phone:
                f=False
                self.phones.pop(n)
                self.phones.insert(n,Phone(new_phone))
            n+=1
        if f:
            raise ValueError

    def remove_phone(self, phone):
        n = 0
        f = True
        try:
            for phon in self.phones:
                if phon.value == phone:
                    f = False
                    self.phones.pop(n)
                n += 1
            if f:
                raise ValueError
        except ValueError:
            print(f'{RED}{phone} {YELLOW}- не знайдений{RESET}')

    def find_phone(self, num_phone):
        for phone in self.phones:
            if phone.value == num_phone:
                return phone

    def __str__(self):
        return f"{BLUE}Contact name:{YELLOW} {self.name.value},{BLUE} phones:{YELLOW} {'; '.join(p.value for p in self.phones)}{RESET}"

class AddressBook(UserDict):
    # npp = 1
    # def add_record(self, record):
    #    self[AddressBook.npp]=record
    #    AddressBook.npp+=1
    def add_record(self, record):
       self[record.name.value]=record


    def get_all(self):
        for name, record in self.data.items():
            print(record)

    def find(self, name):
        for nam, rec in self.data.items():
            if rec.name.value==name:
               return rec

    def delete(self, name):
       for npp, rec in self.data.items():
            if rec.name.value == name:
                del self[npp]
                break





record1=Record("Pepo")
record1.add_phone("7889ewrwe")
record1.add_phone("7889667733")
record1.add_phone("7889662233")
record1.add_phone("788933")
record1.find_phone("7889667733")

record1.edit_phone("7889667733","7889667722")





record2=Record("Pipo")
record2.add_phone("7889940")
record2.add_phone("9044992020")
record2.add_phone("30349920202")
record2.add_phone("9044999990")

record3=Record("Papo")



book=AddressBook()
book.add_record(record1)
book.add_record(record2)
book.add_record(record3)


for name, record in book.data.items():
        print(f'---{record}')

# print("*1"*20)
# book.get_all()
# print("*2"*20)
# book.delete("Pipo")
# book.get_all()
# print("*3"*20)






print(f'знайшли {book.find("Pepo")}')

book.find("Pepo").add_phone("7889662244")
print(f'знайшли {book.find("Pepo")}')
book.find("Pepo").edit_phone("7889662244", "7889662266")

print(f'знайшли {book.find("Pepo")}')





print('_______________________________')

book.get_all()


