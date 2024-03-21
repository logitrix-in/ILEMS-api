import csv

from analytics.models import Chargesheet

from datetime import datetime


def format_date(original_date_str):
    try:
        date_obj = datetime.strptime(original_date_str, "%d-%m-%Y")
        converted_date_str = date_obj.strftime("%Y-%m-%d")
        return converted_date_str
    except ValueError:
        return None


csv_file_path = 'data.csv'


with open(csv_file_path, mode='r', encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        db = Chargesheet.objects.create(
            District_Name=i['District_Name'],
            UnitName=i['UnitName'],
            FIRNo=i['FIRNo'],
            RI=i['RI'],
            Year=i['Year'],
            Month=i['Month'],
            FIR_Date=format_date(i['FIR_Date']),
            Report_Date=format_date(i['Report_Date']),
            Final_Report_Date=format_date(i['Final_Report_Date']),
            Report_Type=i['Report_Type'],
            FR_ID=i['FR_ID']
        )
        print("Processed Document: ", db.id)
