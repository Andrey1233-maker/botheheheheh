import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os

token = "aa1f21dea247df805c0b3136cd220918dfbc24891a09467de0529b5e62cbc4d2b14353e30144361cd261e"

vk = vk_api.VkApi(token = token)

api = vk.get_api()

longpoll = VkLongPoll(vk)

def send(text, id):
	vk.method('messages.send',{'user_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen :
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:

			msg = event.text.lower()
			id = event.user_id

			if msg == "привет":
				send("LOL", id)
				
			else:
				send("WHAT?", id)
