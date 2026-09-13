import bpy
import csv
import math

selection = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

col = ['', 'id', 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']

with open('C:\Anshuman\Temple\Scripts\Scene_positions\Data_files\data_LP_Tile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(col)

    for idx, obj in enumerate(selection):
        data = []
        
        data.append(idx)
        data.append(idx)

        # Translation (meters -> centimeters)
        data.append(obj.location.x * 100)
        data.append(obj.location.y * 100)
        data.append(obj.location.z * 100)

        # Rotation (radians -> degrees)
        data.append(math.degrees(obj.rotation_euler.x))
        data.append(math.degrees(obj.rotation_euler.y))
        data.append(math.degrees(obj.rotation_euler.z))

        # Scale
        data.append(obj.scale.x)
        data.append(-obj.scale.y)
        data.append(obj.scale.z)

        writer.writerow(data)

        del data
