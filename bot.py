import telebot
from telebot import types
from flask import Flask, request

secret = 'topopazzosgravato42069'
url = 'https://ucagnuleu.pythonanywhere.com/' + secret
bot = telebot.TeleBot('1327035157:AAEF1Ya63Pcyt1rJUVX7WvgwyfE624CVT40', threaded=False)

joinedFile = open ("/home/ucagnuleu/mysite/joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

joinedFileAdmin = open ("/home/ucagnuleu/mysite/admin.txt", "r")
joinedUsersAdmin = set()
for line in joinedFileAdmin:
    joinedUsersAdmin.add(line.strip())
joinedFileAdmin.close()

bot.remove_webhook()
bot.set_webhook(url=url)
app = Flask(__name__)

@app.route('/'+secret, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(commands=['start'])
def welcome(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open ("joined.txt", "a")
        joinedFile.write (str (message.chat.id) + "\n")
        joinedUsers.add (message.chat.id)
    else:
        pass
    if str(message.chat.id) in joinedUsersAdmin:
        admin_markup = types.ReplyKeyboardMarkup (resize_keyboard=True)
        btn1 = types.KeyboardButton ("Manda un broadcast a tutti")
        btn2 = types.KeyboardButton ("Gruppo per la statistica")
        btn3 = types.KeyboardButton ("Aggiungi un nuovo admin")
        btn4 = types.KeyboardButton ("Rimuovi admin")
        admin_markup.add (btn1)
        admin_markup.add (btn2)
        admin_markup.add (btn3)
        admin_markup.add (btn4)
        admin_message = f"Benvenuto capo <b>👑{message.from_user.first_name} {message.from_user.last_name}👑</b>\n" \
                        f"Da qua puoi gestire il bot in tutta comoditá"
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBZKlfc1SodyTzrq5ieHEvUuxbLhxAlwAC2AEAAladvQqY1H8pZ85AORsE')
        bot.send_message (message.chat.id, admin_message, parse_mode='html', reply_markup=admin_markup)
        bot.send_message (-357078187,
                          f"L'admin <b>{message.from_user.first_name} {message.from_user.last_name}</b> username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha avviato il bot",
                          parse_mode='html')

    else:
        bot.send_sticker (message.chat.id, 'CAACAgMAAxkBAAEBVyNfYhdsYdPG5YvfpRk6x3jFmFecewAC7wYAAr-MkATyFiq0vkdgjRsE')
        markup = types.ReplyKeyboardMarkup (resize_keyboard=True)
        item1 = types.KeyboardButton ("PlayStation 4")
        item2 = types.KeyboardButton ("Xbox One")
        item3 = types.KeyboardButton ("PlayStation 3")
        item4 = types.KeyboardButton ("Xbox 360")
        item5 = types.KeyboardButton ("PC")
        markup.add (item1, item2)
        markup.add (item3, item4)
        markup.add (item5)
        bot.send_message (message.chat.id,
                          "👋Benvenuto, <b>{0.first_name}</b> su @gta5cheatbot !\nQua puoi vedere i 💬comandi per attivare i 💰trucchi di GTAV.\nScegli la tua piattaforma:".format (
                              message.from_user, bot.get_me ()),
                          parse_mode='html', reply_markup=markup)
        bot.send_message (-357078187,
                          f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha avviato il bot",
                          parse_mode='html')


@bot.message_handler(commands=['broadcast'])
def mess(message):
    if str(message.chat.id) in joinedUsersAdmin:
        for user in joinedUsers:
            try:
                bot.send_message (user, message.text[message.text.find (' '):], parse_mode='html')
            except:
                pass
    else:
        bot.send_message(message.chat.id, "Non ha il permesso di inviare un broadcast😕")

@bot.message_handler(commands=['addadmin'])
def addadmin(message):
    if str(message.chat.id) in joinedUsersAdmin:
        admin = message.text[message.text.find (' '):]
        admin1 = str(admin.replace(" ", ""))
        if len(admin1) == 10 or len(admin1) == 9:
            if admin1.isdigit():
                if int(admin1) > 0:
                    joinedFileAdmin = open ("admin.txt", "a")
                    joinedFileAdmin.write (str (admin1) + "\n")
                    joinedUsersAdmin.add (admin1)
                    bot.send_message (message.chat.id,
                                      f"L'utente <b>{admin1}</b> aggiunto alla lista degli admin con successo")
                    bot.send_message (-357078187,
                          f"L'admin <b>{message.from_user.first_name} {message.from_user.last_name}</b> username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha aggiunto {admin1} agli admin",
                          parse_mode='html')
                else:
                    bot.send_message(message.chat.id, "Un gruppo non puó diventare un admin!")
            else:
                bot.send_message (message.chat.id, "L'id deve essere composto solo da cifre!")
        else:
            bot.send_message(message.chat.id, "L'id é composta da 9 o 10 cifre!")
    else:
        bot.send_message(message.chat.id, "Non ha il permesso di aggiungere un admin")

@bot.message_handler(commands=['help'])
def helt(message):
    help_message = f"ℹ️Per scoprire i codici di <b>GTA V</b>:\n" \
                   f"🔘Clicca la tua piattaforma sulla tastiera o digita:\n" \
                   f"🔘<code>PlayStation 4</code>/<code>PlayStation 3</code>/<code>Xbox One</code>/<code>Xbox 360</code>/<code>PC</code>\n" \
                   f"🔘Scegli la categoria che ti interessa"
    bot.send_message(message.chat.id, help_message, parse_mode='html')
    bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha cliccato /help",
                                  parse_mode='html')

@bot.message_handler(commands=['info'])
def info(message):
    info_message = f"ℹ️<b>Questo bot è stato sviluppato da:</b>\n" \
                   f"🔘@phausto\n" \
                   f"🔘Per ogni domanda/proposta/idea rivolgersi esclusivamente a lui.\n" \
                   f"🔘Per scoprire come usare i trucchi digitare /help"
    bot.send_message(message.chat.id, info_message, parse_mode='html')
    bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha cliccato /info",
                                  parse_mode='html')

@bot.message_handler(commands=['deleteadmin'])
def deleteadmin(message):
    if str(message.chat.id) in joinedUsersAdmin:
        admin = message.text[message.text.find (' '):]
        admin1 = str(admin.replace(" ", ""))
        if len(admin1) == 10 or len(admin1) == 9:
            if admin1.isdigit():
                if int(admin1) > 0:
                    joinedUsersAdmin.discard(admin1)
                    bot.send_message (message.chat.id,
                                      f"L'utente <b>{admin1}</b> é stato rimosso dalla lista degli admin con successo", parse_mode='html')
                else:
                    bot.send_message(message.chat.id, "Un gruppo non puó essere tolto!")
            else:
                bot.send_message (message.chat.id, "L'id deve essere composto solo da cifre!")
        else:
            bot.send_message(message.chat.id, "L'id é composta da 9 o 10 cifre!")
    else:
        bot.send_message(message.chat.id, "Non ha il permesso di rimuovere un admin")
        bot.send_message (-357078187,
                          f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha cercato di rimuovere un admin",
                          parse_mode='html')

@bot.message_handler(content_types=['text'])
def cheatsps4(message):
    if message.chat.type == 'private' and message.text == 'Rimuovi admin':
        if str (message.chat.id) == '396289008':
            message_text = f"<b>Per rimuovere un admin usa il comando</b>\n" \
                           f"/deleteadmin + il suo id (prendi da @get_id_bot)"
            bot.send_message (message.chat.id, message_text, parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Non hai il permesso per fare questa azione☹️")
            bot.send_message(-357078187, f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha cercato di rimuovere un admin",
                          parse_mode='html')

    if message.chat.type == 'private' and message.text == 'Manda un broadcast a tutti':
        if str (message.chat.id) in joinedUsersAdmin:
            message_text = '<b>Digita il comando</b>:\n /broadcast + Il messagio da mandare\n' \
                           'Ex:\n /broadcast Abbiamo una nuova funzione.\n' \
                           'Il messaggio che tutti riceveranno sará:\n' \
                           'Abbiamo una nuova funzione. \n' \
                           'Nel messaggio puoi usare l\'html ma non i link'
            bot.send_message (message.chat.id, message_text, parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Non hai il permesso per fare questa azione☹️")

    if message.chat.type == 'private' and message.text == 'Aggiungi un nuovo admin':
        if str (message.chat.id) in joinedUsersAdmin:
            message_text = f"<b>Per aggiungere un admin usa il comando</b>\n" \
                           f"/addadmin + il suo id (prendi da @get_id_bot)"
            bot.send_message (message.chat.id, message_text, parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Non hai il permesso per fare questa azione☹️")

    if message.chat.type == 'private' and message.text == 'Gruppo per la statistica':
        if str (message.chat.id) in joinedUsersAdmin:
            message_text = "<b>Ecco il link del gruppo</b>\nhttps://t.me/joinchat/FUiUq9UJd4tFhGZP"

            bot.send_message (message.chat.id, message_text, parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Non hai il permesso per fare questa azione☹️")
    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup(row_width=2)
        itm1 = types.InlineKeyboardButton("🚙Veicoli", callback_data='carsps4')
        itm2 = types.InlineKeyboardButton("🧍Personaggio", callback_data='playerps4')
        itm3 = types.InlineKeyboardButton("🎮Gioco", callback_data='gameps4')
        itm4 = types.InlineKeyboardButton("⚔️Battaglia", callback_data='battleps4')
        itm5 = types.InlineKeyboardButton("Come funziona❓", callback_data='helpps')

        markup.add (itm1, itm2)
        markup.add (itm3, itm4)
        markup.add (itm5)
        if message.chat.type == 'private':
            if message.text == 'PlayStation 4':
                bot.send_message (message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha aperto il menú per ps4", parse_mode='html')
                bot.delete_message(message.chat.id, message.message_id)

    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup(row_width=2)
        itm1 = types.InlineKeyboardButton("🚙Veicoli", callback_data='carsps4')
        itm2 = types.InlineKeyboardButton("🧍Personaggio", callback_data='playerps4')
        itm3 = types.InlineKeyboardButton("🎮Gioco", callback_data='gameps4')
        itm4 = types.InlineKeyboardButton("⚔️Battaglia", callback_data='battleps4')
        itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helpps')

        markup.add (itm1, itm2)
        markup.add (itm3, itm4)
        markup.add (itm5)
        if message.chat.type == 'private':
            if message.text == 'PlayStation 3':
                bot.send_message (message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha aperto il menú per ps3",
                                  parse_mode='html')
                bot.delete_message (message.chat.id, message.message_id)

    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup (row_width=2)
        itm1 = types.InlineKeyboardButton ("🚙Veicoli", callback_data='carsxone')
        itm2 = types.InlineKeyboardButton ("🧍Personaggio", callback_data='playerxone')
        itm3 = types.InlineKeyboardButton ("🎮Gioco", callback_data='gamexone')
        itm4 = types.InlineKeyboardButton ("⚔️Battaglia", callback_data='battlexone')
        itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helpxone')

        markup.add (itm1, itm2)
        markup.add (itm3, itm4)
        markup.add (itm5)
        if message.chat.type == 'private':
            if message.text == 'Xbox One':
                bot.send_message (message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha aperto il menú per xboxone",
                                  parse_mode='html')
                bot.delete_message (message.chat.id, message.message_id)

    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup (row_width=2)
        itm1 = types.InlineKeyboardButton ("🚙Veicoli", callback_data='carsxone')
        itm2 = types.InlineKeyboardButton ("🧍Personaggio", callback_data='playerxone')
        itm3 = types.InlineKeyboardButton ("🎮Gioco", callback_data='gamexone')
        itm4 = types.InlineKeyboardButton ("⚔️Battaglia", callback_data='battlexone')
        itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helpxone')

        markup.add (itm1, itm2)
        markup.add (itm3, itm4)
        markup.add (itm5)
        if message.chat.type == 'private':
            if message.text == 'Xbox 360':
                bot.send_message (message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha aperto il menú per xbox360",
                                  parse_mode='html')
                bot.delete_message (message.chat.id, message.message_id)

    if message.chat.type == 'private':
        markup = types.InlineKeyboardMarkup (row_width=2)
        itm1 = types.InlineKeyboardButton ("🚙Veicoli", callback_data='carspc')
        itm2 = types.InlineKeyboardButton ("🧍Personaggio", callback_data='playerpc')
        itm3 = types.InlineKeyboardButton ("🎮Gioco", callback_data='gamepc')
        itm4 = types.InlineKeyboardButton ("⚔️Battaglia", callback_data='battlepc')
        itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helppc')

        markup.add (itm1, itm2)
        markup.add (itm3, itm4)
        markup.add (itm5)
        if message.chat.type == 'private':
            if message.text == 'PC':
                bot.send_message (message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.send_message (-357078187,
                                  f"nome = '{message.from_user.first_name}' cognome = '{message.from_user.last_name}', username = '@{message.from_user.username}', id='<code>{message.chat.id}</code>' ha aperto il menú per pc",
                                  parse_mode='html')
                bot.delete_message (message.chat.id, message.message_id)

@bot.callback_query_handler (func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'carsps4':
                markupcarsps4 = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton("🔙Indietro", callback_data='backps4')
                markupcarsps4.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>AUTO:</b>\n\n<b>🔶Sportcar Rapid GT:</b>\n  R2 L1 O → L1 R1 → ← O R2\n\n<b>🔶Sportcar Comet:</b>\n  R1 O R2 → L1 L2 X X ■ R1\n\n<b>🔶Stretch Limo:</b>\n  R2 → L2 ← ← R1 L1 O →\n\n<b>🔶Trashmaster:</b>\n  O R1 O R1 ← ← R1 L1 O →\n\n<b>🔶Golfcar Caddy:</b>\n  O L1 ← R1 L2 X R1 L1 O X\n\n<b>MOTO:</b>\n\n<b>🔶Moto Sanchez:</b>\n  O X L1 O O L1 O R1 R2 L2 L1 L1\n\n<b>🔶Moto PCJ600:</b>\n  R1 → ← → R2 ← → ■ → L2 L1 L1\n\n<b>🔶Bici BMX:</b>\n  ← ← → → ← → ■ O ▲ R1 R2\n\n<b>AEREOMOBILI:</b>\n\n<b>🔶Elicottero Buzzard:</b>\n  O O L1 O O O L1 L2 R1 ▲ O ▲\n\n<b>🔶Aereo da trick:</b>\n  O → L1 L2 ← R1 L1 L1 ← ← X ▲\n\n<b>🔶Aereo Duster:</b>\n  → ← R1 R1 R1 ← ▲ ▲ X O L1 L1", parse_mode='html', reply_markup=markupcarsps4)


            elif call.data == 'playerps4':
                markupcarsps4 = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backps4')
                markupcarsps4.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 text="<b>🔶Aumenta livello ricercato:</b>\n  R1 R1 O R2 ← → ← → ← →\n\n<b>🔶Diminuisci livello ricercato:</b>\n  R1 R1 O R2 → ← → ← → ←\n\n<b>🔶Salute e armatura:</b>\n  O L1 ▲ R2 X ■ O → ■ L1 L1 L1\n\n<b>🔶Invincibilità (5 min):</b>\n  → X → ← → R1 → ← X ▲\n\n<b>🔶Ricarica abilità speciale:</b>\n  X X ■ R1 L1 X → ← X\n\n<b>🔶Recupera vita + aggiusta auto:</b>\n  Start X O L1 ▲ R2 X ■ O → ■ L1 L1 L1 Start\n\n<b>🔶Ricevi i soldi (non funziona sempre):</b>\n  → → → ← ↑ ■ ↓ ↓  ● → → ↑", parse_mode='html', reply_markup=markupcarsps4)


            elif call.data == 'gameps4':
                markupcarsps4 = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backps4')
                markupcarsps4.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 text="<b>🔶Corsa veloce:</b>\n  ▲ ← → → L2 L1 ■\n\n<b>🔶Nuoto veloce:</b>\n  ← ← L1 → → R2 → L2 →\n\n<b>🔶Rallenta il tempo durante la mira:</b>\n  ■ L2 R1 ▲ ← ■ L2 → X\n\n<b>🔶Diminuisci la gravita per i veicoli:</b>\n  ← ← L1 R1 L1 → ← L1 ←\n\n<b>Super salto:</b>\n  ← ← ▲ ▲ → → ← → ■ R1 R2\n\n<b>🔶Cadi dal cielo:</b>\n  L1 L2 R1 R2 ← → ← → L1 L2 R1 R2 ← → ← →\n\n<b>🔶Rallenta il tempo:</b>\n  ▲ ← → → ■ R2 R1\n\n<b>🔶Cambia il tempo:</b>\n  R2 X L1 L1 L2 L2 L2 ■", parse_mode='html', reply_markup=markupcarsps4)

            elif call.data == 'battleps4':
                markupcarsps4 = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backps4')
                markupcarsps4.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 text="<b>🔶Ricevi tutte le armi:</b>\n  ▲ R2 ← L1 X → ▲ ↓ ■ L1 L1 L1\n\n<b>🔶Paracadute:</b>\n  ← → L1 L2 R1 R2 R2 ← ← → L1\n\n<b>🔶Pugni esplosivi:</b>\n  → ← X ▲ R1 O O O L2\n\n<b>🔶Proiettili esplosivi:</b>\n  → ■ X ← R1 R2 ← → → L1 L1 L1\n\n<b>🔶Proiettili infuocati:</b>\n  L1 R1 ■ R1 ← R2 R1 → ■ → L1 L1", parse_mode='html', reply_markup=markupcarsps4)


            elif call.data == 'carsxone':
                markupxone = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backxone')
                markupxone.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                 text="<b>AUTO:</b>\n\n<b>🔶Sportcar Rapid GT:</b>\n  RT LB B → LB RB → ← B RT\n\n<b>🔶Sportcar Comet:</b>\n  RB B RT → LB LT A A X RB\n\n<b>🔶Stretch Limo:</b>\n  RT → LT ← ← RB LB B →\n\n<b>🔶Trashmaster:</b>\n  B RB B RB ← ← RB LB B →\n\n<b>🔶Golfcar Caddy:</b>\n  B LB ← RB LT A RB LB B A\n\n<b>MOTO:</b>\n\n<b>🔶Moto Sanchez:</b>\n  B A LB B B LB B RB RT LT LB LB\n\n<b>🔶Moto PCJ600:</b>\n  RB → ← → RT ← → X → LT LB LB\n\n<b>🔶Bici BMX:</b>\n  ← ← → → ← → X B Y RB RT\n\n<b>AEREOMOBILI:</b>\n\n<b>🔶Elicottero Buzzard:</b>\n  B B LB B B B LB LT RB Y B Y\n\n<b>🔶Aereo da trick:</b>\n  B → LB LT ← RB LB LB ← ← A Y\n\n<b>🔶Aereo Duster:</b>\n  → ← RB RB RB ← Y Y A B LB LB", parse_mode='html', reply_markup=markupxone)



            elif call.data == 'playerxone':
                markupxone = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backxone')
                markupxone.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>🔶Aumenta livello ricercato:</b>\n  RB RB B RT ← → ← → ← →\n\n<b>🔶Diminuisci livello ricercato:</b>\n  RB RB B RT → ← → ← → ←\n\n<b>🔶Salute e armatura:</b>\n  B LB Y RT A X B → X LB LB LB\n\n<b>🔶Invincibilità (5 min):</b>\n  → A → ← → RB → ← A Y\n\n<b>🔶Ricarica abilità speciale:</b>\n  A A X RB LB A → ← A\n\n<b>🔶Recupera vita + aggiusta auto:</b>\n  Start A B LB Y RT A X B → X LB LB LB Start", parse_mode='html', reply_markup=markupxone)

            elif call.data == 'gamexone':
                markupxone = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backxone')
                markupxone.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>🔶Corsa veloce:</b>\n  Y ← → → LT LB X\n\n<b>🔶Nuoto veloce:</b>\n  ← ← LB → → RT ← LT →\n\n<b>🔶Rallenta il tempo durante la mira:</b>\n  X LT RB Y ← X LT → A\n\n<b>🔶Diminuisci la gravita per i veicoli:</b>\n  ← ← LB RB LB → ← LB ←\n\n<b>🔶Super salto:</b>\n  ← ← Y Y → → ← → X RB RT\n\n<b>🔶Cadi dal cielo:</b>\n  LB LT RB RT ← → ← → LB LT RB RT ← → ← →\n\n<b>🔶Rallenta il tempo:</b>\n  Y ← → → X RT RB\n\n<b>🔶Cambia il tempo:</b>\n  RT A LB LB LT LT LT X", parse_mode='html', reply_markup=markupxone)


            elif call.data == 'battlexone':
                markupxone = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backxone')
                markupxone.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>🔶Ricevi tutte le armi:</b>\n  Y RT ← LB A → Y ↓ X LB LB LB\n\n<b>🔶Paracadute:</b>\n  ← → LB LT RB RT RT ← ← → LB\n\n<b>🔶Pugni esplosivi:</b>\n  → ← A Y RB B B B LT\n\n<b>🔶Proiettili esplosivi:</b>\n  → X A ← RB RT ← → → LB LB LB\n\n<b>🔶Proiettili infuocati:</b>\n  LB RB X RB ← RT RB ← X → LB LB", parse_mode='html', reply_markup=markupxone)


            elif call.data == 'carspc':
                markuppc = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backpc')
                markuppc.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>AUTO:</b>\n\n<b>🔶Sportcar Rapid GT:</b>\n  1-999-727-4348 (RAPIDGT)\n\n<b>🔶Sportcar Comet:</b>\n  1-999-266-38 (COMET)\n\n<b>🔶Stretch Limo:</b>\n  1-999-846-39663 (VINEWOOD)\n\n<b>🔶Trashmaster:</b>\n  1-999-872-433 (TRASHED)\n\n<b>🔶Golfcar Caddy:</b>\n  1-999-4653-46-1 (HOLEIN1)\n\n<b>🔶Auto armata Duke O’Death:</b>\n  1-999-3328-4227 (DEATHCAR)\n\n<b>🔶Auto Go Go Monkey Blista:</b>\n  1-999-282-2537 (BUBBLES)\n\n<b>MOTO:</b>\n\n<b>🔶Moto Sanchez:</b>\n  1-999-633-7629 (OFFROAD)\n\n<b>🔶Moto PCJ600:</b>\n  1-999-762-538 (ROCKET)\n\n<b>🔶Bici BMX:</b>\n  1-999-226-348 (BANDIT)\n\n<b>AEREOMOBILI:</b>\n\n<b>🔶Elicottero Buzzard:</b>\n  1-999-289-9633 (BUZZOFF)\n\n<b>🔶Aereo da trick:</b>\n  1-999-2276-78676 (BARNSTORM)\n\n<b>🔶Aereo Duster:</b>\n  1-999-359-77729 (FLYSPRAY)\n\n<b>🔶Aereo Dodo:</b>\n  1-999-398-4628 (EXTINCT)\n\n<b>ALTRO:</b>\n\n<b>🔶Sottomarino Kraken Sub:</b>\n  1-999-282-2537 (BUBBLES)", parse_mode='html', reply_markup=markuppc)


            elif call.data == 'playerpc':
                markuppc = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backpc')
                markuppc.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>🔶Aumenta livello ricercato:</b>\n  1-999-3844-8483 (FUGITIVE)\n\n<b>🔶Diminuisci livello ricercato:</b>\n  1-999-5299-3787 (LAWYERUP)\n\n<b>🔶Salute e armatura:</b>\n  1-999-887-853 (TURTLE)\n\n<b>🔶Invincibilità (5 min):</b>\n  1-999-724-4654-5537 (PAINKILLER)\n\n<b>🔶Ricarica abilità speciale:</b>\n  1-999-769-3787 (POWERUP)\n\n<b>🔶Recupera vita + aggiusta auto:</b>\n  1-999-887-853 (TURTLE)",
                                  parse_mode='html', reply_markup=markuppc)

            elif call.data == 'gamepc':
                markuppc = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backpc')
                markuppc.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>🔶Corsa veloce:</b>\n  1-999-228-8463 (CATCHME)\n\n<b>🔶Nuoto veloce:</b>\n  1-999-468-44557 (GOTGILLS)\n\n<b>🔶Rallenta il tempo durante la mira:</b>\n  1-999-332-3393 (DEADEYE)\n\n<b>🔶Diminuisci la gravita per i veicoli:</b>\n  1-999-356-2837 (FLOATER)\n\n<b>🔶Super salto:</b>\n  1-999-467-86-48 (HOPTOIT)\n\n<b>🔶Cadi dal cielo:</b>\n  1-999-759-3255 (SKYFALL)\n\n<b>🔶Rallenta il tempo:</b>\n  1-999-756-966 (SLOWMO)\n\n<b>🔶Cambia il tempo:</b>\n  1-999-625-348-7246 (MAKEITRAIN)", parse_mode='html', reply_markup=markuppc)


            elif call.data == 'battlepc':
                markuppc = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backpc')
                markuppc.add (back)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="<b>🔶Ricevi tutte le armi:</b>\n  1-999-8665-87 (TOOLUP)\n\n<b>🔶Paracadute:</b>\n  1-999-759-3483 (SKYDIVE)\n\n<b>🔶Pugni esplosivi:</b>\n  1-999-4684-2637 (HOTHANDS)\n\n<b>🔶Proiettili esplosivi:</b>\n  1-999-444-439 (HIGHEX)\n\n<b>🔶Proiettili infuocati:</b>\n  1-999-462-363-4279 (INCENDIARY)", parse_mode='html', reply_markup=markuppc)


            elif call.data == 'backps4':
                markup = types.InlineKeyboardMarkup (row_width=2)
                itm1 = types.InlineKeyboardButton ("🚙Veicoli", callback_data='carsps4')
                itm2 = types.InlineKeyboardButton ("🧍Personaggio", callback_data='playerps4')
                itm3 = types.InlineKeyboardButton ("🎮Gioco", callback_data='gameps4')
                itm4 = types.InlineKeyboardButton ("⚔️Battaglia", callback_data='battleps4')
                itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helpps')

                markup.add (itm1, itm2)
                markup.add (itm3, itm4)
                markup.add (itm5)
                bot.send_message (call.message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.delete_message (chat_id=call.message.chat.id, message_id=call.message.message_id)

            elif call.data == 'backxone':
                markup = types.InlineKeyboardMarkup (row_width=2)
                itm1 = types.InlineKeyboardButton ("🚙Veicoli", callback_data='carsxone')
                itm2 = types.InlineKeyboardButton ("🧍Personaggio", callback_data='playerxone')
                itm3 = types.InlineKeyboardButton ("🎮Gioco", callback_data='gamexone')
                itm4 = types.InlineKeyboardButton ("⚔️Battaglia", callback_data='battlexone')
                itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helpxone')

                markup.add (itm1, itm2)
                markup.add (itm3, itm4)
                markup.add (itm5)
                bot.send_message (call.message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.delete_message (chat_id=call.message.chat.id, message_id=call.message.message_id)

            elif call.data == 'backpc':
                markup = types.InlineKeyboardMarkup (row_width=2)
                itm1 = types.InlineKeyboardButton ("🚙Veicoli", callback_data='carspc')
                itm2 = types.InlineKeyboardButton ("🧍Personaggio", callback_data='playerpc')
                itm3 = types.InlineKeyboardButton ("🎮Gioco", callback_data='gamepc')
                itm4 = types.InlineKeyboardButton ("⚔️Battaglia", callback_data='battlepc')
                itm5 = types.InlineKeyboardButton ("Come funziona❓", callback_data='helppc')

                markup.add (itm1, itm2)
                markup.add (itm3, itm4)
                markup.add (itm5)
                bot.send_message (call.message.chat.id, "Scegli la categoria☎️:", reply_markup=markup)
                bot.delete_message (chat_id=call.message.chat.id, message_id=call.message.message_id)

            elif call.data == 'helpps':
                markupinfo = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backps4')
                markupinfo.add (back)
                bot.send_message(call.message.chat.id, "<b>Attenzione! Inserendo un trucco disabiliti l'ottenimento dei trofei nel gioco!</b>\n Il nostro consiglio è di salvare il gioco prima di inserire i trucchi.\n<b>Come faccio ad attivare i trucchi?</b>\n Entra in una partita e clicca la combinazione di tasti sul controller.", parse_mode='html', reply_markup=markupinfo)
                bot.send_photo(call.message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Dualshock3_Layout.svg/1200px-Dualshock3_Layout.svg.png')
                bot.delete_message (chat_id=call.message.chat.id, message_id=call.message.message_id)

            elif call.data == 'helpxone':
                markupinfo = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backxone')
                markupinfo.add (back)
                bot.send_message(call.message.chat.id, "<b>Attenzione! Inserendo un trucco disabiliti l'ottenimento degli obiettivi nel gioco!</b>\n Il nostro consiglio è di salvare il gioco prima di inserire i trucchi.\n<b>Come faccio ad attivare i trucchi?</b>\n Entra in una partita e clicca la combinazione di tasti sul controller.", parse_mode='html', reply_markup=markupinfo)
                bot.send_photo(call.message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/360_controller.svg/432px-360_controller.svg.png')
                bot.delete_message (chat_id=call.message.chat.id, message_id=call.message.message_id)

            elif call.data == 'helppc':
                markupinfo = types.InlineKeyboardMarkup (row_width=1)
                back = types.InlineKeyboardButton ("🔙Indietro", callback_data='backpc')
                markupinfo.add (back)
                bot.send_message(call.message.chat.id, "<b>Attenzione! Inserendo un trucco disabiliti l'ottenimento dei trofei nel gioco!</b>\n Il nostro consiglio è di salvare il gioco prima di inserire i trucchi.\n<b>Come faccio ad attivare i trucchi?</b>\n Entra in una partita e digita sulla tastiera la parola che corrisponde al trucco. In alternativa chiama il numero di telefono col telefono virtuale nel gioco.", parse_mode='html', reply_markup=markupinfo)
                bot.delete_message (chat_id=call.message.chat.id, message_id=call.message.message_id)


    except Exception as e:
        print (repr (e))