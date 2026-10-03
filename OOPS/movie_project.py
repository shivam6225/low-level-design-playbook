class Movie:

    def __init__(self,movie_name=None,total_seats=0,ticket_price=0.0,booked_seats=0):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = booked_seats

    def book_tickets(self,num_of_tickets):

        if num_of_tickets <= self.total_seats - self.booked_seats:
            total_price = num_of_tickets * self.ticket_price
            print(f"Amount to pay for {self.movie_name } tickets: {num_of_tickets} is : {total_price} ")
            self.booked_seats += num_of_tickets
        else:
            print("Sorry , not enough seats available")

    def show_status(self):
        print(f"Movie {self.movie_name} has {self.total_seats-self.booked_seats} seats available and {self.booked_seats} tickets booked")


m1 = Movie("Titanic",100,2.5)
m1.show_status()
m1.book_tickets(10)
m1.show_status()
m1.book_tickets(90)
m1.show_status()
m1.book_tickets(50)
