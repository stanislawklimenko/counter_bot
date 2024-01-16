import schedule
import time
from datetime import datetime, timedelta

food = 0
rent = 0
friends_family = 0
connection = 0
transport = 0
home = 0
hair = 0
taxes = 0
clothes = 0
subscription = 0
education = 0
health = 0


def end_of_month_job():
    print(f'food: {food} '
          f'\nrent: {rent} '
          f'\nfriends_family: {friends_family} '
          f'\nconnection: {connection} '
          f'\ntransport: {transport} '
          f'\nhome: {home} '
          f'\nhair: {hair} '
          f'\ntaxes: {taxes} '
          f'\nclothes: {clothes} '
          f'\nsubscription: {subscription} '
          f'\neducation: {education} '
          f'\nhealth: {health}')


# Schedule the job at 23:59 on the last day of each month
def schedule_end_of_month_job():
    now = datetime.now()
    last_day_of_month = datetime(now.year, now.month, 1) + timedelta(days=32)
    last_day_of_month = last_day_of_month.replace(day=1) - timedelta(days=1)
    last_day_time = last_day_of_month.replace(hour=23, minute=59, second=0, microsecond=0)
    schedule.every().day.at(last_day_time.strftime('%H:%M')).do(end_of_month_job)


# Function to add cost to a specific category
def add_cost(category, cost):
    global food, rent, friends_family, connection, transport, home, hair, taxes, clothes, subscription, education, health

    if category == 'food':
        food += cost
    elif category == 'rent':
        rent += cost
    elif category == 'friends_family':
        friends_family += cost
    elif category == 'connection':
        connection += cost
    elif category == 'transport':
        transport += cost
    elif category == 'home':
        home += cost
    elif category == 'hair':
        hair += cost
    elif category == 'taxes':
        taxes += cost
    elif category == 'clothes':
        clothes += cost
    elif category == 'subscription':
        subscription += cost
    elif category == 'education':
        education += cost
    elif category == 'health':
        health += cost
    else:
        print("Invalid category")


# Function to get user input for cost and category
def get_user_input():
    try:
        category = input("Enter category: ")
        cost = float(input("Enter cost: "))
        add_cost(category, cost)
        print(f"{cost} added to {category}")
    except ValueError:
        print("Invalid input. Cost must be a number.")


# Schedule the job
schedule_end_of_month_job()

# Continue the loop for user input
while True:
    schedule.run_pending()
    time.sleep(1)
    get_user_input()
