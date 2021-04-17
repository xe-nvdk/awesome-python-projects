from datetime import datetime

from influxdb_client import Point, InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "money"

client = InfluxDBClient.from_config_file('config.ini')

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

print("#############################################################################")
print("####################### Welcome to Follow the Money #########################")
print("#############################################################################\n")


CONT = "y"
while CONT =="y":

    OPERATION = str(input("Do you want to enter a income or expense\n\nPress 1 for income \nPress 2 for expense\n\nPress 0 to set a initial balance\n\nType your election: "))

    if OPERATION == "1":
        CATEGORY = str(input("Type category for you income: "))
        INCOME = str(input("Name your income: "))
        VALUE = float(input("Enter the amount: "))
        p = Point("follow-the-money").tag("operation", "income").tag("category", CATEGORY).tag("item", INCOME).field("amount", VALUE)
        write_api.write(bucket=bucket, record=p)

        CONT = str(input("\nDo you want to add another record? [y/n]: "))

    elif OPERATION == "2":
        CATEGORY = str(input("Type category for you expense: "))
        EXPENSE = str(input("Name your expense: "))
        VALUE = float(input("Enter the amount: "))
        p = Point("follow-the-money").tag("operation", "expense").tag("category", CATEGORY).tag("item", EXPENSE).field("amount", VALUE)
        write_api.write(bucket=bucket, record=p)

        CONT = str(input("\nDo you want to add another record? [y/n]: "))

    elif OPERATION == "0":
        VALUE = float(input("Enter your initial balance: "))
        p = Point("follow-the-money").tag("operation", "initial-balance").field("amount", VALUE)
        write_api.write(bucket=bucket, record=p)

        CONT = str(input("\nDo you want to add another record? [y/n]: "))

    else:
        pass