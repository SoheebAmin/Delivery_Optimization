# This is the package class for creating package objects from the data pulled from CSV files.


class Package:

    def __init__(self, id, address, city, state, zip, deadline, mass, note, delivery_time, delivered_by):
        """
        :param id: the unique ID of the package
        :param address: the addresses to which the package is to be delivered
        :param city: The city to be delivered
        :param state: The state to be delivered
        :param zip: The zipcode where it needs to be delivered
        :param deadline: The time by which the package must be delivered
        :param mass: The weight of the package
        :param note: The special note for the package, if any
        :param delivery_time: delivery times remains None until actually delivered, then it is updated
        :param delivered_by: Number of truck to append once delivered
        Time Complexity: O(1)
        Space Complexity: O(1)

        The constructor for package objects, composed of all the attributes found in the CSV, as well as two additional
        parameters for when and by which truck the delivery is made.
        """
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.delivery_time = delivery_time
        self.delivered_by = delivered_by
