from flask import Flask, request, jsonify

print("Hello, World!")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'
# act with the flask application
# define a route: a url 
# 127.0.0.1:500/ behind is the get request 
# ? after that is specify parameters to the variable 
# post got no question mark

if __name__ == '__main__':
    app.run(port=5000, debug=True)

#template: 
@app.route('/')
def hello_world():
    return 'Hello, World'

# START FROM HERE!!!!!!!
from flask import Flask, request, jsonify
import sqlite3
import json
import requests

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('ellipsis_hack.db')
cursor = conn.cursor()

@app.route('/get_elderly_details')
def get_elderly_details():
    elderly_list = cursor.execute("SELECT * FROM Elderly")
    for elderly in elderly_list:
        ElderlyID, FirstName, LastName, DOB, Address, PhoneNumber, Email, CreatedAt = elderly
    return elderly_list

@app.route('/get_caregiver_details')
def get_caregiver_details():
    caregiver_list = cursor.execute("SELECT * FROM Caregivers")
    for caregiver in caregiver_list:
        CaregiverID, FirstName, LastName, PhoneNumber, Email, Expertise, CreatedAt = caregiver
    return caregiver_list

@app.route('/get_service_details')
def get_service_details():
    service_list = cursor.execute("SELECT * FROM Services")
    for service in service_list:
        ServiceID, ServiceName, Description, CategoryID, CreatedAt = service
    return service_list

@app.route('/get_servicecatergory_details')
def get_servicecategory_details():
    service_list = cursor.execute("SELECT * FROM ServiceCategories")
    for service in service_list:
        ServiceID, ServiceName, Description, CategoryID, CreatedAt = service
    return service_list

@app.route('/get_servicerecords_details')
def get_servicerecords_details():
    service_records = cursor.execute("SELECT * FROM ServiceRecords")
    for service_record in service_records:
        RecordID, ElderlyID, CaregiverID, ServiceID, ServiceDate = service_record
    return service_records

@app.route('/match_nearest_caregiver')
def match_nearest_caregiver():
    nearest_caregiver = None
    min_distance = 0
    elderly_list = get_elderly_details
    address_list = []
    for elderly in elderly_list:
        address = elderly['Address']
        address_list.append(address)
    for address in address_list:

if __name__ == '__main__':
    app.run(port=5000, debug=True)



