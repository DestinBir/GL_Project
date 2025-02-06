from openpyxl import load_workbook

PATH = "format.xlsx" #Variable pour stoquer l'emplacement du fichier. il sera récupere dans un widget
NAME_PROMOTION = "Bac3 Info GL" #varible pour savoir la promotion gérer par le sécretaire du jury


from openpyxl import load_workbook

def excel_to_list_of_dictionaries(file_path, sheet_name=None):
    """
    Transforms an Excel sheet into a list of dictionaries to analyze the data.
    """
    wb = load_workbook(file_path)

    sheet_active = None
    if sheet_name:
        if sheet_name.lower() in [sheet.lower() for sheet in wb.sheetnames]:
            sheet_active = wb[sheet_name]
    else:
        sheet_active = wb.active  # Use active sheet if no name is provided

    if not sheet_active:
        raise ValueError("Sheet not found")

    header = []
    data = []
    
    for row_index, row in enumerate(sheet_active.iter_rows(), start=1):
        data_dict = {}
        for i, cell in enumerate(row):
            if row_index == 1:
                # First row: header
                header.append(cell.value.lower())
            else:
                data_dict[header[i]] = cell.value
        if row_index != 1:  # Skip adding an empty dictionary for the header row
            data.append(data_dict)

    return data

def filter_fonction(data):
	"""
	supprimer les données dont la matricule, le nom ou le prénom serait absente
	"""
	for i in data.copy():
		if i["matricule"]==None or i["nom"]==None or i["prenom"]==None:
			data.remove(i)
	return data

def 