from google.cloud import bigquery
import os

credentials_path = r"C:\Users\block360_\Desktop\Zeeshan Data\Project"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'bubbly-enigma-444309-h2.Shops.orders'

rows_to_insert = [
    {"id": 0, "product_id":1001 , "product_name" : "Laptop", "quantity": 1, "price": 1200,"order_id": 1 ,"order_date": "2024-12-24"},
    {"id": 1, "product_id":1002 , "product_name" : "Mouse", "quantity": 2, "price": 50,"order_id": 1 ,"order_date": "2024-12-24"},
    {"id": 2, "product_id":1003 , "product_name" : "Desk Chair", "quantity": 1, "price": 200,"order_id":2 ,"order_date": "2024-12-22"}
]
errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))
client = bigquery.Client()
table_id = 'bubbly-enigma-444309-h2.Shops.orders'

rows_to_insert = [
    {"id": 0, "product_id":1001 , "product_name" : "Laptop", "quantity": 1, "price": 1200,"order_id": 1 ,"orders_date": 2024-12-24},
    {"id": 1, "product_id":1002 , "product_name" : "Mouse", "quantity": 2, "price": 50,"order_id": 1 ,"orders_date": 2024-12-24},
    {"id": 2, "product_id":1003 , "product_name" : "Desk Chair", "quantity": 1, "price": 200,"order_id":2 ,"orders_date": 2024-12-22}
]
errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))