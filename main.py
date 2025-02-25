import datetime
import googleapiclient.discovery
import google.auth
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Retrieve information from environment variables
SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = os.getenv("GOOGLE_CALENDAR_ID")
auth_path = os.getenv("GOOGLE_AUTH_PATH")

# Load Google API authentication
gapi_creds = google.auth.load_credentials_from_file(auth_path, SCOPES)[0]

# Create a resource object for the API
service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)

# Set the date and time (as an example, we will create an event for February 3, 2025)
year = 2025
month = 2
dates_and_times = [
    {"days": [3,3,3], "range_time": [[10, 0], [15, 0]]},
    {"days": [3], "range_time": [[10, 0], [13, 0]]},
]
timezone = 'Japan' # Timezone
colorId = "10"  # Green

for date_time in dates_and_times:
    days = date_time["days"]
    range_time = date_time["range_time"]
    
    for day in days:
        range_hours = range_time[1][0] - range_time[0][0]
        if range_hours >= 6:
            range_time_end = range_time[1][0] + 1
            range_hours = f"{range_hours}+1"
        else:
            range_time_end = range_time[1][0]
        range_length = range_time_end - range_time[0][0] + abs(range_time[1][1] - range_time[0][1]) / 60
        
        body = {
            "summary": f"({range_length}h) Working at home", # Event title
            "start": {
                "dateTime": datetime.datetime(year, month, day, range_time[0][0], range_time[0][1]).isoformat(),
                "timeZone": timezone
            },
            "end": {
                "dateTime": datetime.datetime(year, month, day, range_time_end, range_time[1][1]).isoformat(),
                "timeZone": timezone
            },
            "colorId": colorId
        }

        # Insert the event into Google Calendar
        event = service.events().insert(calendarId=calendar_id, body=body).execute()
