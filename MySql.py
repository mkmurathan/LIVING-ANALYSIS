import pandas as pd
import mysql.connector

# Verilerinizi pandas DataFrame olarak yükleyin
df = pd.read_csv("data.csv")  # CSV dosyanızın yolu

# MySQL bağlantısı kurun
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="country_data"
)
cursor = connection.cursor()

# Veriyi MySQL tablosuna aktarın
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO country_info (Country, Year, Average_Monthly_Income, Cost_of_Living, 
                                  Housing_Cost_Percentage, Tax_Rate, Savings_Percentage, 
                                  Healthcare_Cost_Percentage, Education_Cost_Percentage, 
                                  Transportation_Cost_Percentage, Region)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))
connection.commit()
cursor.close()
connection.close()
