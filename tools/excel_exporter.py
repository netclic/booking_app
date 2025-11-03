from openpyxl import Workbook

def export_to_excel(data, filename="export.xlsx"):
    """Exporter des données vers Excel."""
    workbook = Workbook()
    sheet = workbook.active

    # Ajouter les données ligne par ligne (exemple de données = liste de tuples)
    for row in data:
        sheet.append(row)

    # Sauvegarder le fichier Excel
    workbook.save(filename)
    print(f"Exporté vers {filename}")