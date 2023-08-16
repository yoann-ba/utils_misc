

import json



# load

file_path = ''
with open(file_path, 'r') as json_file:
    file = json.load(json_file)



# save with dump

dictionary = {}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)


# save with dumps

dictionary = {}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


