import matplotlib.pyplot as plt
import csv

with open('precipitationmga.csv','r+') as fl:
    reader = csv.reader(fl)
    for row in reader:
        for element in row:
            if ',' in element:
                row.remove(element)
                elemente = element.replace(',','.')
                row.append(elemente)
fl.close()