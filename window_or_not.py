def c(n, tn):
    if n<=0 or n>tn :
        print("Invalid seat number")
total_rows = 11
seats_per_row = int(input("Enter the number of seats per row\n"))
total_seats = total_rows * seats_per_row
window_seats = total_rows * 2

seat_no = int(input("Enter the seat number\n"))
c(seat_no, total_seats)
print("Window Seat") if seat_no%seats_per_row == 1 or seat_no%seats_per_row == 0 else print("Aisle Seat")