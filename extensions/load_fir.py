import csv

from analytics.models import FIR

def format_date(original_date_str):
    from datetime import datetime

# Original date string in dd-mm-yyyy format
    

    # Convert the original date string to a datetime object
    date_obj = datetime.strptime(original_date_str, "%d-%m-%Y")

    # Format the datetime object to a string in yyyy-mm-dd format
    converted_date_str = date_obj.strftime("%Y-%m-%d")

    # print(converted_date_str)
    return converted_date_str


# Path to your CSV file
csv_file_path = 'data.csv'

# Read the CSV file and convert it into a list of dictionaries
with open(csv_file_path, mode='r',encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    # Convert to a list of dictionaries
    for i in csv_reader:
        # print(i)
        
        db = FIR.objects.create(
            fir_no=i['FIRNo'],
            district=i['District_Name'],
            unit_name=i['UnitName'],
            
            year=i['Year'],
            month=i['Month'],
            
            registered_on=format_date(i['FIR_Date']),
            fir_type=i['FIR Type'],
            fir_stage=i['FIR_Stage'],
            complaint_mode=i['Complaint_Mode'],
            crime_group_name=i['CrimeGroup_Name'],
            crime_head_name=i['CrimeHead_Name'],
            latitude=i['Latitude'],
            longitude=i['Longitude'],
            ActSection=i['ActSection'],
            IOName=i['IOName'],
            KGID=i['KGID'],
            IOAssigned_Date=i['IOAssigned_Date'] if i['IOAssigned_Date'] != "NULL" else None,
            Internal_IO=i['Internal_IO'],
            Place_of_Offence=i['Place of Offence'],
            distance_from_ps=i['Distance from PS'],
            Beat_Name=i['Beat_Name'],
            Village_Area_Name=i['Village_Area_Name'],
            Male=float(i['Male']),
            Female=float(i['Female']),
            Girl=float(i['Girl']),
            Age=float(i['Age 0']),
            VICTIM_COUNT=float(i['VICTIM COUNT']),
            ACCUSED_COUNT=float(i['Accused Count']),
            Arrested_Male=float(i['Arrested Male']),

        )
        
        print("Processing...")




