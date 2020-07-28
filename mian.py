import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os

token = os.environ.get('BOT_TOKEN')

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
