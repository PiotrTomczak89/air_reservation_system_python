class Flight:
    def __init__(self, flight_number, airplane):
        self.flight_number = flight_number

    def get_airlines(self):
        return self.flight_number[:2]
    
    def get_airnumber(self):
        return self.flight_number[2:]
    
    def get_model(self):
        return self.flight_number.get_airplane_model()
    

class Airplane:
    
    def get_seats_no(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)

class AirbusA300(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus A380'
    
    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'

class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Boeing 737 Max'
    
    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'






airbus = AirbusA300()
boeing = Boeing737Max()
f = Flight('LO127', airbus)

print(f.get_airlines())
