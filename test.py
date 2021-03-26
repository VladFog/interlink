import csv
with open("acme_worksheet.csv", newline = '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        print(row['Employee Name'],'|',row['Date'],row,'|',['Work Hours'])
        

