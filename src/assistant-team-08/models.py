class Note:
    def __init__(self, key, text, create_date):
        self._key = key
        self._text = text
        self._create_date = create_date
        self._tags = []
    
    def __str__(self):
        str = f"Key: {self._key}  Text: {self._text}  Created: {self._create_date}"
        if len(self._tags) > 0:
            str += f"\nTags: {",".join(self._tags)}"
        return str
    
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    def add_tag(self, tag):
        self._tags.append(tag)

    def remove_tag(self, tag):
        for t in self._tags:
            if t == tag:
                self._tags.remove(t)

    def has_tag(self, tag):
        for t in self._tags:
            if t == tag:
                return True
        return False


class Record:
    def __init__(self, name: str):
        self._name = NameField(name)
        self._phones = []
        self._email = None
        self._address = None
        self._birthday = None

    def __str__(self):
        str = ""

        if self._name:
            str += f"{self._name}\n"

        if self._phones:
            for phone in self._phones:
                str += f"{phone}\n"

        if self._email:
            str += f"{self._email}\n"

        if self._address:
            str += f"{self._address}\n"

        if self._birthday:
            str += f"{self._birthday}\n"

        return str.strip()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = NameField(name)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = AddressField(address)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = EmailField(email)

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = BirthdayField(birthday)

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, value):
        self._phones = value

    def add_phone(self, phone):
        self._phones.append(PhoneField(phone))

    def remove_phone(self, phone):
        for p in self._phones:
            if p.value == phone:
                self._phones.remove(p)

    def has_phone(self, phone):
        for p in self._phones:
            if p.value == phone:
                return True
        return False


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        pass

    def __str__(self):
        return f"{self.name.capitalize()}: {self.value}"


class NameField(Field):
    def __init__(self, value):
        super().__init__("name", value)
        pass


class PhoneField(Field):
    def __init__(self, value):
        super().__init__("phone", value)
        pass


class AddressField(Field):
    def __init__(self, value):
        super().__init__("address", value)
        pass


class EmailField(Field):
    def __init__(self, value):
        super().__init__("email", value)
        pass


class BirthdayField(Field):
    def __init__(self, value):
        super().__init__("birthday", value)
        pass
