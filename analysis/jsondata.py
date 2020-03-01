#load json file to a dictionary
import json

def load_data():
    with open('data.json') as json_file:
        data = json.load(json_file)
    
	return data


#save a dictionary to json file
# def store_data(data):
#     with open('data.json', 'w') as outfile:
#         json.dump(data, outfile)