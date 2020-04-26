# Ramzan Calendar
This script will create Sehar-o-Aftar events in calendar, so you can get the notification just like your meeting, 
also you can see times on daily baises.

### Project Setup
* Download and install Git - [Official Download Link](https://git-scm.com/downloads)
* Install Python 3 - [Official Download Link](https://www.python.org/downloads/)

```bash
# Clone the Project
git clone git@github.com:malikshahzad228/ramzan_calendar.git
# Get into project directory
cd ramzan_calendar
# Make Virtual Env with python 3
python3 -m venv
# Activate Virtual Env
source venv/bin/activate
# Install requirements
pip install -r requirements.txt
``` 


### Things to do first
- Create a calendar and get the calendarId, which will be replaced at ramzan_calendar.py:45
- Make an application in Google apps, get the `credentials.json` paste that file in this folder.


### Run the script
Run with command
```bash
python ramzan_calendar.py
```
