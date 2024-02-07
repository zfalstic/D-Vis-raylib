import csv
import os

class CSV:
    def __init__(self, path: str):
        self.path = path
        self.scaled_rows = []
        
        with open(self.path, mode='r') as file:
            csvFile = csv.DictReader(file)
            
            self.rows = [line for line in csvFile]
    
    def scale_rows(self, MAX: int, MIN: int):
        minX = float('inf')
        maxX = float('-inf')
        minY = float('inf')
        maxY = float('-inf')
        minZ = float('inf')
        maxZ = float('-inf')
        
        for row in self.rows:
            if float(row['x']) > maxX: maxX = float(row['x'])
            if float(row['x']) < minX: minX = float(row['x'])
            if float(row['y']) > maxY: maxY = float(row['y'])
            if float(row['y']) < minY: minY = float(row['y'])
            if float(row['z']) > maxZ: maxZ = float(row['z'])
            if float(row['z']) < minZ: minZ = float(row['z'])
        
        self.scaled_rows = []
        for row in self.rows:
            new_row = {}
            new_row['x'] = (MAX - MIN) * (float(row['x']) - minX) / (maxX - minX) + MIN
            new_row['y'] = (MAX - MIN) * (float(row['y']) - minY) / (maxY - minY) + MIN
            new_row['z'] = (MAX - MIN) * (float(row['z']) - minZ) / (maxZ - minZ) + MIN
            new_row['species'] = row['species']
            self.scaled_rows.append(new_row)
        
if __name__ == '__main__':
    my_csv = CSV(os.path.join('.', '.', 'data', 'iris.csv'))
    my_csv.scale_rows(-10, 10)
    print(my_csv.scaled_rows)