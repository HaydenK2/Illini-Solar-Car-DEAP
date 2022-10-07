import csv
#write csv function
#make the csv file writable
 
def write_csv():
  with open('path/to/csv_file', 'csv_name') as f:
    writer = csv.writer(f)
 
    #write header
    header = ['target_mph', 'acceleration', 'decceleration', 'try-loop', 'is_keyboard']
    writer.writerow(header)

    #from here we write the data that we received onto the csv file
    

