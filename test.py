import csv
with open("acme_worksheet.csv", newline = '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        print(row['Employee Name'],'|',row['Date'],row,'|',['Work Hours'])
        
with open("new_acme_worksheet.csv", 'a+', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    
    writer.writerow(["Vlad","26.03.22","8"])
    writer.writerow(["Alex","26.03.21","6"])
    writer.writerow(["Ivan","26.03.23","5"])
