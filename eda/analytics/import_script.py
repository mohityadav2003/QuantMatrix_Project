import csv
from datetime import datetime
from analytics.models import RetailData  # Change 'yourapp' to your actual app name
from django.db import transaction

def float_or_none(val):
    try:
        return float(val)
    except:
        return None

@transaction.atomic
def import_retail_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')  # Use ',' if CSV is comma-separated
        print(reader.fieldnames)  # to double-check columns

        count = 0
        for row in reader:
            try:
                RetailData.objects.create(
                    Market=row['Market'],
                    Channel=row['Channel'],
                    Region=row['Region'],
                    Category=row['Category'],
                    SubCategory=row['SubCategory'],
                    Brand=row['Brand'],
                    Variant=row['Variant'],
                    PackType=row['PackType'],
                    PPG=row['PPG'],
                    PackSize=row['PackSize'],
                    Year=int(row['Year']),
                    Month=int(row['Month']),
                    Week=int(row['Week']),
                    Date=datetime.strptime(row['Date'], "%d-%m-%Y %H:%M"),
                    BrCatId=row['BrCatId'],
                    SalesValue=float(row['SalesValue']),
                    Volume=float(row['Volume']),
                    VolumeUnits=row['VolumeUnits'],

                    D1=float_or_none(row['D1']),
                    D2=float_or_none(row['D2']),
                    D3=float_or_none(row['D3']),
                    D4=float_or_none(row['D4']),
                    D5=float_or_none(row['D5']),
                    D6=float_or_none(row['D6']),

                    AV1=float_or_none(row['AV1']),
                    AV2=float_or_none(row['AV2']),
                    AV3=float_or_none(row['AV3']),
                    AV4=float_or_none(row['AV4']),
                    AV5=float_or_none(row['AV5']),
                    AV6=float_or_none(row['AV6']),

                    EV1=float_or_none(row['EV1']),
                    EV2=float_or_none(row['EV2']),
                    EV3=float_or_none(row['EV3']),
                    EV4=float_or_none(row['EV4']),
                    EV5=float_or_none(row['EV5']),
                    EV6=float_or_none(row['EV6']),

                    PrepDate=datetime.strptime(row['PrepDate'], "%d-%m-%Y %H:%M"),

                )
                count += 1
            except Exception as e:
                print(f"❌ Error on row {count + 1}: {e}")

        print(f"✅ Successfully imported {count} rows.")