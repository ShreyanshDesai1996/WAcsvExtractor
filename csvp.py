import os
import csv

filectr=0
numctr=0

newfile=open("AllNumbers.csv","w")

directory = os.path.join("c:\\","wnum")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           with open(file) as csv_file:
               csv_reader = csv.reader(csv_file, delimiter=',')
               filectr+=1
               line_count = 0
               for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        print(row[12])
                        newfile.write(row[12]+'\n')
                        numctr+=1
                        line_count += 1
newfile.close()
print('Number of files read:'+str(filectr))
print('Phone numbers saved:'+str(numctr))