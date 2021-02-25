import csv


with open('data.csv',encoding="utf8") as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    for row in data:
        if not first_line:
            if row[5] == "None":
                with open('noninteresting_url.csv', mode='a',newline='') as csv_file2:
                    data = csv.writer(csv_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([row[4]]) 
            else:
                with open('interesting_url.csv', mode='a',newline='') as csv_file1:
                    data = csv.writer(csv_file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data.writerow([row[0],row[1],row[2],row[3],row[4],row[5]])  
        else:
            first_line = False