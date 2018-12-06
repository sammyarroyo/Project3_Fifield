from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float
import csv
import pandas as pd

#Opening/Reading of CSV data, creation of engine, and extraction of metadata
csvdata = open("./Lost__found__adoptable_pets_no_duplicate_IDs.csv")
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
