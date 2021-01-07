
# package class

# fields for the class: 0. ID 1. Address 2.City  3.State	4.Zip
# 5.Delivery Deadline 6. "Mass in KILO"	7. Notes

class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, note, delivery_time):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.delivery_time = None


