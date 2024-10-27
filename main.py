import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, '''Привет! Я бот, который рассказывает советы по экологии\n\n
        Мои команды: \n\n
        \sort <наименование мусора для утелизациии>
        \\time <нименование предмета>
        '''
        )
    
@bot.message_handler(commands=['sort'])
def send_item(message):
    key = telebot.util.extract_arguments(message.text).lower()
    list_utils = ['телевизор', 
                  'баторейки',
                  'батарейка',
                  'пылесос',
                  'аккамуляторы', 
                  'шины', 
                  'нефтепродукты', 
                  'градусник', 
                  'медецинские отходы']
    if key in list_utils:
        bot.send_message(message.chat.id, f'{key} необходимо отдать на перероботку')
    else:
        bot.send_message(message.chat.id, f'{key} можно выбросить в мусорку')

@bot.message_handler(commands=['time'])
def time_item(message):
    key  = telebot.util.extract_arguments(message.text).lower()
    decompose_items = {
        'пластиковая бутылка': '450 лет',
        'стеклянная бутылка': '1-2 миллиона лет',
        'бумага': '2-5 лет',
        'картон': '1-3 года',
        'книга': '50-100 лет',
        'журнал': '10-50 лет',
        'резиновая покрышка': '50-80 лет',
        'батарейки': '1-5 лет',
        'аккумуляторы': '5-10 лет',
        'телевизор': '100-500 лет',
        'пылесос': '100-500 лет',
        'нефтепродукты': '100-500 лет',
        'градусник': '100-500 лет',
        'медицинские отходы': '100-500 лет',
        'банановая кожура': '2-5 недель',
        'полиэтиленовый пакет': '10-20 дет'
    }
    if key in decompose_items:
        bot.send_message(message.chat.id, f'время разложения {key}:  {decompose_items[key]}')
    else:
        bot.send_message(message.chat.id, f'время разложения {key} неизвестно')


bot.infinity_polling()
