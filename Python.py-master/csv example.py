import csv

'#set csv file location and filename
self.loc = 'D:\csv_temp.csv'

#when make a csvfile
with open(self.loc, 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter = ',', quotechar = '|')
  writer.writerow(['obs', 'var1', 'var2', 'var3',...])
  
#write new data on csvfile
with open(self.loc, 'a') as csvfile:
  writer = csv.writer(csvfile, delimiter = ',', quotechar = '|')
  writer.writerow([obs, data1, data2, data3, data4, ....])
  
#read csvfile
with open(self.loc, 'rb') as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
  for row in csvreader:
    print row
    print row[1]
    
#modify csvdata
r = csv.reader(open(self.loc))
  lines = [l for l in r]
  print lines
  lines[obs][3] = new_data
  writer = csv.writer(open(location, 'w'))
  writer.writerows(lines)
