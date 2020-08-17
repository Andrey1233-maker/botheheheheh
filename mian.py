import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import file
import botFun

token = "380b581f07cd920b8f639962f3ddea7050a04447b8bb301a7929ff5295e4782d0f5572ed7ec2b91f8bcdf"

vk = vk_api.VkApi(token=token)

api = vk.get_api()

longpoll = VkLongPoll(vk)

info = "А никак"
    ##"для этого нужно скачать на телефон приложение meme generator free,сделайте 1 комикс со смешариками и отправьте администратору сообщества,либо его заму.\n Администратор сообщества: https://vk.com/mi_miha\nзам.администратор: https://vk.com/andrew19e\nДальше администраторы решат брать ли вас в наш коллектив или нет"


def send(text, id, k):

    if k:
        vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, "keyboard": keyboard})
    else:
        vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

def buttonLol(label, color):
    text = "LOL"
    return{
        "action":{
            "type": "text",
            "payload": "{\"button\": \"1\"}",
            "label": label
        },
        "color": color
    }

def sendImage(code, id):
    vk.method("messages.send", {"peer_id": id, "attachment": str(code), "random_id": 0})

keyboard = {
    "one_time": False,
    "buttons": [
        [buttonLol("Стать редактором", color="positive")],
        [buttonLol("Пообщаться", color="positive")],
        [buttonLol("+", color="positive"),
        buttonLol("-", color="negative")]
    ]

}

keyboard = json.dumps(keyboard, ensure_ascii= False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id
            b = False

            if msg == "привет":
                send("LOL", id, False)
                b = True

            if msg == "начать":
                send("Чего вы хотите", id, True)
                b = True

            if msg == "стать редактором":
                send(info, id, False)
                b = True

            if msg == "пообщаться":
                send("Не работет( , но когда-нибудь будет", id, False)
                sendImage("photo-197780046_457239019", id)
                b = True

            if msg == "+":
                file.add_in_list(str(id))
                send("Не работет())))) , но когда-нибудь будет", id, False)
                b = True

            if msg == "-":
                file.remove_in_list(str(id))
                send("Не работет()))) , но когда-нибудь будет", id, False)
                b = True

            if msg.find("!ras") == 0:
                botFun.sendall(msg, vk)
                send("Мб сработало", id, False)
                b = True

            if b != True:
                sendImage("photo-197780046_457239018", id)

