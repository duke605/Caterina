from slackclient import SlackClient
from datetime import datetime, timedelta
import requests, json, time

MENU_URL = ''
TOKEN = ''
API_URL = 'https://slack.com/api'

EARLY_WARN = 10
SECOND_WARN = 11

while True:
    dt = datetime.now()

    if dt.hour < EARLY_WARN:
        time.sleep(int((dt.replace(hour=EARLY_WARN, minute=0, second=0, microsecond=0) - datetime.now()).total_seconds()))
    elif dt.hour < SECOND_WARN:
        time.sleep(int((dt.replace(hour=SECOND_WARN, minute=0, second=0, microsecond=0) - datetime.now()).total_seconds()))
    else:
        time.sleep(int(((dt + timedelta(days=1)).replace(hour=EARLY_WARN, minute=0, second=0, microsecond=0) - datetime.now()).total_seconds()))


    with requests.get(MENU_URL) as r:
        fields = r.json()['items'][0]['fields']

    data = {
        'token': TOKEN,
        'channel': 'C7GHFJV61',
        'attachments':  json.dumps([
            {
                'author_name': fields['caterer'],
                'author_link': 'http://www.urbanprairiecuisine.com/',
                'fields': [{'title': key.capitalize(), 'value': '\n'.join(value), 'short': False} for key, value in fields.items() if isinstance(value, list)]
            }
        ])
    }

    with requests.post(f'{API_URL}/chat.postMessage', data=data) as r:
        pass
