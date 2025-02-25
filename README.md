# Google-Calendar-Time-Slot-Automator
automates event creation in Google Calendar when the event title remains the same but the date and time vary. This tool helps streamline scheduling by reducing manual input and ensuring accuracy.

## Features

- Ideal for users who need to add events with the same title on different dates and times each month.
- For example, this month you may have events on the 2nd, 3rd, and 4th, while next month you may have them on the 12th, 21st, and 30th, but the event title remains consistent.
- Once configured, multiple events can be easily added for different dates, making it efficient for managing recurring schedules.

## Requirements

- Google Service Account Key
- Libraries: `google-auth`, `google-api-python-client`, `python-dotenv`

## Setup

1. Create a Google Service Account and download the JSON key file.
2. Create a `.env` file and add the following information:
   ```
   GOOGLE_CALENDAR_ID=<Google calendar id | Most users probably use Gmail>
   GOOGLE_AUTH_PATH=<path to Google service account key>.json
   ```
3. Install the required Python libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `Set the date and time` section in the script to define event dates and times.
2. Modify the `Event title` to set an appropriate title.
3. Run the script to add events to your specified Google Calendar:
   ```sh
   python main.py
   ```

## Customization

- You can specify multiple dates in `dates_and_times` to create multiple events at once.
- Change `colorId` to modify the event color.

## Notes

- Ensure that the `.env` file correctly specifies the path to the Google Service Account Key.
- Set up Google Calendar API authentication properly.
- Test thoroughly in a safe environment to avoid unintended bulk event creation.

---

This script allows you to effortlessly add recurring events to Google Calendar. Feel free to customize it as needed.
