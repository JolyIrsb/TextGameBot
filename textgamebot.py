import telebot
import random

bot = telebot.TeleBot("1078370491:AAHZnEmtvUSx7QSXhWEJbysV5E8U_R98H74")

arthp = 12
witchhp = 20

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	global arthp
	global witchhp
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, напиши /startgame, чтобы начать")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "/startgame - начать игру")
	elif message.text == "/startgame":
		bot.send_message(message.from_user.id, "Добро пожаловать в игру! Твой герой сейчас - КиберРыцарь 1 уровня. HP: 20, Урон: 3-6 единиц.")
		bot.send_message(message.from_user.id, "Твой первый противник - КиберБомж. HP: 12, Урон: 2-4 единицы. Предсмертный хрип: атакует перед смертью.")
		bot.send_message(message.from_user.id, "Твой ход первый! Сейчас ты можешь только бить или использовать свое особое умение: восстановление здоровья на 1-5 единиц.")
		bot.send_message(message.from_user.id, "Напиши Атака или Перк")
	elif message.text == "Атака":
		witchdm = random.randrange(3, 6)
		arthp -= witchdm
		fdm = f'Ты нанес {witchdm} единиц урона КиберБомжу. Здоровье Кибербомжа: {arthp}'
		bot.send_message(message.from_user.id, fdm)
		bot.send_message(message.from_user.id, "Ход КиберБомжа!")
		artdm = random.randrange(2, 6)
		witchhp -= artdm
		sdm = f'Кибербомж нанес тебе {artdm} единиц урона. Твое здоровье: {witchhp}'
		bot.send_message(message.from_user.id, sdm)
	elif message.text == "Перк":
		heal = random.randrange(1, 5)
		witchhp += heal
		fheal = f'Ты похилил себя на {heal} единиц здоровья. Твое здоровье: {witchhp}'
		bot.send_message(message.from_user.id, fheal)
		bot.send_message(message.from_user.id, "Ход КиберБомжа!")
		artdm = random.randrange(2, 6)
		witchhp -= artdm
		sheal = f'Кибербомж нанес тебе {artdm} единиц урона. Твое здоровье: {witchhp}'
		bot.send_message(message.from_user.id, sheal)
	if arthp <= 0:
		bot.send_message(message.from_user.id, "Ты победил! Мои поздравления, пока это все, игра в разработке. /startgame - чтобы сыграть заново.")
		arthp = 12
		witchhp = 20
	if witchhp <= 0:
		bot.send_message(message.from_user.id, "Ты погиб! RIP :(")
		arthp = 12
		witchhp = 20

bot.polling( none_stop = True )
