import re

# Read the whole .obo file into a string
with open('hp.obo') as f:
    hpo_obo = f.read()

# This will include all entity names, including main names and synonyms
entity_names = []

# This looks for all the text that is after "name: "
entity_names += re.findall('name: (.*)', hpo_obo)

# The first entity ("All") in the .obo file is special and should be removed from the list of entity names
entity_names.pop(0)

# This looks for all the text that is after "synonym: " and between double quotes
entity_names += re.findall('synonym: "(.*)"', hpo_obo)

# Do some post-processing in the lexicon.
# Lowercase everything
entity_names = map(lambda entity: entity.lower(), entity_names)
# Remove trailing whitespaces (ex: convert "oral ulcer " to "oral ulcer")
entity_names = map(lambda entity: entity.strip(), entity_names)
# Remove duplicates
entity_names = list(set(entity_names))

# Create lexicon file
with open('hpo.txt', 'w') as f:
    for entity_name in entity_names:
        f.write(entity_name + '\n')
