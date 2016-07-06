#! python3
# Customer list merge for CBD users + Theos mail list data for sales team
# data is from CSV files downloaded from Theos and CBD web
# copy the files into the mailist directory on D:\
# Chad Cropley 2016-06-24 a RAD design solution
#
# import modules
import os
import csv
import shutil

# make sure we're in the right directory
os.chdir('d:\\maillist\\')
# print(os.getcwd())

# read file1
filename = input('Enter a Theos mail list filename: ')

shutil.copyfile(filename, 'CUSTLIST-THEOS.csv')

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar="'")
    with open('output11.csv', 'w') as output:
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
        headers = ('Number, Email, Name, Address_1, Address_2, City, State, Zip, Phone, First name, Last name, Contact, SLS Last')
        print(headers, file = output)
        for row in reader:
            if row['Number'] != '':
                print(row['Number'],',',row['Email'],',',row['Name'],',',
                    row['Address_1'],',',row['Address_2'],',',row['City'],',',
                    row['State'],',',row['Zip'],',',row['Phone'],',', ' ',',', ' ',',',
                    row['CONTACT'],',', row['SLS LAST'], file = output)

# read file2
filename2 = input('Enter a CBD mail list filename: ')

shutil.copyfile(filename2, 'cust_cbd.csv')

with open(filename2) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar="'")
    with open('output11.csv', 'a') as output:
        writer = csv.DictWriter(output, quoting=csv.QUOTE_NONE, fieldnames=reader.fieldnames)
        for row in reader:
            if row['Login'] != '':
                print(row['Login'],',',row['E-mail'],',',row['Billing: first name'],',',
                    row['Billing: address'],',',row['Billing: address (line 2)'],',',
                    row['Billing: city'],',',row['Billing: state'],',',
                    row['Billing: zipcode'],',',row['Phone'],',',row['First name'],',',
                    row['Last name'],',',row['Company'], file = output)
            
os.system('pause')

# Remove duplicate items from merge

inFile = open('output11.csv','r')

outFile = open('output12.csv','w')

listLines = []

for line in inFile:
    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()

print ('open output12.csv for mergerd customer list')

os.system('pause')
