from suncraft_parsing import line, admin_url, import_handeling, catsubtag_block, list_groups_as_string, name, description, string_it, file_saving, meta_data, meta_name, part, upc
from suncraft_varriables import suncraft_database_file, looking_for, type_of_group



def read_it_all(imported_dict, body = "", all_cat = set(), all_subcat = set(), all_tags = set()):

    # This part is the body of the document and how it's formatted
    for pages_id in sorted(imported_dict, key = lambda pages_id: int(imported_dict[pages_id]["rank"])):
        product_page = "" # This holds the information for this loop don't remove it
        part_name_length = 0
        for i in part(imported_dict, pages_id, False):
            if len(i) > part_name_length:
                part_name_length = len(i)

        all_cat.update(list_groups_as_string(imported_dict, pages_id,"Categories", False))
        all_subcat.update(list_groups_as_string(imported_dict, pages_id,"subcategories", False))
        all_tags.update(list_groups_as_string(imported_dict, pages_id,"tags", False))

        meta_name_list = meta_name(imported_dict, pages_id, False, "- ")
        meta_data_list = meta_data(imported_dict, pages_id, False)
        meta_dict = dict(zip(meta_name_list, meta_data_list))

        upc_list = upc(imported_dict, pages_id, False)
        part_list = part(imported_dict, pages_id, False)
        parts_dict = dict(zip(part_list, upc_list))


        #Page
        product_page += \
            line(30) +\
            f'Name: {name(imported_dict, pages_id)}\n' +\
            line(30) +\
            catsubtag_block(imported_dict, pages_id) +\
            line(30) +\
            f'Description: {description(imported_dict, pages_id)}' + "\n" +\
            line(30) +\
            f'| UPC | {str.center("Part", part_name_length)}|  Info\n' +\
            line(30)

        for i in parts_dict:
            try:
                product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_length + 1)} {meta_dict[i]}\n')
            except KeyError:
                product_page += (f'|{parts_dict[i]}| {str.rjust(i + "|", part_name_length + 1)}\n')

        product_page += f'\n'
        body += product_page 

    body += "Categories: " + string_it(all_cat) + "\n"
    body += "Subcategories: " + string_it(all_subcat) + "\n"
    body += "Tags: " + string_it(all_tags) + "\n"

    return body
    # Creates and/or opens the file to work with.


# # Variables
# file_name_prefix = "all"
# imported_dict = import_handeling(suncraft_database_file, False)
# body = read_it_all(imported_dict)
# file_saving(f'{file_name_prefix}_{suncraft_database_file.split(".")[0]}', body)

