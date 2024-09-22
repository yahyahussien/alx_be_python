# Prompt for the task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for whether the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder based on the priority and time sensitivity
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please complete it as soon as possible."
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that you should aim to complete today."
        else:
            reminder += ". Try to finish it within the next few days."
    case 'low':
        reminder = f"'{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " that you should consider completing today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority. Please enter 'high', 'medium', or 'low'."

# Print the customized reminder
print(f"Reminder: {reminder}")
