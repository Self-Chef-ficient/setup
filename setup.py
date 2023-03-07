"""
Read the data from data folder and create a CSV file for 
recipe instruction, ingredients list and images for storing those
values in DB
"""

import json, csv

def createInstructions(cooking_instruction):
    """
    This function will take in json data from layer1.json
    and will create a instruction.csv that contains ingredient ID,
    ingredient name and step-by-step cooking instruction as three columns
    """
    rows = [] 
    for i in range(0,len(cooking_instruction)):
        row = []
        row.append(cooking_instruction[i]["id"])
        row.append(cooking_instruction[i]["title"])
        step = 0
        instruction = ""
        for j in range(0,len(cooking_instruction[i]["instructions"])):
            instruction += "Step " + str(step) + "->" + cooking_instruction[i]["instructions"][j]["text"] + " "
            step += 1
        row.append(instruction)
        rows.append(row)
    return rows

def createImages(images):
    """
    This function will take in json data from layer2.json
    and will create a images.csv that contains ingredient ID,
    URL of the food image
    """
    rows = [] 
    for i in range(0,len(images)):
        row = []
        row.append(images[i]["id"])
        row.append(images[i]["images"][0]["url"])
        rows.append(row)
    return rows

def ingredientFoodMapping(ingrs):
    """
    This function will take in json data from det_ingrs.json
    and will create a ingrs_food_map.csv that contains ingredient ID,
    and ingrdient
    """
    rows = []
    for i in range(0,len(ingrs)):
        id = ingrs[i]["id"]
        for j in range(0,len(ingrs[i]["ingredients"])):
            row = []
            row.append(id)
            row.append(ingrs[i]["ingredients"][j]["text"])
            rows.append(row)
    return rows


def main():
    #Getting cooking instruction from the layer1.json file
    layer1_filename = "data/layer1.json"
    cooking_instruction_csv = "data/cooking_instruction.csv"
    cooking_instruction_fields = ['ID', 'Name', 'Instructions']
    layer1 = open(layer1_filename, 'r')
    cooking_instruction = json.load(layer1)
    cooking_instruction_data = createInstructions(cooking_instruction)
    layer1.close()
    with open(cooking_instruction_csv, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(cooking_instruction_fields) 
        csvwriter.writerows(cooking_instruction_data)   

    #Getting images URL for displaying in the frontend from layer2
    layer2_filename = "data/layer2.json"
    image_csv = "data/images.csv"
    image_fields = ['ID', 'URL']
    layer2 = open(layer2_filename, 'r')
    images = json.load(layer2)
    images_data = createImages(images)
    layer2.close()
    with open(image_csv, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(image_fields) 
        csvwriter.writerows(images_data)

    #Creating ingredients to food id mapping
    ingrs_filename = "data/det_ingrs.json"
    ingrs_csv = "data/ingrs_food_map.csv"
    ingrs_fields = ['ID', 'Ingr']
    ingrs_file = open(ingrs_filename, 'r')
    ingrs = json.load(ingrs_file)
    ingrs_data = ingredientFoodMapping(ingrs)
    ingrs_file.close()
    with open(ingrs_csv, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(ingrs_fields) 
        csvwriter.writerows(ingrs_data)


if __name__ == "__main__":
    main()