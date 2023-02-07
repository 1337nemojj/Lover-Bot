#pip install pyTelegramBotAPI
import telebot
import json
from telebot import types
import random
from datetime import datetime
import time

with open('config.json', 'r') as fcc_file:
     cfg = json.load(fcc_file)

tok = cfg[0]
print(tok.get('apikey'))
TOKEN = tok.get('apikey')
bot = telebot.TeleBot(TOKEN, skip_pending=True, num_threads= 4)
#list of stickers ID
s_dir =\
    {1: "CAACAgIAAxkBAAEGcoljdS_imWaz72H-jp74TiZwTqfTeQACQQcAAlwCZQM3_GOaGamGFSsE",
     2: "CAACAgIAAxkBAAEGcmxjdS8GPGA4oWrenK7N160YI_fxZgACwAwAAvM0QEuBFItlPbqOtisE",
     3: 'CAACAgIAAxkBAAEGcl5jdS7T771oLt6JZAz7mfIHh3FxDgACEwoAAuohYUs6h3OH456CgysE',
     4: "CAACAgIAAxkBAAEGclZjdS6d7xnEaymFGh9xVnSIl6sbawACqhYAApybUEgXaAudwwX_WisE",
     5: 'CAACAgIAAxkBAAEGcmZjdS7mQo26DqS3IBTOQXHCkhxE3QACKQ0AAqHqEEi4h3H9kmf5sisE',
     6: 'CAACAgIAAxkBAAEGcmRjdS7hQMzJX07xcDZWEWZwAhsaCwACWw0AAiEYYEoKyDN0qoo5dCsE',
     7: 'CAACAgIAAxkBAAEGcm5jdS8IYPnFNP24Eyzl-07xX44qowACDQ4AAm8IQUsLdgZpiWzZ2ysE',
     8: 'CAACAgIAAxkBAAEGclxjdS7R9EWRji7kz2RGysn9XqS7xQACcwwAAg0UYEvlp6c9lQYfGisE',
     9: 'CAACAgIAAxkBAAEGclBjdS6PkwWFMk2QNqEAAUEtKO5lNFEAAncaAAJjjklISd0Cezg37worBA',
     10: 'CAACAgIAAxkBAAEGck5jdS6LkTTa0qGmhEoJAAFMAYuKJnYAAsoVAAJlVFFIi9qogrgSagQrBA',
     11: 'CAACAgUAAxkBAAEGckBjdS5DJUgB4er8tlEUpL3jr4JoywACPQQAAuLL0Vc8fzVOSO5JVCsE',
     12: 'CAACAgQAAxkBAAEGcjhjdS4PQ8dUbXVUkEs_JlCKQps58gACpwoAAoKyAAFSIeArZ4BQN6grBA',
     13: 'CAACAgQAAxkBAAEGciJjdS3WnjVGByGIuq53j-vLrhdQNQACBA0AAv254FH_mdx0RsOKcysE',
     14: 'CAACAgQAAxkBAAEGch5jdS3M9AtrKTr-p69C3N0EoAGj8gAC5w0AAgtFyVH7DS_ct-HGQysE',
     15: 'CAACAgIAAxkBAAEGcgpjdS08zryDiJ-jlQRM6VlWVej0LgACHwADobYRCL2v7UTV4wIUKwQ',
     16: 'CAACAgQAAxkBAAEGcgZjdS0jnhRlJHGHxFUTIdVDd6-M8wACugwAAqsCQFDOypnUFxVHXisE',
     17: 'CAACAgIAAxkBAAEGcmpjdS7qWJJH_Vo8p_iVMEytRUvb0QACrBUAAl9M0UobCDPwT3UoJysE',
     18: 'CAACAgIAAxkBAAEGcnBjdS81T6A5d9xVWzyktKHU2_cerwACBAAD5HgnCOkqWUDQlOXGKwQ',
     19: "CAACAgIAAxkBAAEGcphjdTI7VFQ9tvW4hYDTsW54pEz29wACgxkAAiY7mEhfKtXAStm9aysE",
     20: "CAACAgIAAxkBAAEGcpxjdTJ-SmnEIYiL21z03pk61ZhTxAAC2BkAAoveSEjErNoxCEU_YysE",
     21: 'CAACAgIAAxkBAAEGcqBjdTLpoCqItfNWdyggnSlja70D7QACthAAAi13eEjXDa4U1u_aAysE',
     22: 'CAACAgIAAxkBAAEGcqxjdTNjDomdHcmyM0rU9zAZplWGVQACQw8AArnNQUu2-JWFnFodBysE',
     23: 'CAACAgIAAxkBAAEGcrBjdTOrTrEmpL71t0Cp5U8AAdwMp4gAAvABAAKZmEYRv74VXCae-eArBA',
     24: 'CAACAgIAAxkBAAEGcrJjdTPAEykWE-uzS5u1S_LB8tl7rwACEQAD5HgnCEcK_tYUQpzuKwQ',
     25: 'CAACAgIAAxkBAAEGcrBjdTOrTrEmpL71t0Cp5U8AAdwMp4gAAvABAAKZmEYRv74VXCae-eArBA',
     26: 'CAACAgIAAxkBAAEGcotjdTAlCGampdxsmjlRSZsfWS44EgACHRQAApP0yUsAAZQ58XT5J5UrBA',
     27: 'CAACAgIAAxkBAAEGcodjdS_aGORTIJZPC7pv27bD-mO5YwACBwMAAlwCZQOmWFrzZSZxJCsE',
     28: 'CAACAgIAAxkBAAEGclRjdS6ZoWOWqI5Wy-m4_TJ2FP6c5gACGxQAAmb1UEgrdI7Fm5RV5SsE',
     29: 'CAACAgIAAxkBAAEGckhjdS5zkDj8j7olY3k0Gh3_LzOkVwACKwwAAjCVYUvPuA_NUBg0qisE',
     30: 'CAACAgQAAxkBAAEGcjpjdS4ZlanfETCCa9Y3mmrAK8yjpgACDwwAAvCmkFFn4SnYD2VIyCsE',
     31: 'CAACAgIAAxkBAAEGcihjdS3o40Hv5TFrFXUtB8ou5V2LcAACKCAAAiWmCUvhagpOe-vhVSsE',
     32: 'CAACAgQAAxkBAAEGciBjdS3Rg5DJM3wVo31aLJa9zvqjywACjgsAAvsm6FJ-_p0kiwRi2isE',
     33: 'CAACAgQAAxkBAAEGcgxjdS1DA8QLPD_rxCa-lVre405AVgACNQsAApFHCVJwvJ0N0FU-xCsE',
     34: 'CAACAgIAAxkBAAEGcg5jdS1kIjnEtK89FDkNfVc67irQWQACgRsAAqwZWEnWUM4sWHebAisE',
     35: 'CAACAgQAAxkBAAEGchJjdS2flXp8_JK-A6vYVfP-TaUp7gAC-woAAnI1QFPd1klx8DwwpCsE',
     36: 'CAACAgQAAxkBAAEGcjRjdS4Hod4P0sCae-oIcX6Ixk-SlwACkA0AAjDf-FEFueV-addoEysE',
     37: 'CAACAgQAAxkBAAEGcjhjdS4PQ8dUbXVUkEs_JlCKQps58gACpwoAAoKyAAFSIeArZ4BQN6grBA',
     38: 'CAACAgQAAxkBAAEGch5jdS3M9AtrKTr-p69C3N0EoAGj8gAC5w0AAgtFyVH7DS_ct-HGQysE',
     39: 'CAACAgQAAxkBAAEGcjJjdS4EkoBDGWNChg-ScwJPMVd4lQACWAwAApqDmFHWRFVu7IPxSysE',
     40: 'CAACAgQAAxkBAAEGciRjdS3YmPZCkqWaeuj86U_4GT9fBQACiwwAAvVFWVIYrCHDIpei-ysE',
     41: 'CAACAgEAAxkBAAEGdfZjd2AvrOs-IkIhI0mLxe22Xq8sKgACVAEAAlXgShdzEuwOxaOseSsE',
     42: 'CAACAgIAAxkBAAEGdfxjd2Cpa2LJrW-FuAABDEEvK8fkQsMAAqITAALs20FJcbX0Vh6bRF0rBA',
     43:'CAACAgIAAxkBAAEGdf5jd2C8hhe240-WGaaDOpLy1XpNoQACcwwAAg0UYEvlp6c9lQYfGisE',
     44:'CAACAgIAAxkBAAEGdgJjd2EOg20TQhD_8-trASIIKoBqJQACCxMAAn48UUgqTH8r8cBwdisE',
     45:'CAACAgIAAxkBAAEGdgZjd2Eng6z9AAHl365qLoFRxq00NoIAAgkbAAKX7UlIb18e2GSN7lcrBA',
     46:'CAACAgIAAxkBAAEGdghjd2E1OqgyMO4vl4Nxh0x70mldQgACERsAAuKtSEg0iBrMZ_JOoisE',
     47:'CAACAgIAAxkBAAEGdgpjd2FwsZWpqXT0SehESB2EEL9mcQACgQMAAm2wQgOxqAABZxcolQABKwQ',
     48:'CAACAgIAAxkBAAEGdhpjd2U4m1qY36G1dPZJYY4DZeCIJgACORIAAvtpEUrEH03rPXZmWysE',
     49:'CAACAgIAAxkBAAEGdhxjd2Ve5kFDcwhegkTl6iE-wFrPrgACsg4AAgtmoUruFymh7zTYNSsE',
     50:'CAACAgEAAxkBAAEGdh5jd2V6q1taeUJsmKEQgI12hV4C7wACpgEAAljvEDI4GsbfAR_SQSsE',
     51:'CAACAgIAAxkBAAEGcmpjdS7qWJJH_Vo8p_iVMEytRUvb0QACrBUAAl9M0UobCDPwT3UoJysE',
     52:'CAACAgQAAxkBAAEGdiBjd2WtTp2tCfaMtuc7BEX5exFw1QACng4AApnGCFBldjtD9uslZisE',
     53:'CAACAgQAAxkBAAEGdiJjd2X5T0L9hbor_dQVU6S2JxepIwACvw0AAsNGQVDV5HfNIko4eysE',
     54:'CAACAgQAAxkBAAEGdiZjd2YSLqtRf-ndkkCdykzsizr5oAACGhAAAmsQGVGvskVlhkC-fCsE',
     55:'CAACAgIAAxkBAAEGdihjd2YpkRhVDDt3SuNKrIb0G3wwFAACjxoAAs4hUUkCWbjzwMXmCCsE',
     
     }
