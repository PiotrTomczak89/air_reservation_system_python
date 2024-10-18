from pprint import pprint as pp
from flight import Flight 
from planes import AirbusA380, Boeing737Max
# from planes import * # import only __all__
from helpers import card_printer



def main():
    # plane = Airplane()
    airbus = AirbusA380()
    boeing = Boeing737Max()
    f = Flight('LO127', airbus)
    # print(boeing.get_seating_plan())
    # print(f.get_airline())
    # print(f.get_number())
    # print(f.get_model())
    # print(boeing.get_seats_no())
    f.allocate_passenger(passenger="Lech K", seat="12C")
    f.allocate_passenger(passenger="Jarosław K", seat="12B")
    f.allocate_passenger(passenger="Paweł K", seat="12A")
    f.relocate_passenger(seat_from="12A", seat_to="25G")
    pp(f.seating_plan)
    pp(f.get_empty_seat())
    # pp(f.get_passenger_list())

    f.print_ticket(card_printer)

    for passenger in f.get_passenger_list():
        print(passenger)
        
        
if __name__ == 'main':
    main()