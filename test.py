import anvil

region0 = anvil.Region.from_file('worlds/New World2/region/r.0.0.mca')
region1 = anvil.Region.from_file('worlds/New World2/region/r.0.-1.mca')
# You can also provide the region file name instead of the object
chunk0 = anvil.Chunk.from_region(region0, 0, 0)
chunk1 = anvil.Chunk.from_region(region1, 0, -3)

print(chunk0 == chunk1)

# If `section` is not provided, will get it from the y coords
# and assume it's global

block = chunk1.get_block(0, 0, 13)

print(block)