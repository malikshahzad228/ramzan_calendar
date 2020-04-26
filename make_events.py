import csv
from datetime import datetime, timedelta

GMT_OFF = '+05:00'
LOCATION = 'Bahawalpur, Punjab, PK 63100'
TIME_ZONE = 'Asia/Karachi'
SEHAR_SUMMARY_TEMPLATE = '{}: Sahr Time {}'
AFTAR_SUMMARY_TEMPLATE = '{}: Aftar Time {}'
DESCRIPTION = 'Ramadan timing for Bahawalpur according to Fiqah e Hanafi/Shafi'


def get_events():
    events = list()

    with open('timings.csv', mode='r', encoding='utf-8-sig') as csv_file:
        _reader = csv.DictReader(csv_file)

        for file_data in _reader:

            sehar_start_time = '{} {}:{}:00'.format(file_data['date'], file_data['sehar_h'], file_data['sehar_m'])
            sehar_start_time = datetime.strptime(sehar_start_time, '%Y-%m-%d %H:%M:%S')
            sehar_end_time = sehar_start_time + timedelta(minutes=10)

            aftar_start_time = '{} {}:{}:00'.format(file_data['date'], file_data['aftar_h'], file_data['aftar_m'])
            aftar_start_time = datetime.strptime(aftar_start_time, '%Y-%m-%d %H:%M:%S')
            aftar_end_time = aftar_start_time + timedelta(minutes=10)

            sehar_event = {
                'summary': SEHAR_SUMMARY_TEMPLATE.format(file_data['no'], sehar_start_time.strftime('%I:%M %p')),
                'location': LOCATION,
                'description': DESCRIPTION,
                'start': {
                    'dateTime': sehar_start_time.strftime('%Y-%m-%dT%H:%M:%S+05:00'),
                    'timeZone': TIME_ZONE
                },
                'end': {
                    'dateTime': sehar_end_time.strftime('%Y-%m-%dT%H:%M:%S+05:00'),
                    'timeZone': TIME_ZONE,
                },
            }

            aftar_event = {
                'summary': AFTAR_SUMMARY_TEMPLATE.format(file_data['no'], aftar_start_time.strftime('%I:%M %p')),
                'location': LOCATION,
                'description': DESCRIPTION,
                'start': {
                    'dateTime': aftar_start_time.strftime('%Y-%m-%dT%H:%M:%S+05:00'),
                    'timeZone': TIME_ZONE,
                },
                'end': {
                    'dateTime': aftar_end_time.strftime('%Y-%m-%dT%H:%M:%S+05:00'),
                    'timeZone': TIME_ZONE,
                },
            }

            events.append(sehar_event)
            events.append(aftar_event)

    return events