#list of messages
dic = \
    {1: "Ты обворожительна!",
     2: "Ты будто сошла со страниц красивой сказки!",
     3: 'Ты – мой идеал!',
     4: "Ты красива, как богиня!",
     5: 'Ты – произведение искусства!',
     6: 'Ты легка, как весенний утренний ветерок.',
     7: 'С тобой хорошо и легко, будто я сам наедине с собой.',
     8: 'Твои глаза – два бездонных океана, в которых я готов утонуть прямо в эту минуту!',
     9: 'Ты умна и красива, разве так может быть это одновременно?',
     10: 'Ты так ухожена и привлекательна!',
     11: 'В тебе столько нежности, это меня привлекает и делает тебя невероятно женственной!',
     12: 'Ты – клад, который мне повезло найти!',
     13: 'Когда ты рядом, я забываю о всех своих проблемах и причина тому эта невероятная легкость!',
     14: 'Ты настоящая муза, которая дает силы и вдохновение для шедевров!',
     15: 'Ни в коем случае ничего не меняй в себе, ты просто божественна!',
     16: 'О такой красавице, как ты, я даже и не мечтал!',
     17: 'Я настоящий везунчик, ведь мне повезло встретить именно тебя!',
     18: 'У тебя самая привлекательная и милая улыбка на свете!',
     19: "Ты так меня понимаешь, будто читаешь все мои мысли и это так сводит меня с ума!",
     20: "Твои черты списаны с самых лучших картин художников!",
     21: 'Ты свежа и красива, как розовый бутон!',
     22: 'Ни один цветок в мире не сравниться с твоей красотой.',
     23: 'Ты – песня!',
     24: 'Когда ты смотришь на меня, я забываю обо всем на свете!',
     25: 'Не могу отвести глаз от твоей красоты!',
     26: 'Ты такая уточенная, такая изысканная и красивая, я не могу тобой не восхищаться!',
     27: 'Быть такой красивой – это преступление!',
     28: 'Боюсь, что тебя могут просто украсть из-за твоей красоты!',
     29: 'Не могу подобрать слов, олицетворяющих твою красоту, ведь в словаре их просто не хватает!',
     30: 'От твоей красоты темнеют глаза!',
     31: 'С годами твоя красота не блекнет, а лишь обретает новые краски!',
     32: 'Твоя красота заставляет чувствовать меня на вершине мира!',
     33: 'Твоя красота заставляет чувствовать меня пьяным.',
     34: 'Твои глаза – настоящий магнит и я не могу не смотреть в них!',
     35: 'Не переставай улыбаться, твоя улыбка обворожительна!',
     36: 'Ты настоящее сокровище!',
     37: 'Ты даже без какой-либо косметики выглядишь сногсшибательно!',
     38: 'Ты не воровка? Ведь совершенно бесстыдно ты украла все мои мысли и сердце!',
     39: 'Когда я смотрю на тебя, я просто теряю реальность!',
     40: 'У тебя космическая, невероятная и просто сказочная красота!',

     41: 'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nТы так красиво улыбнулась, что я забыл, куда шел. Предлагаю пойти куда-нибудь вместе!',
     42: 'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nТакой красивой девушке обязательно нужен телохранитель! Я с 30 метров в банку попадаю. Возьмете меня на работу?',
     43:'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nТвоя красота обезоруживает!',
     44:'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nИнтересно, какого дракона надо убить, чтобы добиться сердца такой принцессы, как ты?',
     45:'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nЕсли быть красивой считалось бы преступлением, тогда тебя объявили бы виновной!',
     46:'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nПо шкале от 1 до 10 ты выглядишь на 20!',
     47:'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nТвои глаза! Хочу в них утонуть… Когда ты смотришь на меня, я забываю, что умею плавать!',
     48:'ТЕБЕ ВЫПАЛ СУПЕР ПОДКАТ💖\nХочу признаться, лишь тебе: ты самая-самая лучшая на этой Земле!',
     
     49:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nВстреча с тобой, Булочка, это необыкновенный подарок судьбы! Ты мой ангел и сокровище. Только с тобой я чувствую себя самым счастливым, ты вдохновляешь меня!',
     50:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nЮночка, мне кажется, я заслужил премию и теперь точно разбогатею! Столько лет все мучаются вопросом, в чем смысл жизни, и никто до сих пор не нашел ответа. А я все знаю: для меня и ответ, и смысл жизни — это ты, моя Булочка!',
     51:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nЯ бы стал котом, чтобы провести с тобой девять жизней.(твой котя)',
     52:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nТы та, для кого бьется мое сердце!(100 ударов в минуту)',
     53:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nНет на Земле девушки прекраснее, чем ты, и нет мужчины счастливее, чем я, потому что возможность обнимать тебя – это и есть высшее счастье!',
     54:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nНа первый взгляд ты кажешься такой хрупкой, но своей улыбкой хоть кого отправишь в нокаут!',
     55:'ТЕБЕ ВЫПАЛ МЕГА-СУПЕР ПОДКАТ!!!💖💖💖\nЯ не могу поверить в то, что я встретил такую очаровательную девушку как ты!',
     
     }

