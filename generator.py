import anvil
import json
import os

id_number = 0
maps_to_include = ["New World"]
region_files = []
region_tuples = []
chunks_to_load = []
loaded_regions = {}
loaded_chunks = {}

for world in maps_to_include:
    filepath = "worlds/" + world + "/region"
    for worldfile in os.listdir(filepath):
        if worldfile.endswith(".mca"):
            region_files.append(worldfile)

    for filename in region_files:
        splitfilename = filename.split(".")
        region_tuples.append((int(splitfilename[1]), int(splitfilename[2])))
        loaded_regions[(int(splitfilename[1]), int(splitfilename[2]))] = anvil.Region.from_file(filepath + "/" + filename)
    
    for region_to_load in region_tuples:
        for i in range(0, 32):
            for j in range(0, 32):
                chunks_to_load.append(((region_to_load[0]*32)+i, (region_to_load[1]*32)+j))
    
    for chunk in chunks_to_load:
        print(chunk[0], chunk[1])
        x, y = chunk[0] // 32, chunk[1] // 32
        print("Loading chunk:", chunk[0], chunk[1])
        right_region = loaded_regions[(x, y)]
        try:
            loaded_chunks[(chunk[0], chunk[1])] = anvil.Chunk.from_region(right_region, chunk[0], chunk[1])
        except:
            pass
