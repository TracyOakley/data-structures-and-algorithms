from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        animal_string = animal.value

        if animal_string == "dog":
            self.dog_queue.enqueue(animal)
            return

        if animal_string == "cat":
            self.cat_queue.enqueue(animal)
            return
        else:
            return "We cannot accept your Iguana."

    def dequeue(self, pref):
        if pref == "dog":
            return self.dog_queue.dequeue()

        if pref == "cat":
            return self.cat_queue.dequeue()

        else:
            return None


class Dog:
    def __init__(self, value="dog", next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self):
        return f"I'm a {self.value}"


class Cat:
    def __init__(self, value="cat", next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self):
        return f"I'm a {self.value}"
