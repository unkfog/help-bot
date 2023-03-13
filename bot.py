import telebot

bot = telebot.TeleBot('6216965118:AAEN7XxFCX0eYO8yoYHdmRSC2u84abEgYC8')



@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,'Привет,' + str(message.from_user.first_name)+' этот бот будет пытатся помочь в програмирование python\n/help - команды')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'/video - тут будут собраны видео которые помогут тебе в изучение\n/website - сайты с статьями по изучению\n/book - книги\n/apps - приложения\n/wish - пожелания от автора')

@bot.message_handler(commands=['video'])
def video(message):
    bot.send_message(message.chat.id,'/detailed - для подробного изучения\n/short - уроки которые объясняют вкратце основы')

@bot.message_handler(commands=['detailed'])
def detailed(message):
    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=5g-MHZ0MzZY&t=2s&ab_channel=PythonHubStudio \n это видео сам я не смотрел,однако много положительных комментариев \n/next_video для просмотра следующего видео ')

@bot.message_handler(commands=['next_video'])
def next_video(message):
    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=cr_3evPrzsU&t=21249s&ab_channel=BogdanStashchuk \n тоже самое что и с прошлым')

@bot.message_handler(commands=['short'])
def short(message):
    bot.send_message(message.chat.id,'https://www.youtube.com/playlist?list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY \nэтот мини-курс я и сам смотрел,как по мне человек понятно объясняет всё')

@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id,'https://pythonworld.ru/samouchitel-python \n если хотите учить или закрепить знания по пайтону,то сайт давольно хорош')

@bot.message_handler(commands=['book'])
def book(message):
    bot.send_message(message.chat.id,'https://oz.by/books/more10569541.html \n данная книга помогает вам с пониманием алгоритмов,книжка довольно таки интересная,а самое главное лёгкая в обучение(автор бота досих пор читает её=))')

@bot.message_handler(commands=['apps'])
def apps(message):
    bot.send_message(message.chat.id,'https://play.google.com/store/apps/details?id=com.getmimo\nздесь будут целые уроки для изучения\n/next_apps -для просмотра следующего приложения')

@bot.message_handler(commands=['next_apps'])
def next_apps(message):
    bot.send_message(message.chat.id,'https://play.google.com/store/apps/details?id=ru.pythono.pythono&hl=ru&gl=US\nизучение пайтона по порядку')

@bot.message_handler(commands=['wish'])
def wish(message):
    bot.send_message(message.chat.id,'я надеюсь этот бот помог и понравился тебе!желаю успехов в изучение,главное не спеши')

if __name__ == '__main__':
     bot.infinity_polling()

