import csv
import os

# Set the target file size in bytes
target_size = 1000000

# Define the number of rows and columns in the CSV file
num_rows = 1000
num_cols = 10

# Generate random data for the CSV file
data = [[str(i) + ',' + str(j) for j in range(num_cols)] for i in range(num_rows)]

# Open a file for writing and use the csv module to write the data to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Column ' + str(i) for i in range(num_cols)])
    
    # Write the data rows
    while os.path.getsize('output.csv') < target_size:
        writer.writerow(data[random.randint(0, num_rows - 1)])
