from background_task import background
from django.template.loader import render_to_string
from .models import Request
import requests
from Requests.settings import TOKEN_BOT, CHAT_ID


@background(schedule = 0)
def send_telegram_message_async(i_pk):
    data = Request.objects.get(pk = i_pk)
    message = render_to_string('bot/bot.html', {'i': data})
    chat_id = CHAT_ID
    token = TOKEN_BOT
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    response = requests.post(url,
                             json={
                                 'chat_id': chat_id,
                                 'text': message,
                                 'parse_mode': 'HTML'
                             },
                             timeout=20)

    return response.json()