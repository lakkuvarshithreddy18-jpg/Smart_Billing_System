# COMPLETE STORE SYSTEM

import pywhatkit
import datetime

# --- global storage ---
all_persons = []

items = {
    "I001": {"name": "Brownise Bread", "price": 40, "qty": 10},
    "I002": {"name": "Amul Milk (1L)", "price": 60, "qty": 10},
    "I003": {"name": "India Gate Rice (10kg bag)", "price": 300, "qty": 10},
    "I004": {"name": "Neuturalla Peanut Butter (250ml)", "price": 250, "qty": 10},
    "I005": {"name": "Godrej Yummiez Eggs 6", "price": 42, "qty": 10},
    "I006": {"name": "Broom Stick", "price": 110, "qty": 10},
    "I007": {"name": "Sugar 1kg", "price": 50, "qty": 10},
    "I008": {"name": "Prestige Mop", "price": 450, "qty": 10}
}


# === person class ===
class Person:

    def __init__(self, uid, name, balance):
        self.uid = uid
        self.name = name
        self.balance = balance
        self.total_spent = 0
        self.bills = []   # Stores full bill records


# === store class ===
class Store:

    def __init__(self, name):
        self.name = name

    def find_person(self, uid):
        for person in all_persons:
            if person.uid == uid:
                return person
        return None

    def process_shopping(self, uid, item_orders):

        print("\n------------------------------")

        person = self.find_person(uid)

        if person is None:
            print("Invalid UID")
            return

        print("Welcome", person.name)
        print("Balance:", person.balance)

        total_bill = 0
        bill_items = {}

        # --- add items ---
        for item_id, quantity in item_orders.items():

            if item_id in items:

                available_stock = items[item_id]["qty"]

                if available_stock >= quantity:

                    item_name = items[item_id]["name"]
                    price = items[item_id]["price"]

                    total_price = price * quantity
                    total_bill += total_price

                    items[item_id]["qty"] -= quantity
                    bill_items[item_name] = quantity

                    print("Added:", item_name, "x", quantity)
                   

                else:
                    print("Error:", item_id,
                          "| Only", available_stock, "available")

            else:
                print("Invalid Item:", item_id)

        print("\nFinal Bill:", total_bill)

        # --- payment ---
        if person.balance >= total_bill and total_bill > 0:

            person.balance -= total_bill
            person.total_spent += total_bill

            # Store complete bill
            person.bills.append({
                "person": person.name,
                "previous_balance": person.balance + total_bill,
                "items": bill_items,
                "total": total_bill,
                "remaining_balance": person.balance,
            })

            print("Payment Successful")
            print("Remaining Balance:", person.balance)

        else:
            print("Not enough balance or no valid items")


# === print items ===
def print_available_items():

    print("\nAvailable Items:")
    print("-----------------")

    for key, value in items.items():
        print(key, "-", value["name"],
              "-", value["price"],
              "| Stock:", value["qty"])

    print("-----------------")


# === summary ===
def print_summary():

    print("\n====== SUMMARY ======")

    total_revenue = 0

    for person in all_persons:

        initial_balance = person.balance + person.total_spent
        total_revenue += person.total_spent

        print("\nName:", person.name)
        print("UID:", person.uid)
        print("Initial Balance:", initial_balance)
        print("Total Spent:", person.total_spent)
        print("Current Balance:", person.balance)

        print("\nBill History:")

        overall_items = 0

        for bill in person.bills:

            total_items = sum(bill["items"].values())
            overall_items += total_items
            

            print("               Items purchased       ")
            for item_name,qty in bill["items"].items():
                print("          -" , item_name, "x",qty)
            print("  Total Items Bought:", total_items)
            print("  Bill Amount:", bill["total"])
            print("  ----------------")

        print("Total Items Bought (All Bills):", overall_items)
        print("================================")

    print("\nTotal Store Revenue:", total_revenue)

    print_available_items()


# === setup ===
def setup():

    print("Store Started...\n")

    all_persons.append(Person("252U1R1138", "Varshith", 5000))
    all_persons.append(Person("252U1R1161", "Deepika", 3000))
    all_persons.append(Person("252U1R1163", "Vignesh", 8000))

    print_available_items()

    return Store("Debba Debba Mart")


# === main ===

store = setup()

store.process_shopping("252U1R1138", {"I001": 2, "I002": 1})
store.process_shopping("252U1R1161", {"I004": 1})
store.process_shopping("252U1R1163", {"I002": 11})  # Error case

print_summary()
message = all_persons[1].bills
Datte = datetime.datetime.now()
phone_number = "+919063185101"
pywhatkit.sendwhatmsg(phone_number, str(message), Datte.hour, Datte.minute + 2)