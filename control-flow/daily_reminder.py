task = input("Enter your task: ")
priority  = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f'Reminder: "{task}" is a high priority task that requires immediate attention today!')
        elif time_bound == "no":
            print(f'Reminder: "{task}" is a high priority. Consider completing it when you have free time.')
    case "medium":
        if time_bound == "yes":
            print(f'Reminder: "{task}" is a medium priority task that requires attention today or tommorrow!')
        elif time_bound == "no":
            print(f'Reminder: "{task}" is a medium priority. Consider completing it when you have free time.')
    case "low":
        if time_bound == "yes":
            print(f'Reminder: "{task}" is a low priority task that do not requires immediate attention today!. You can do it next weeek.')
        elif time_bound == "no":
            print(f'Reminder: "{task}" is a low priority. Do not need completing it.')
            