def cur_time():
    t = datetime.now()
    return t.strftime("%m/%d/%Y, %H:%M:%S")

def show_wat_show(n):
    if 0 < n < 41:
        return "common"
    elif 40 < n < 49:
        return "rare"
    else:
        return "mega rare"

def ending(message,messageedit):
    frame_1 = """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍"""
    while frame_1.find("🤍") != -1:
        try:
            # Реплейсим одно белое на красное
            frame_1 = frame_1.replace("🤍", "❤️", 1)
            # Отображаем
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame_1)
            time.sleep(.1)

        except Exception as ex:
            time.sleep(0.4)

            # Отображаем
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame_1)
            time.sleep(.1)

    heart_rows_list = frame_1.split("\n")
    # Обрезаем строки, пока не останется один символ (8 итераций)
    for _ in range(8):
        # Удаляется нижняя строка
        del heart_rows_list[len(heart_rows_list) - 1]

        # Удаляется по одному последнему символу из строк
        for i in range(len(heart_rows_list)):
            heart_rows_list[i] = heart_rows_list[i][:-2]

        # Отображаем фрейм
        try:
            frame = "\n".join(heart_rows_list)

            bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
            time.sleep(.4)

        except Exception as ex:
            print(ex)

            bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
            time.sleep(.4)

