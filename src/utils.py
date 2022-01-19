import urllib.parse
import re

# Turns blob notes into usable text
# Returns the headers embedded in HTML as special and the flavor text as normal
def get_blob_notes(blob_notes):
    unencoded = urllib.parse.unquote(blob_notes).replace("<br>","\n")
    # Find all of the text embedded in HTML tags
    special = re.findall(r"<(\w+)>([^<>]*)</?\1>", unencoded)
    # Find all of the text not embedded in HTML tags
    normal = re.findall(r"</\w+>\s*(\w(.|\s)*)", unencoded)
    return (special, normal)

# Get the rarity of a magic item
def get_rarity(item):
    rarities = ["legendary", "very rare", "rare", "uncommon", "common"]
    for rarity in rarities:
        if item.lower().find(rarity) >= 0:
            return rarity

# Get all the tags of an item, compared to a preexisting one
def get_tags(item):
    tags = ["wand"] # TODO: Add all tags here
    found_tags = []
    for tag in tags:
        if item.lower().find(tag) >= 0:
            found_tags.append(tag)
    return found_tags