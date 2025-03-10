from suncraft_parsing import items_block, live_url, admin_url, import_handeling, catsubtag_block, list_groups_as_string


# Variables
parsed_file_name = "stats"
suncraft_database_file = "SClist_2023_07_25_08:19AM.json"
imported_dict = import_handeling(suncraft_database_file, False)
def undline(string):
    underlined = ""
    underlined += f'\n{string}\n{"-" * len(string)}\n'
    return underlined

body = "" 
all_cat = set()
all_subcat = set()
all_tags = set()

# Creates and opens the file to work with.
write_to_this_file = f'{parsed_file_name}_{suncraft_database_file.split(".")[0]}.txt'
working_file = open(write_to_this_file, "w")



# This part is the body of the document and how it's formatted
for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
    all_cat.update(list_groups_as_string(imported_dict, pages_id,"Categories",False))
    all_subcat.update(list_groups_as_string(imported_dict, pages_id,"subcategories", False))
    all_tags.update(list_groups_as_string(imported_dict, pages_id,"tags", False))

    items_block(imported_dict, pages_id)

body += undline("Catagories:")
for i in all_cat:
    body += i + "\n"

body += "\n" + undline("Subcatagories:")
for i in all_subcat:
    body += i + "\n"

body += "\n" + undline("Tags:")
for i in all_tags:
    body += i + "\n"


# Writes and closes the file and indicates that the task is compleate
working_file.write(body)
working_file.close()
print(f'\nDone: {write_to_this_file} has been saved\n')



