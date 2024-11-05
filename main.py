from LD_player_bot import Bot, change_account
from time import sleep
from sys import setrecursionlimit

setrecursionlimit(200)

harvest_values = [
    (175, 39),
    (150, 39),
    (175, 36),
    (175, 39),
    (200, 39),
    (175, 39)
]
sleep(0)
bots = []
for storage, harvest_value in harvest_values:
    bot = Bot(13, storage, harvest_value)
    bots.append(bot)


while True:
    for i in  range(1, 6):
        bot = bots[i - 1]
        try:
            change_account(i)
            bot.run()
        except ReferenceError:
            bot.remove_error()
            sleep(1)
        except LookupError:
            bot.close_continue()
        except EnvironmentError:

            change_account(i)
            bot.run()

        except RecursionError:
            bot.fix_crush()



