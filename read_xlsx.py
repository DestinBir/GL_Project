from openpyxl import load_workbook

PATH = "format.xlsx" #Variable pour stoquer l'emplacement du fichier. il sera récupere dans un widget
NAME_PROMOTION = "Bac3 Info GL" #varible pour savoir la promotion gérer par le sécretaire du jury


def excel_to_list_of_dictionaries(file_path, sheet_name=None):
	"""
		Transfomer une feuille excel en dictionnaire afin d'étudier ces données
	"""
	wb = load_workbook(PATH)

	for sheet in wb.sheetnames:
		if sheet.lower() == NAME_PROMOTION.lower():
			sheet_active = wb[sheet]
			start_up = 1
			header = []
			data=[]
			data_dict={}
			for row in sheet_active.iter_rows():
				for i, cell in enumerate(row):
					if start_up == 1:
						header.append(cell.value.lower())
					else:
						data_dict[header[i]]=cell.value
				data.append(data_dict)
				start_up=0
	return data

def filter_fonction(data):
	"""
	supprimer les données dont la matricule, le nom ou le prénom serait absente
	"""
	for i in data.copy():
		if i["matricule"]==None or i["nom"]==None or i["prenom"]==None:
			data.remove(i)
	return data

data = excel_to_list_of_dictionaries(PATH, NAME_PROMOTION)

data_filter =filter_fonction(data)
print(data_filter)