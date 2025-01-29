class PublicExample:
    def __init__(self):
        self.public_attribute = "I am public"

    def public_method(self):
        return "This is a public method"

obj = PublicExample()
print(obj.public_attribute)  # Accessible
print(obj.public_method())   # Accessible


class ProtectedExample:
    def __init__(self):
        self._protected_attribute = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

obj = ProtectedExample()
print(obj._protected_attribute)  # Accessible mais déconseillé
print(obj._protected_method())   # Accessible mais déconseillé