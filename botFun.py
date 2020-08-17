
def sendall(msg, vk):
    p = open("IdList.txt", "r")
    allid = p.read()
    x = len(allid)
    id = ""

    for i in range(x):
        if allid[i] != '\n':
            id += allid[i]
        else:
            send(msg, id, False, vk)
            id = ""

def send(text, id, k, vk):

    if k:
        vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, "keyboard": keyboard})
    else:
        vk.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})
