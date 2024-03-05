
import csv

# with open("csv_sales_data.csv", newline="") as csvfile:
#     sales_data = csv.reader(csvfile)
#
#     for row in sales_data:
#         for item in row:
#             print(item, end=" ")
#         print()


with open("csv_people_data.csv", "w", newline="") as csvfile:
    data_writer = csv.writer(csvfile)
    data_writer.writerow(["Tom", "Kaunas", "25"])
    data_writer.writerow(["John", "London", "46"])

with open("csv_people_data.csv", "w", newline="") as csvfile:
    data_writer = csv.writer(csvfile, delimiter=" ", quotechar='|')
    data_writer.writerow(["Tom", "Kaunas", "25"])
    data_writer.writerow(["John", "London", "46"])
