# Import the package to manage csv files
import csv

# Loop through each CSV file and output the contents
with open('/Users/bradmessner/Desktop/emp_data.csv', 'rb') as csvfile:
     fileContents = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in fileContents:
         print ', '.join(row)

# Write data out to a file
with open('/Users/bradmessner/Desktop/emp_data_out.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name'] + ['Office'] + ['Course'])
    filewriter.writerow(['Brad D Messner'] + ['Lynch 103'] + ['Machine Learning'])
    filewriter.writerow(['Ryan #1', 'Lynch 106', 'Machine Learning'])