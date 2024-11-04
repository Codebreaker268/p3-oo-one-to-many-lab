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
        return [ pet for pet in Pet.all if pet.owner==self]

    def get_sorted_pets(self):
        # print(sorted(self._pets, key=lambda pet: pet.name))
        return sorted((pet for pet in Pet.all if pet.owner == self), key=lambda pet: pet.name)

jim=Owner("jim")
pet4=Pet("ted","rodent",jim)
pet3=Pet("niga","bird",jim)
pet2=Pet("tiga","cat",jim)
pet1=Pet("liga","dog",jim)
jim.add_pet(pet1)
jim.add_pet(pet2)
jim.add_pet(pet4)
jim.add_pet(pet3)

print(jim.pets())
print(jim.get_sorted_pets())