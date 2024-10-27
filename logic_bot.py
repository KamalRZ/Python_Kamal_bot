from newkamal import bot

def hehehehehe(message):
    a = message.text.split()
    if len(a)-1 and a[1].isdigit():
        bot.reply_to(message, "he"*int(a[1]))
    else:
        bot.reply_to(message, "he"*5)



def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

def send_bye(message):
    bot.reply_to(message, random.choice(["пока", "ещё встретимся"]))


def send_mem(message):
    with open(f'images/{random.choice(os.listdir("images"))}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
def get_image_url():
        url = random.choice(['https://random-d.uk/api/random'])
        res = requests.get(url)
        data = res.json()
        return data['url']



def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения'''
    image_url = get_image_url()
    bot.reply_to(message, image_url)


def ecolog(m):
    bot.reply_to(m, random.choice(["https://turclub-pik.ru/blog/chto-ya-mogu-sdelat-dlya-ehkologii-30-sposobov/",
                                   "https://ru.wikihow.com/жить-с-заботой-об-окружающей-среде",
                                   "https://ru.wikihow.com/дети-могут-помочь-защитить-окружающую-среду",
                                   "https://ecologyofrussia.ru/lifehack/priroda-dlya-detey/",
                                   "https://avatars.mds.yandex.net/i?id=06a6b1f46a40ce1f446b318438d0436e0d637516-9151019-images-thumbs&n=13",
                                   "https://avatars.mds.yandex.net/i?id=43d83b7758a694a5cdbd6ae408a086659a7f169b-7952541-images-thumbs&n=13",
                                   "https://avatars.mds.yandex.net/i?id=33afe99cbe4df9bba0fc70bcba0afefe141ac428-4591508-images-thumbs&n=13",
                                   "https://cdn.culture.ru/images/cb7707de-f76c-5e2e-9950-d7cc1df66b4f"]))

def send_welcome(message):
    bot.reply_to(message, """Привет! Я твой Telegram бот. мои команды:
            команда(-ы)     |                    объяснение
____________________________|______________________________
help, start                 |помощь по командам
mem                         |присылает мем
hello                       |приветствие
bye                         |прощание
duck                        |присылает картинку с утками
ecolog                      |помогает стать экологом
""")