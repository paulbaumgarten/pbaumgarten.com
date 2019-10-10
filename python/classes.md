# Classes

Classes are a core part of a computer programming philosophy known as Object Orientated Programming. This particular page currently only stands as a reference for basic usage of classes in Python, if you need an introduction into OOP you'll have to remind me to develop a proper resource for it.

```python
#### File: person.py

class Person():

    def __init__(self, given_name, family_name, email=None):
        self.given_name = given_name
        self.family_name = family_name
        if email:
            self.email = email
            self.email_provided = True
        else:
            self.email_provided = False

    def set_email(self, email):
        self.email = email
        self.email_provided = True

    def get_name(self):
        return(self.given_name+" "+self.family_name)

    def get_email(self):
        if self.email_provided:
            return self.email
        else:
            return ""
```

```python
#### File: main.py
from person import Person

me = Person("Paul", "Baumgarten", "pbaumgarten@isl.ch")

print("Your email is: " + me.get_email())
print("Your full name is: " + me.get_name())
```

Note: Naming conventions in Python:

* Class names are PascalCase
* Modules and function names are lower_case_with_underscores

