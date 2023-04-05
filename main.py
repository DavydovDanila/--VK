import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


from colorama import init
init()
from colorama import Fore



vk_session = vk_api.VkApi(token="Ваш токен") 
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


def message (id, text):
    vk_session.method("messages.send", {"user_id": id, "message": text , "random_id": 0})


for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            print(Fore.RED + str(id) + ":",Fore.GREEN + str(msg))
            print()
            input_message = msg
            print(Fore.GREEN + input_message)
            message(id, input_message)


