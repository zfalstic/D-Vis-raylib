import csv
import os
from src.gradient import get_color_gradient
from src.tsne import tsne_to_csv
from distinctipy import get_colors

class CSV:
    def __init__(self, file_name: str):
        tsne_to_csv(file_name)
        
        with open(os.path.join('.', 'data', file_name + '_TSNE'), mode='r') as file:
            csvFile = csv.DictReader(file)
            
            self.rows = [line for line in csvFile]
            
        self.scaled_rows = []
        self.scale_rows(-10, 10)
            
        self.label_color = {}
        self.label_num = 0
        self.color_labels([255, 165, 29], [255, 255, 255]) #original
        #self.color_labels([255, 165, 29], [0, 127, 255]) #azure
        #self.color_labels([0, 255, 0], [0, 0, 255])
        
            
    def color_labels(self, color1, color2):
        for row in self.scaled_rows:
            if row['label'] not in self.label_color:
                self.label_color[row['label']] = []
                
        self.label_num = len(self.label_color)
        
        #gradient = get_color_gradient(color1, color2, self.label_num)
        gradient = [[int(round(i * 255)) for i in x] for x in get_colors(self.label_num)]
        i = 0
        for label in self.label_color:
            self.label_color[label] = gradient[i]
            i += 1
    
    def scale_rows(self, MIN: int, MAX: int):
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
            
            new_row['label'] = row['label']
            self.scaled_rows.append(new_row)
        
if __name__ == '__main__':
    my_csv = CSV(os.path.join('.', '.', 'data', 'iris.csv'))
    my_csv.scale_rows(-10, 10)
    print(my_csv.scaled_rows)