def init_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Тык❤️')
    item2 = types.KeyboardButton('✨')
    item3 = types.KeyboardButton('❤️❤️❤️')
    item4 = types.KeyboardButton('I LOVE U 💖')
    markup.add(item4, item2, item3)
    markup.add(item1)
    return markup

def get_img(filename):
    img = open(f"{filename}.jpg", 'rb')
    return img

@bot.message_handler(commands=['start']) 
def start(message):
    print(f"[{message.from_user.first_name}:{message.from_user.id}] - {cur_time()} - NEW USER")
    bot.send_message(message.chat.id,
                     'И снова Привет, {0.first_name}! Я восстал из мертвых(Ботик) и опять буду работать не обещаю, что бесперебойно. НО! я буду стараться ❤️\n функционал я весь забыл потомму что мой программист не сохранял копии проекта, но обещает все восстановить)))'.format(
                         message.from_user), reply_markup=init_buttons()) # /start message

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Тык❤️':
            r = random.randint(1, 55) # select random message
            """if r == 56:
            print(f"[{message.from_user.first_name}:{message.from_user.id}] - {cur_time()} - Love story")
            bot.send_message(message.chat.id, "❤️ chance get this message 1.78% ❤️")
            time.sleep(0.8)
            for i in range(1,5):
                try:
                    bot.send_message(message.chat.id, f"{i} ❤️")
                    bot.send_photo(message.chat.id, get_img(f"love_story/{i}"))
                    time.sleep(1.8)
                except Exception as e:
                    print(e)
            bot.send_message(message.chat.id, "❤️ that's all kiss u :) ❤️")"""
        # else:    
            print(f"[{message.from_user.first_name}:{message.from_user.id}] - {cur_time()} - {show_wat_show(r)}") # console output for tracking clicks [username:user_id] - time - event
            bot.send_message(message.chat.id, dic[int(r)]) # send meassage
            bot.send_sticker(message.chat.id, sticker = s_dir[int(r)]) #send sticker


        if message.text == '❤️❤️❤️':
            print(f"[{message.from_user.first_name}:{message.from_user.id}] - {cur_time()} - ❤️❤️❤️")
            messageedit = bot.send_message(message.chat.id, f"❤️❤️❤️")


            frame_1 = """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍"""

            frame_2 = frame_1.replace("❤️", "🧡")

            frame_3 = frame_1.replace("❤️", "💛")

            frame_4 = frame_1.replace("❤️", "💚")

            frame_5 = frame_1.replace("❤️", "💙")

            frame_6 = frame_1.replace("❤️", "💜")

            frame_7 = frame_1.replace("❤️", "🖤")

            frame_8 = frame_1.replace("❤️", "🤎")

            # hearts
            heart_assortment = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤎"]

            # random frames
            frame_9 = "".join(
                list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

            frame_10 = "".join(
                list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

            frame_11 = "".join(
                list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

            frame_12 = "".join(
                list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

            frame_13 = "".join(
                list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

            # add frames to list
            frames_to_print = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9, frame_10, frame_11, frame_12, frame_13, frame_1]

            # show all frames
            for frame in frames_to_print:

                try:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.4)

                except Exception as ex:
                    print(ex)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.4)

            # change background to red hearts
            while frame_1.find("🤍") != -1:

                try:
                    # replace on red
                    frame_1 = frame_1.replace("🤍", "❤️", 1)
                    # output
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame_1)
                    time.sleep(.1)

                except Exception as ex:
                    time.sleep(0.4)

                    # output
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame_1)
                    time.sleep(.1)

            # list of frames
            heart_rows_list = frame_1.split("\n")
            # 8 iteration
            for _ in range(8):
                # del down string
                del heart_rows_list[len(heart_rows_list) - 1]

                # del one symbol
                for i in range(len(heart_rows_list)):
                    heart_rows_list[i] = heart_rows_list[i][:-2]

                # output frame
                try:
                    frame = "\n".join(heart_rows_list)

                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.4)

                except Exception as ex:
                    print(ex)

                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.4)
            
        if message.text == '✨':
            print(f"[{message.from_user.first_name}:{message.from_user.id}] - {cur_time()} - ✨")
            # frames
            frame_1 = """✨💎💎✨💎💎✨
💎💎💎💎💎💎💎
💎💎💎💎💎💎💎
✨💎💎💎💎💎✨
✨✨💎💎💎✨✨
✨✨✨💎✨✨✨
"""

            frame_2 = frame_1.replace("💎", "🌺")
            frame_3 = frame_1.replace("💎", "😘").replace("✨", "☁️")
            frame_4 = frame_1.replace("💎", "🌸")
            frame_5 = frame_1.replace("💎", "🐸").replace("✨", "🌾")
            frame_6 = frame_1.replace("💎", "💥").replace("✨", "🔫")
            frame_7 = frame_1.replace("💎", "💟").replace("✨", "☁️")
            frame_8 = frame_1.replace("💎", "💖").replace("✨", "🍀")
            frame_9 = frame_1.replace("💎", "🐼").replace("✨", "🌴")

            # add frames to list
            frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]

            # show each frame
            messageedit = bot.send_message(message.chat.id, f"✨")
            for frame in frames:
                
                try:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.5)

                except Exception as ex:
                    time.sleep(.5)
                    print(ex)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.5)
            ending(message,messageedit)

        if message.text == 'I LOVE U 💖':
            messageedit = bot.send_message(message.chat.id, f"I LOVE U 💖")
            t = datetime.now()
            print(f"[{message.from_user.first_name}:{message.from_user.id}] - {cur_time()} - I LOVE U 💖")
            # animation frames
            first_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            i_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨✨✨✨❤️❤️✨✨✨✨✨
