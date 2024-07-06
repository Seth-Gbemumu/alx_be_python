def display_current_datetime():
    import datetime
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

display_current_datetime()

def calculate_future_date():
    import datetime 
    number_of_days = int(input("Enter the number of days to add to the current date: "))
   # future_date = datetime.timedelta(number_of_days = number_of_days)
    future_date = datetime.datetime.now() + datetime.timedelta(days = number_of_days)
    future_date = future_date.date()
    print(f"Future date: {future_date}")

calculate_future_date()
