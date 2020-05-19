import anvil
import json
import os

id_number = 0
folders_to_include = []
region_files = []
region_tuples = []
chunks_to_load = []

for world in folders_to_include:
    for file in os.listdir("/worlds/" + world + "/region"):
        if file.endswith(".mca"):
            region_files.append(file)

    for filename in region_files:
        filename = filename.split(".")
        region_tuples.append((filename[1], filename[2]))
    
    for region_to_load in region_tuples:
        for i in range(0, 31):
            for j in range(0, 31):
                chunks_to_load.append(((region_to_load[0]*32)+i, (region_to_load[1]*32)+j))
    
    print(chunks_to_load)
