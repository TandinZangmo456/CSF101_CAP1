import Schedule
import time

# Define your tasks as functions
def task1():
    weather = "sunny"  # Replace with your weather data source
    if weather == "sunny":
        print("Task 1: Go for a run on a sunny day")
    else:
        print("Task 1: Stay indoors on a cloudy or rainy day")

def task2():
    groceries_needed = True  # Replace with your grocery list status
    if groceries_needed:
        print("Task 2: Buy groceries")
    else:
        print("Task 2: No need to buy groceries today")

def task3():
    project_completed = False  # Replace with your project status
    if project_completed:
        print("Task 3: Make dinner")
    else:
        print("Task 3: Make dinner")

# Schedule your tasks
schedule.every().day.at("08:00").do(task1)  # Schedule task1 at 8:00 AM
schedule.every().day.at("12:30").do(task2)  # Schedule task2 at 12:30 PM
schedule.every().day.at("16:00").do(task3)  # Schedule task3 at 4:00 PM

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)  # Check for scheduled tasks every second
