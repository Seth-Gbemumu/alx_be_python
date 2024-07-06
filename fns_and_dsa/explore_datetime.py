
def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

display_current_datetime()
#import datetime
def calculate_future_date(): 
    number_of_days = int(input("Enter the number of days to add to the current date: "))
   # future_date = datetime.timedelta(number_of_days = number_of_days)
    future_date = datetime.datetime.now() + datetime.timedelta(days = number_of_days)
    future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

calculate_future_date()
