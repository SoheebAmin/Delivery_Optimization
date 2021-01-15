# This is the package class for creating package objects from the data pulled from CSV files.


class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, note, delivery_time, delivered_by):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.delivery_time = None  # delivery times remains None until actually delivered, then it is updated.
        self.delivered_by = None  # Number of truck to append once delivered
