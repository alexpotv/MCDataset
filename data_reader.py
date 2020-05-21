import anvil
import json

def global_coord_finder(chunk_x, chunk_z, local_x, local_y, local_z):
    x = (int(chunk_x)*16) + local_x
    z = (int(chunk_z)*16) + local_z

    return (x, local_y, z)

with open('datasets/dataset.json') as json_file:
    world = json.load(json_file)

name = world['metadata']['name']
chunks = world['chunks']
regions = {}

length = len(chunks)
i = 0

for chunk in chunks:
    chunk_xz = chunk.split(',')
    right_region = (int(chunk_xz[0]) // 32, int(chunk_xz[1]) // 32)

    if right_region not in regions:
        regions[right_region] = anvil.EmptyRegion(right_region[0], right_region[1])
    
    for x in range(16):
        for z in range(16):
            for y in range(256):
                gcoords = global_coord_finder(chunk_xz[0], chunk_xz[1], x, y, z)
                block = anvil.Block('minecraft', chunks[chunk][str(x)+',.,'+str(z)][y].split(':')[1])
                regions[right_region].set_block(block, gcoords[0], gcoords[1], gcoords[2])
    i += 1
    print("Read chunk ", i, " on ", length)

len_reg = len(regions)
k = 0

for region in regions:
    regions[region].save("generated_world/r."+str(region[0])+"."+str(region[1])+".mca")
    k += 1
    print("Saved region ", k, " on ", len_reg)
