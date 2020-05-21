import anvil
import json
import os

region_files = []
region_tuples = []
chunks_to_load = []
loaded_regions = {}
loaded_chunks = {}

print("Folder name?")
world = input()

print("World name?")
name = input()

print("Authors (Separated by commas)?")
authors = input().split(',')

print("Source?")
source = input()

print("Published date (DD/MM/YYYY)?")
date = input()

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
    print("Region:", x, y)
    right_region = loaded_regions[(x, y)]
    try:
        loaded_chunks[(chunk[0], chunk[1])] = anvil.Chunk.from_region(right_region, chunk[0], chunk[1])
    except:
        pass

whole_chunks = {}

length = len(loaded_chunks)
i = 0

for chunk in loaded_chunks:
    chunk_blocks = {}
    chunk_name = str(chunk[0])+','+str(chunk[1])
    for x in range(16):
        for z in range (16):
            height_list = []
            for y in range(256):
                height_list.append("minecraft:" + str(loaded_chunks[chunk].get_block(x, y, z).id))
            chunk_blocks[str(x)+',.,'+str(z)] = height_list
    whole_chunks[chunk_name] = chunk_blocks
    i += 1
    print("Chunk ", i, " on ", length)


world_dict = {'metadata': {'name': name, 'authors': authors, 'source': source, 'date': date}, 'chunks': whole_chunks}

with open('MCDataset.json', 'a', encoding='utf-8') as json_file:
    json.dump(world_dict, json_file, ensure_ascii=False, indent=4)
    json_file.write('\n')
