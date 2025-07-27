from datetime import datetime
def display_current_datetime ():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
display_current_datetime()