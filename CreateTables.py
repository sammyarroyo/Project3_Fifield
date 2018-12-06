from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float
import csv
import pandas as pd

#Opening/Reading of CSV data, creation of engine, and extraction of metadata
csvdata = open("/ufrc/zoo6927/share/fifield/Lost__found__adoptable_pets_no_duplicate_IDs.csv")
reader = csv.DictReader(csvdata)
engine = create_engine('sqlite:///./Project3DB.sqlite')
metadata = MetaData(engine)


#Opening of Tables if they are already available, Setting up schema of tables if they are not yet created
try:
        StaffInfo = Table('StaffInfo', metadata, autoload=True)
except:
        StaffInfo = Table('StaffInfo', metadata,
                Column('Impound_No', String),
                Column('Animal_ID', String, primary_key=True),
                Column('Address', String),
                Column('City', String),
                Column('State', String),
                Column('Zip_Code', Integer),
                Column('Jurisdiction', String),
                Column('Latitude', String),
                Column('Longitude', String),
                Column('Memo', String)
                )

try:
        GuestInfo = Table('GuestInfo', metadata, autoload=True)
except:
        GuestInfo = Table('GuestInfo', metadata,
                Column('Animal_IDg', String, ForeignKey("StaffInfo.Animal_ID")),
                Column('Record_Type', String),
                Column('Link', String),
                Column('Current_Location', String),
                Column('Animal_Name', String),
                Column('Animal_Type', String),
                Column('Age', String),
                Column('Animal_Gender', String),
                Column('Animal_Breed', String),
                Column('Animal_Color', String),
                Column('Image', String),
                Column('Temperament', String),
                )

#Creation of tables within the database
metadata.create_all(engine)

#check that both tables were created
for t in metadata.sorted_tables:
        print(t.name)

#Open the data and connect to the data
csvdata = open("ufrc/zoo6927/share/fifield/Lost__found__adoptable_pets_no_duplicate_IDs.csv")
conn = engine.connect()

#Insert the data from the original data file into the new tables in the database in the correct columns
reader= csv.DictReader(csvdata)
for Line in reader:

        ins=StaffInfo.insert().values(Impound_No=Line['impound_no'],
                                        Animal_ID=Line['Animal_ID'],
                                        Address=Line['Obfuscated_Address'],
                                        City=Line['City'],
                                        State=Line['State'],
                                        Zip_Code=Line['Zip'],
                                        Jurisdiction=Line['jurisdiction'],
                                        Latitude=Line['obfuscated_latitude'],
                                        Longitude=Line['obfuscated_longitude'],
                                        Memo=Line['Memo']
                                        )
        ins2=GuestInfo.insert().values(Animal_IDg=Line['Animal_ID'],
                                        Record_Type=Line['Record_Type'],
                                        Link=Line['Link'],
                                        Current_Location=Line['Current_Location'],
                                        Animal_Name=Line['Animal_Name'],
                                        Animal_Type=Line['animal_type'],
                                        Age=Line['Age'],
                                        Animal_Gender=Line['Animal_Gender'],
                                        Animal_Breed=Line['Animal_Breed'],
                                        Animal_Color=Line['Animal_Color'],
                                        Image=Line['Image'],
                                        Temperament=Line['Temperament']
                                       )

        result = conn.execute(ins)
        result2 = conn.execute(ins2)
