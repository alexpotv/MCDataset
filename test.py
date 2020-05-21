import json
import anvil

region = anvil.Region.from_file('worlds/Test/region/r.0.0.mca')

# You can also provide the region file name instead of the object
chunk = anvil.Chunk.from_region(region, 0, 0)

# If `section` is not provided, will get it from the y coords
# and assume it's global
block = chunk.get_block(0, 0, 0)

print(block) # <Block(minecraft:air)>
print("minecraft:" + str(block.id))

a = {'Name': 'Alex'}
b = {'Name': 'Arianne'}

dicts = [a, b]

for a in dicts:
    with open('names.json', 'a', encoding='utf-8') as json_file:
        json.dump(a, json_file, ensure_ascii=False, indent=4)
        json_file.write('\n')
