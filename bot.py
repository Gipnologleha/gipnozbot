#😱 😉 😃 😅 😞 😭 😐 👍 😌 🤨 🧐 🤓 😎 😄 😁 🤯 😶 🤝 ✊ 🙌 👏 🤏 👆 🎃 😷 🤒 🤕 🤧 🤐 🙋‍♂️ 🙅‍♂️ 💧 💦 ❄️ 🌨 🌩 ⛈ 🌧 🌈 ☀️ ⚡️ 💥 🌝 🌒 🌚 😴 🥱 🤤 😦 😯 😑 😐 🤔 🤗😵🔬🖊🔎📎⬅️➡️⬆️⬇️↗️↘️↙️↖️
import telebot
import config
import random 
from telebot import types


bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):

    sti = open('/home/lex/freud.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
    item2 = types.InlineKeyboardButton("о гипнозе💬", callback_data='hypnosis')
    item3 = types.InlineKeyboardButton("психисоматика🤔", callback_data='bad')
    item4 = types.InlineKeyboardButton('психологические проблемы😐', callback_data='norm')
    item5 = types.InlineKeyboardButton('консультации🤝', callback_data='kons')
    item6 = types.InlineKeyboardButton('гипнотерапия😵', callback_data='gip')
    item7 = types.InlineKeyboardButton('обучение🖊🔎', callback_data='obuch')
    
    
 
    
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #item1 = types.KeyboardButton("главная")
    #item2 = types.InlineKeyboardButton( text = "whatsapp", url = 'https://wa.me/79150496843')
    #markup.add(item1, item2)
  
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать людям😁".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
                        
            if call.data == 'bad':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='qwerty')

                markup.add(item5, item6) 

                bot.send_message(call.message.chat.id, 'Пара слов о психосоматике💬 \n Например,если в общих чертах, то это узкое направление психологии, связанное с изучением проблем тела. \n В рамках психосоматики исследовались и исследуются связи между характеристиками личности (конституциональные особенности, черты характера и личности, стили поведения, типы эмоциональных конфликтов) и тем или иным соматическим заболеванием.\nВ альтернативной медицине популярно мнение, что все болезни человека возникают по причине психологических несоответствий и расстройств, возникающих в душе, в подсознании, в мыслях человека. \n \n«Все болезни от нервов» — это миф?\n \nЭто даже не миф, это просто старая студенческая шутка. Полная цитата звучит так: «Все болезни — от нервов, и только пять — от любви» (имеется в виду пять классических венерических болезней). Впрочем, хронический стресс — действительно доказанный фактор риска развития как минимум сердечно-сосудистых заболеваний.',   reply_markup=markup)
            if call.data == 'norm':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='qwerty')

                markup.add(item5, item6) 


                bot.send_message(call.message.chat.id, 'Психологические проблемы\nТот самый момент, когда вам нужно срочно избавиться от того, что вам очень мешает. Например, от неуверенности в себе, постоянного упадка сил, трудности в общении, панической атаки или же депрессивного состояния. Выбор делать вам: носить их с собой или избавиться от них.',reply_markup=markup)
            if call.data == 'hypnosis': 
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='qwerty')

                markup.add(item5, item6) 

                bot.send_message(call.message.chat.id,"О гипнозе\nГипноз покрыт мифами и тайнами. Мы его с ними и оставим. Пусть он остается под мантией таинственности. Самое важное — гипнотическое состояние присуще человеку по умолчанию. Это нормально совершенно. В этом состоянии возможно дойти до глубин подсознания и избавить от любой психологической проблемы ",reply_markup=markup)

            if call.data == 'kons':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='qwerty')

                markup.add(item5, item6) 
                bot.send_message(call.message.chat.id, 'Психологическое консультирование\nТот самый случай, когда  вам необходимо разобраться в себе. Со своими мыслями, переживаниями… Навести полный порядок в голове и заставить тараканов маршировать ровным строем. Вам будет легко и хорошо, и неразбериха из вашей жизни исчезнет. Записывайтесь!', reply_markup=markup)
            

            if call.data == 'gip':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='qwerty')

                markup.add(item5, item6) 
                bot.send_message(call.message.chat.id, 'Избавиться от проблем хотите?\n Вы хотите чувствовать себя нормальным человеком без загонов - гипнотерапия это тот самый инструмент, который позволит вашей цели достичь и причем довольно быстро.\n  \n В гипнотерапии нет "может быть", вероятностей и т.д., работа ведется только с вашим эмоциональным состоянием. И ведется она успешно всегда. Потому что это только ваше, и только с этим работа.\n Без сторонних отвлечений. \n-Армия инструментов\n-длительность сеанса 4 часа \n-предварительная беседа \n-замечательная польза гипноза как такового - все это приведет к тому, что вам станет легче и вы освободитесь от психологических проблем и начнете чувствовать себя нормально. Нормально всегда везде и во всем.\n \nЧто может быть важнее? Ничего не может быть важнее собственного самочувствия.', reply_markup=markup)
            if call.data == 'obuch':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='qwerty')
                item7 = types.InlineKeyboardButton(text = "курс СЕРЫЙ КАРДИНАЛ", callback_data='graykardinal')
                itemA = types.InlineKeyboardButton(text = 'курс БАБА ЯГА', callback_data='babayaga')
                markup.add(item5, item6, item7, itemA)

                bot.send_message(call.message.chat.id, 'про обучение🔬🔎', reply_markup=markup)
            elif call.data == 'qwerty':
                

                            
                sti = open('/home/georgy/anim.tgs', 'rb')
                bot.send_sticker(call.message.chat.id, sti)

                
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item2 = types.InlineKeyboardButton("о гипнозе💬", callback_data='hypnosis')
                item3 = types.InlineKeyboardButton("психисоматика🤔", callback_data='bad')
                item4 = types.InlineKeyboardButton('психологические проблемы😐', callback_data='norm')
                item5 = types.InlineKeyboardButton('консультации🤝', callback_data='kons')
                item6 = types.InlineKeyboardButton('гипнотерапия😵', callback_data='gip')
                item7 = types.InlineKeyboardButton('обучение🖊🔎', callback_data='obuch')
            
            
                markup.add(item1, item2, item3, item4, item5, item6, item7)
                bot.send_message(call.message.chat.id, "вы вернулись в гланвое меню", reply_markup=markup)
            
            elif call.data =='graykardinal':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='obuch')

                markup.add(item5, item6) 
                bot.send_message(call.message.chat.id, 'текст по курсу', reply_markup=markup)
            elif call.data == 'babayaga':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item5 = types.InlineKeyboardButton( text = "whatsapp🟩", url = 'https://wa.me/79150496843')
                item6 = types.InlineKeyboardButton(text = "назад⬅️", callback_data='obuch')

                markup.add(item5, item6) 
                bot.send_message(call.message.chat.id, 'текст по 2 курсу', reply_markup=markup)
          
    except Exception as e:
        print(repr(e))


    
bot.polling(none_stop=True)