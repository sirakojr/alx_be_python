current_date = display_current_datetime()
try:
    days_input = input("Enter the number of days to add to the current date: ")
    days_to_add = int(days_input)
    future_date = calculate_future_date(days_to_add)
except ValueError:
    print("Invalid input! Please enter a valid integer number.")