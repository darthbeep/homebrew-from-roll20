from src import utils

def create_item(item):
    iattr = item["attributes"]
    special, normal = utils.get_blob_notes(item["blobNotes"])
    if special[1][0] == "em":
        rarity = utils.get_rarity(special[1][1])
        found_tags = utils.get_tags(special[1][1])
    
    # Fill out fields
    name = iattr["name"]
    print(special, normal, rarity, found_tags)
    