✨✨✨✨❤️❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃❤️❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃❤️❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃❤️❤️🌃🌃🌃🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            second_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            third_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨❤️❤️❤️❤️❤️✨✨✨
✨✨❤️❤️❤️❤️❤️❤️❤️✨✨
✨❤️❤️❤️✨✨✨❤️❤️❤️✨
✨❤️❤️✨✨✨🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️❤️🌃🌃🌃❤️❤️❤️🌃
🌃🌃❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃❤️❤️❤️❤️❤️🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            fourth_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️✨✨✨✨✨✨✨❤️✨
✨❤️✨✨✨✨✨✨✨❤️✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨✨❤️✨✨✨🌃🌃❤️🌃🌃
🌃🌃❤️❤️🌃🌃🌃❤️❤️🌃🌃
🌃🌃❤️❤️🌃🌃🌃❤️❤️🌃🌃
🌃🌃🌃❤️🌃🌃🌃❤️🌃🌃🌃
🌃🌃🌃🌃❤️❤️❤️🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            fifth_frame = """✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            sixth_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️✨✨✨✨✨✨✨❤️✨
✨✨❤️✨✨✨✨✨❤️✨✨
✨✨✨❤️✨✨✨❤️✨✨✨
✨✨✨✨❤️✨❤️🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            seventh_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨❤️❤️❤️❤️❤️✨✨✨
✨✨❤️❤️❤️❤️❤️❤️❤️✨✨
✨❤️❤️❤️✨✨✨❤️❤️❤️✨
✨❤️❤️✨✨✨🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️❤️🌃🌃🌃❤️❤️❤️🌃
🌃🌃❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃❤️❤️❤️❤️❤️🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            eighth_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨❤️❤️✨✨✨🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️❤️🌃🌃🌃❤️❤️❤️🌃
🌃🌃❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃❤️❤️❤️❤️❤️🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

            # add frames to list
            frames = [first_frame, i_frame, second_frame, third_frame, fourth_frame, fifth_frame, sixth_frame, seventh_frame, eighth_frame]

            # output frames per 0.7 sec
            for frame in frames:

                try:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.7)

                except Exception as ex:
                    time.sleep(0.7)
                    print(ex)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=frame)
                    time.sleep(.7)
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageedit.message_id, text=f"❤️")
            ending(message,messageedit)

bot.polling()

