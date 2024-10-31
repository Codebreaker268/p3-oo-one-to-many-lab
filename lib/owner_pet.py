class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # Calls the setter to validate and set the type
        self.owner = owner  # Optional owner attribute
        Pet.all.append(self)

    def pet_type_getter(self):
        return self._pet_type

    def pet_type_setter(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise ValueError(f"{pet_type} is not a valid pet type.")

    pet_type = property(pet_type_getter, pet_type_setter)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Changed from _pet to _pets for clarity

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)  # Append the pet to the list
            pet.owner = self  # Set the owner for the pet
        else:
            raise ValueError("Only Pet instances can be added.")  # Ensure to raise the exception

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)  # Sort by pet's name
