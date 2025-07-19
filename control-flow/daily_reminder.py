
# Get user input for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        else:
            reminder += ". Focus on this today!"
            print(f"Reminder: {reminder}")
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        else:
            reminder += ". Try to complete it when possible."
            print(f"Reminder: {reminder}")
    
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            print(f"Reminder: {reminder}")
        else:
            reminder += ". Consider completing it when you have free time."
            print(f"Note: {reminder}")
    
    case _:
        print("Invalid priority level. Please use high, medium, or low.")
