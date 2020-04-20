from python_omegle import InterestsChat
from python_omegle import ChatEvent
from python_omegle import RandomChat
import time

mensajes_recibidos=[]
n_chat = 0


def chat_loop(chat):
    global mensajes_recibidos, n_chat
    while True:
        # Start a new chat every time the old one ends
        print("- Starting chat -")
        chat.interes
        chat.start()
        while True:
            event, argument = chat.get_event()
            if event == ChatEvent.CHAT_WAITING:
                print("- Waiting for a partner -")
            elif event == ChatEvent.CHAT_READY:
                print("- Connected to a partner -")
                chat.start_typing()
                time.sleep(2)
                chat.send("Hola! 24 chico!")
                chat.stop_typing()
                chat.start_typing()
                time.sleep(1)
                chat.send("y tú?")
                chat.stop_typing()
                break
        # Connected to a partner
        while True:
            event, argument = chat.get_event()
            if event == ChatEvent.GOT_SERVER_NOTICE:
                notice = argument
                print("- Server notice: {} -".format(notice))
            elif event == ChatEvent.GOT_MESSAGE:
                message = argument
                mensajes_recibidos.append(message)
                print("la lista de mensajes es; ", mensajes_recibidos)
                print("Partner: {}".format(message))
            elif event == ChatEvent.CHAT_ENDED:
                print("- Chat ended -")
                n_chat +=1
                with open('{}.txt'.format(str(n_chat)), 'w') as f:
                    for msg in mensajes_recibidos:
                        f.write("%s\n" % msg)
                break

if __name__ == "__main__":
    chat = InterestsChat(["pruebita"], language="es")
    chat_loop(chat=chat)