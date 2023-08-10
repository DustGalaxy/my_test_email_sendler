# -*- coding: utf-8 -*-
import menu as mn, bombmessage as bm, json


def main():
    with open("config.json") as file:
        data = json.loads(file.read())

    bomb = bm.BombMessage(data['filename'],
                        data['from'],
                        data['password'],
                        data['to'],
                        data['subject'])

    email_menu = mn.Menu("> Email menu <",
                {
                "Email list": lambda: print('\n'.join([f"{x}" for x in bomb.addresses])),
                "Add email address": lambda: bomb.add_address(),
                "Del email address": lambda: bomb.del_address(),
                })

    main_menu = mn.Menu("> Main menu <",
                {

                "Start bombing": lambda: bomb.send_bomb(),
                "Bomb message": lambda: print(bomb.content.as_string()),
                "Edit subject": lambda: bomb.edit_subject(),
                "Login email": lambda: print(bomb.sendler),
                "Email menu": lambda: email_menu.start(),
                })

    main_menu.start()


if __name__ == "__main__":
    main()
