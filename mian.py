import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import os

token = ""

vk = vk_api.VkApi(token=token)

api = vk.get_api()

longpoll = VkLongPoll(vk)


def send(text, id):
    vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == "привет":
                send("LOL", id)

             if msg == 'приве':
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('Хочу тян', color=VkKeyboardColor.POSITIVE)
                keyboard.add_button('Тян не нужны!', color=VkKeyboardColor.NEGATIVE)

            else:
                send("WHAT?", id)
