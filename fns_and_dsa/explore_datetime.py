from datetime import datetime, timedelta


def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    return current_date


def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
    return future_date


def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        # Prompt user for number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        # Calculate and display future date
        calculate_future_date(days_to_add)
        
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()