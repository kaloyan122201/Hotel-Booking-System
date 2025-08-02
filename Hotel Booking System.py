import json
import datetime

#saving data
def save_bookings(all_rooms, filename="bookings.json"):
    try:
        with open(filename, "w") as file:
            json.dump(all_rooms, file)
        print("✅ Bookings saved successfully.")
    except Exception as e:
        print(f"❌ Failed to save bookings: {e}")
#load data from a file
def load_bookings(filename="bookings.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Keys in JSON come back as strings, so convert them back to int
        return {int(k): v for k, v in data.items()}
    except FileNotFoundError:
        print("⚠️ No saved booking file found. Starting fresh.")
        return {}
    except Exception as e:
        print(f"❌ Failed to load bookings: {e}")
        return {}

# room = type = str,price = float,booked = bool,guest = None/str
def show_menu():
    options = ["View Available Rooms","Book a Room","Cancel a Booking","View All Bookings","Search Booking by Guest Name","Save Bookings", "Load Bookings"]
    counter = 1
    print()
    for option in options:
        print(f"{counter}. {option}")
        counter+=1

#show types of room
def show_types_of_rooms(nm_room:int) :
    type_of_room = ""
    price = 0.00
    if nm_room == 1 or nm_room ==99 or nm_room == 101 or nm_room == 199:
        type_of_room = "Apartment"
        price = 120.00
    elif nm_room % 3 ==0:
        type_of_room = "Deluxe"
        price = 85.00
    elif nm_room %5 ==0:
        type_of_room = "Suite"
        price = 100.00
    elif nm_room %2==0:
        type_of_room ="Double"
        price = 75.00
    else:
        type_of_room ="Twins"
        price = 75.00
    return type_of_room,price

def view_available_rooms(all_rooms):
    print("Type Exit to go back")
    print("Or type All to see all available rooms")
    while True:
        search_type = input("Type of room: ").title()
        if search_type =="Exit":
            break
        elif search_type == "All":
            for room, info in all_rooms.items():
                if not info["booked"]:
                    print(f"{room} - {info["type"]}")
        for room,info in all_rooms.items():
            if not info["booked"] :
                if search_type == "Twins":
                    if info["type"] == search_type:
                        price = info["price"]
                        print(f"Room {room} - {info['type']} - ${info['price']}")
                elif search_type == "Double":
                    if info["type"] == search_type:
                        print(f"Room {room} - {info['type']} - ${info['price']}")
                elif search_type == "Deluxe":
                    if info["type"] == search_type:
                        print(f"Room {room} - {info['type']} - ${info['price']}")
                elif search_type == "Apartment":
                    if info["type"] == search_type:
                        print(f"Room {room} - {info['type']} - ${info['price']}")
                else:
                    if info["type"] == search_type:
                        print(f"Room {room} - {info['type']} - ${info['price']}")

def book_a_room(all_rooms):
    date = datetime.datetime.now()
    formatted_date = date.strftime("%d-%m-%Y")
    print("Type Exit to go back!")
    while True:
        room = input("Enter room number you want to book: ")

        if room == "Exit":
            break
        elif not room.isdigit():
            print("Please enter a valid number.")
            continue

        room = int(room)
        if room < 1 or room > 200:
            print("Invalid number. The room should be between 1 and 200")
            continue

        if not all_rooms[room]['booked']:
            type_of_room, price = show_types_of_rooms(room)
            print(f"Room type: {type_of_room} \nPrice: ${price:.2f}")
            try:
                name_of_guest = input("Enter your full name: ").strip().title().split()
                if name_of_guest == "Exit":
                    break
            except ValueError:
                print("Wrong input... Let's start again!")
                continue
            # Ask how many nights
            while True:
                try:
                    nights = int(input("How many nights will you stay? "))
                    if nights <= 0:
                        print("Please enter a positive number of nights.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            from_date = date.strftime("%d-%m-%Y")
            end_date = date + datetime.timedelta(days=nights)
            until_date = end_date.strftime("%d-%m-%Y")

            all_rooms[room] = {
                "type": type_of_room,
                "price": price,
                "booked": True,
                "guest": name_of_guest,
                "from": from_date,
                "until": until_date
            }

            print(f"✅ Room {room} booked successfully from {from_date} until {until_date}.")
            break
        else:
            print(
                f"\nRoom {room} is already booked by {' '.join(all_rooms[room]['guest'])} from {all_rooms[room]['from']} until {all_rooms[room]['until']}")



def cancel_booking(all_rooms:dict):
    while True:
        print("Type Exit to go back")
        guest_room = input("Which room you would like to cancel: ")
        if guest_room == 'Exit':
            break
        if guest_room.isdigit():
            guest_room = int(guest_room)
            if guest_room not in all_rooms:
                print("Invalid number")
                break
            else:
                if not all_rooms[guest_room]["booked"]:
                    print(f"Currently room {guest_room}№ is not booked.")
                    full_name = input("Can you confirm your full name: ")
                    reservation_name = ' '.join(all_rooms[guest_room]["guest"])
                    if full_name == reservation_name:
                        print(f'Thank you {full_name} your reservation is canceled successfully!')
                        all_rooms[guest_room]["booked"] = False
                        all_rooms[guest_room]["guest"] = None
                        all_rooms[guest_room]["from"] = None
                        all_rooms[guest_room]["until"] = None

                    else:
                        print("Name does not match the booking. Cannot cancel.")
                        break
                else:
                    full_name = input("Can you confirm your full name: ")
                    reservation_name = ' '.join(all_rooms[guest_room]["guest"])
                    if full_name == reservation_name:
                        are_you_sure = input("Are you sure you want to cancel you reservation?: [y/n]").lower()
                        if are_you_sure == "y":
                            print(f'Thank you {full_name} your reservation is canceled successfully!')
                            all_rooms[guest_room]["booked"] = False
                            all_rooms[guest_room]["guest"] = None
                            all_rooms[guest_room]["from"] = None
                            all_rooms[guest_room]["until"] = None
                            break
                        else:
                            print("You didn't cancel your reservation. You are being transfered to the main menu.")
                            break
                    else:
                        print("Name does not match the booking. Cannot cancel.")
                        break

def check_all_bookings(all_rooms):
    for room,info in all_rooms.items():
        if all_rooms[room]["guest"] == None and all_rooms[room]["from"] == None:
            continue
        else:
            print(f"Room № {room} booked by {' '.join(all_rooms[room]["guest"])} from {all_rooms[room]["from"]} until {all_rooms[room]["until"]}")

def search_booking_by_name(all_rooms):
    print("Type Exit to go back!")
    while True:
        searched_name = input("Search for booking. Enter a name: ")
        if searched_name == "Exit":
            break
        found = False
        for room, info in all_rooms.items():
            guest = info.get("guest")
            if not guest:
                continue  # skip if guest is None or empty
            try:
                full_name = ' '.join(guest)  # guest is a list like ['Kaloyan', 'Hristov']
            except TypeError:
                continue  # skip if guest is not iterable (just in case)

            if searched_name.title() in full_name.title():
                print(f"{full_name} has room № {room} ({info['type']}) from {info['from']} until {info["until"]}")
                found = True

        if not found:
            print(f"{searched_name} does not have a booking.")

#Hotel Booking System
hotel_occupancy = 200
print("Welcome to your Hotel Booking System")
print(f"The hotel has a total amount of  {hotel_occupancy} rooms")
print("Types: Twins, Double, Suite, Deluxe, Apartment")

rooms = {}
for room_number in range(1,hotel_occupancy +1):
    type_of_room, price = show_types_of_rooms(room_number)
    rooms[room_number] = {"type": type_of_room,
                    "price": price,
                    "booked": False,
                    "guest": None,
                    "from": None,
                    "until": None
                    }
while True:
    try:
        show_menu()
        choice = int(input("\nEnter your choice [1-7]: "))
        print()
        if 0>=choice >=8:
            print("Invalid input.")
            continue
    except ValueError:
        print("Invalid input.")
        continue
    match choice:
        case 1:
            view_available_rooms(rooms)
        case 2:
            book_a_room(rooms)
        case 3:
            cancel_booking(rooms)
        case 4:
            check_all_bookings(rooms)
        case 5:
            search_booking_by_name(rooms)
        case 6:
            save_bookings(rooms,"bookings.json")
            break
        case 7:
            rooms = load_bookings("bookings.json")
