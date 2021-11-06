from logging import debug
from pprint import pprint

import flask
from flask.json import jsonify

from Google import Create_Service
from flask import Flask ,request




# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

event = {
  'summary': '[Vaccine appointment] NGAI MEI FONG (+60) 126995668',
  #'location': '800 Howard St., San Francisco, CA 94103',
  'description': '[Dr Chan Klk Xian ] NGAI MEI FONG \n contact:(+60) 126995668. \n ClinicComments:HEP B 3RD DOSE \n this is a Existing patient',
  'creator':{'email':'medlotfi.omar@esprit'},
  'colorId':5,
  'start': {
    'dateTime': '2021-12-16T06:00:00-00:00',
    #'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2021-12-16T06:15:00-00:00',
    #'timeZone': 'America/Los_Angeles',
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 48 * 60},
      {'method': 'popup', 'minutes': 48 * 60},
    ],
  },
}
app=Flask(__name__)
@app.route('/getEventList',methods=['GET'])
def getEvents():
 Client_Sercret_File='Client_Secret.json'
 API_NAME='calendar'
 API_VERSION = 'v3'
 SCOPES=['https://www.googleapis.com/auth/calendar']
 agenda_id='c_classroom2b634909@group.calendar.google.com'
 service = Create_Service(Client_Sercret_File,API_NAME,API_VERSION,SCOPES)
 page_token = None
 while True:
  events = service.events().list(calendarId='medlotfi.omar@esprit.tn', pageToken=page_token).execute()
  return (events)
@app.route('/insertEvent',methods=['POST'])
def addEvents():
 Client_Sercret_File='Client_Secret.json'
 API_NAME='calendar'
 API_VERSION = 'v3'
 SCOPES=['https://www.googleapis.com/auth/calendar']
 agenda_id='c_classroom2b634909@group.calendar.google.com'
 service = Create_Service(Client_Sercret_File,API_NAME,API_VERSION,SCOPES)
 event_obj = request.get_json()
 event = service.events().insert(calendarId='medlotfi.omar@esprit.tn', body=event_obj).execute()
 return jsonify({"messgae":event['summary']})
if __name__ =="__main__":
  app.run(debug=True,port=8000)
  