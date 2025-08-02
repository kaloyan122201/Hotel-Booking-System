# 🏨 Hotel Booking System (Python Console App)

This is a simple **Hotel Booking System** built in Python, designed to manage hotel room bookings directly from the terminal. It allows users to view available rooms, make reservations, cancel bookings, and save or load booking data using a JSON file.

## 🚀 Features

- View available rooms by type or list all
- Book a room with guest name and duration
- Cancel an existing booking by confirming guest name
- View all current bookings
- Search bookings by guest name
- Save bookings to a `.json` file
- Load bookings from a saved `.json` file

## 🛏️ Room Types & Pricing

Room types are determined by the room number:

| Room Type  | Criteria                   | Price  |
|------------|----------------------------|--------|
| Apartment  | Room 1, 99, 101, 199        | $120.00 |
| Deluxe     | Room number divisible by 3  | $85.00  |
| Suite      | Room number divisible by 5  | $100.00 |
| Double     | Room number divisible by 2  | $75.00  |
| Twins      | All other rooms             | $75.00  |

---

## 📦 How to Run

1. Make sure you have **Python 3** installed.
2. Save the code in a file named something like `hotel_booking.py`.
3. Open your terminal or command prompt.
4. Run the script using:

```bash
python hotel_booking.py
