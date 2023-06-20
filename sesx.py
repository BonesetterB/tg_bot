import requests
id_sss="1325062977"
TOKEN="5815046882:AAEda4DeKsDr3N2TadHINxuqW_De1CwYONc"
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getChat?chat_id={id_sss}')
data = response.json()
chat_id = data['result']['id']
print(f"\n Айді корго там чат сЕКС воот {chat_id}")

def send_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, params)
    if response.status_code == 200:
        print('Повідомлення успішно надіслано!')
    else:
        print('Помилка при надсиланні повідомлення.')

# Використання функції для надсилання повідомлення
message = 'Привіт, це приклад повідомлення!'  # Замініть 'Привіт, це приклад повідомлення!' на ваше власне повідомлення
send_message(TOKEN, chat_id, message)