class Hall:
    def __init__(self, row, col, hall):
        self.seats = [[0 for i in range(col)] for j in range(row)]
        self.show_list = []
        self.row = row
        self.col = col
        self.hall = hall
    def entry_show(self, id, movie_name, time):
        show = {'id': id, 'movie_name': movie_name, 'time': time}
        self.show_list.append(show)

    def book_seats(self, seat_book):
        for row, col in seat_book:
            if 1 <= row <= self.row and 1 <= col <= self.col:
                if self.seats[row ][col] == 0:
                    self.seats[row ][col] = 1
                else:
                    print("Seat is Booked")
            else:
                print("Invalid Seat")

    def view_list(self):
        for show in self.show_list:
            print(show)

    def availeble_seat(self):
        for row in self.seats:
            print(" ".join(map(str, row)))

class StarCinema:
    def __init__(self):
        self.hall_dict = {}

    def entry_hall(self, hall):
        self.hall_dict[hall.hall] = hall
    def hall_no(self, hall):
        return self.hall_dict.get(hall)

hall1 = Hall(7,6,1)
hall2 = Hall(7,6,2)
hall1.entry_show('100','Avenger','11:00 Am')
hall2.entry_show('103','Dark world', '3:00 PM')

cinema = StarCinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)
while True:
    print("1. View  Shows ")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")
    opt = input("Enter some one: ")
    if opt == '1':
        for hall_no, hall in cinema.hall_dict.items():
            print(f"Hall No: {hall_no}")
            hall.view_list()
        print()
    elif opt == '2':
        hall = int(input("Enter hall No : "))
        hall = cinema.hall_no(hall)
        if hall:
            hall.availeble_seat()
        else:
            print("Not Found")
    elif opt == '3':
        hall = int(input("Enter Hall Number: "))
        hall = cinema.hall_no(hall)
        if hall:
            show_id = input("Enter Show ID: ")
            cnt = int(input("Enter The Number Of Seats "))
            booking_seat = []
            for _ in range(cnt):
                seat_input = input(f"Enter Seat {_ + 1}")
                seat = tuple(map(int, seat_input.split('-')))
                booking_seat.append(seat)
            hall.book_seats(show_id, booking_seat)
            print("Your seat is booked ")
        else:
            print("Not Found.")
    elif opt == '4':
        break
    else:
        print("Enter curect number for right information")
