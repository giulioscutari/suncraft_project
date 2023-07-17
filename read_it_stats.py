from suncraft_parsing import items_block, live_url, admin_url, file_handeling, catsubtag_block, tags, subcat, cat


# Variables
parsed_file_name = "stats"
suncraft_database_file = "SClist_2023_07_17_08:13AM.json"
imported_dict = file_handeling(suncraft_database_file, False)

body = "" 
all_cat = set()
all_subcat = set()
all_tags = set()

# Creates and opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")



# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    all_cat.update(cat(imported_dict, pages_id, False))
    all_subcat.update(subcat(imported_dict, pages_id, False))
    all_tags.update(tags(imported_dict, pages_id, False))

body += "Catagories:\n"
for i in all_cat:
    body += i + "\n"

body += "\nSubcatagories:\n"
for i in all_subcat:
    body += i + "\n"

body += "\nTags:\n"
for i in all_tags:
    body += i + "\n"


# Writes and closes the file and indicates that the task is compleate
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')


