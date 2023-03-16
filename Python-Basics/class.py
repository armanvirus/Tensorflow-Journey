class Flight():
        def __init__(self,capacity)
            self.capacity = capacity
            self.passenger = []
        def add_passenger(self,name):
            if not self.open_seats():
                return False
            self.passenger.append(name)
            return True
        
        def open_seats(self):
            return self.capacity - len(self.passenger)


flight = Flight(3)

people = ["arman","jacks", "kabash", "al-amin"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        