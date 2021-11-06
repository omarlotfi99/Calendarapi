# Calendarapi
calendar api with flask 
1/run the server by taping "python API.py" and open postman to test the api 
#posting an event
2/run the following api path on postman http://127.0.0.1:8000/insertEvent and choose the POST method and put the following Json object in the body: 

{
  "summary": "[Vaccine appointment]  NGAI MEI FONG (+60) 126995668",
  "location": "800 Howard St., San Francisco, CA 94103",
  "description": "[Dr Chan Klk Xian ] NGAI MEI FONG \n contact:(+60) 126995668. \n ClinicComments:HEP B 3RD DOSE \n this is a Existing patient",
  "creator":{"email":"medlotfi.omar@esprit"},
  "colorId":5,
  "start": {
    "dateTime": "2021-12-16T06:00:00-00:00",
    "timeZone": "America/Los_Angeles"
  },
  "end": {
    "dateTime": "2021-12-16T06:15:00-00:00",
    "timeZone": "America/Los_Angeles"
  },
  "reminders": {
    "useDefault": "False",
    "overrides": [
      {"method": "email", "minutes": 2880},
      {"method": "popup", "minutes":2880}
    ]
  }
}

3/run the following api path on post man http://127.0.0.1:8000/getEventList and choose the GET method: 
this witll return all the events of a specific calendar 

