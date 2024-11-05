from utils import Match
import pyautogui
from time import sleep
width = 1920
height = 1080

matcher = Match()


def slide_list():
    pyautogui.mouseDown(matcher.find_match('3'))
    pyautogui.moveRel(0, -600, duration=0.2)
    pyautogui.mouseUp()

def change_account(count):
    sleep(0.2)
    pyautogui.click(matcher.find_match('options'))
    sleep(0.3)
    pyautogui.click(350, 430)
    sleep(0.4)

    pyautogui.click(matcher.find_match('change'))
    sleep(0.3)

    if count > 3:
        slide_list()
    pyautogui.click(matcher.find_match(str(count)))
    #pyautogui.click(1250, 650 + (count-1)*75)

    sleep(1)


def go_through_field():
    for i in range(7):
        pyautogui.moveRel(700, -350, 0.15)
        pyautogui.moveRel(12, 12)
        pyautogui.moveRel(-700, 350, duration=0.15)
        pyautogui.moveRel(12, 12)


def adjustment(x, y):
    pyautogui.mouseDown()
    offset_x = x - 726
    offset_y = 660 - y
    pyautogui.moveRel(offset_x, offset_y, duration=0.2)
    pyautogui.mouseUp()
    return x + offset_x, offset_y + y


class Bot:
    def __init__(self, quantity, storage, harvest_value):
        self.quantity = quantity
        self.storage = storage
        self.harvest_value = harvest_value

        self.m = Match()

    def take_harvest(self):
        post_box_pos = self.m.find_match('post_box')
        harvest_pos = (post_box_pos[0] + 100, post_box_pos[1]-5)
        pyautogui.click(harvest_pos)

        sickle_pos = (self.m.find_match('sickle'))
        pyautogui.mouseDown(*sickle_pos)
        pyautogui.moveTo(post_box_pos[0] , post_box_pos[1] - 50)

        go_through_field()

        pyautogui.mouseUp()
        sleep(.7)

        post_box_pos = self.m.find_match('post_box')
        harvest_pos = (post_box_pos[0] + 100, post_box_pos[1])
        pyautogui.click(harvest_pos)
        wheat_pos = self.m.find_matches('wheat')
        pyautogui.mouseDown(sickle_pos[0] + 70, sickle_pos[1] - 50)
        post_box_pos = self.m.find_match('post_box')
        sleep(.9)
        if len(list(self.m.find_matches('continue'))):
            self.close_continue()
            pyautogui.click(harvest_pos)
            wheat_pos = self.m.find_matches('wheat')
            pyautogui.mouseDown(sickle_pos[0] + 70, sickle_pos[1] - 50)
            post_box_pos = self.m.find_match('post_box')

        pyautogui.moveTo(post_box_pos[0] + 120, post_box_pos[1], duration=0.15)

        pyautogui.moveTo(post_box_pos)

        go_through_field()


        self.shop_pos = self.m.find_match('apples')

        pyautogui.mouseUp()

    def shopping(self):


        pyautogui.click(self.shop_pos[0] - 90, self.shop_pos[1] - 25)
        if len(list(self.m.find_matches('continue'))):
            self.close_continue()
            pyautogui.mouseDown(1000,500)
            pyautogui.moveRel(300,0,duration=.15)
            pyautogui.mouseUp()
            self.shop_pos = self.m.find_match('apples')
            self.shopping()

        success = False
        count = 0
        for sold in self.m.find_matches('sold'):
            count += 1
            pyautogui.click(sold)

        if count > 4:
            sleep(1)

        for slot in self.m.find_matches('empty_slot'):

            pyautogui.click(slot)

            if not success:
                wheat_pos = list(self.m.find_matches('wheat_shop'))
            success = True


            if wheat_pos:
                pyautogui.click(550, 300)
            else:
                pyautogui.click(300, 330)
                pyautogui.click(550, 300)

            pyautogui.click(1250, 550)

            pyautogui.click(1200, 800)

            pyautogui.click(1340, 950)
            self.quantity -= 10
            if self.quantity <= 20:
                break

        if not success:
            pyautogui.click(self.m.find_match('occupied_slot'))
            sleep(0.1)

            if len(list(self.m.find_matches('magazine_time'))) == 0 and len(list(self.m.find_matches('published_magazine'))) == 0:
                pyautogui.click(self.m.find_match('ready_magazine'))
                sleep(0.2)
                pyautogui.click(self.m.find_match('make_published'))


            else:
                pyautogui.click(1570, 170)

        sleep(0.2)
        pyautogui.click(1570, 170)


    def run(self):
        self.start()
        if self.quantity + self.harvest_value < self.storage:
            self.take_harvest()
            self.quantity += self.harvest_value
        else:
            sleep(5)
            self.shop_pos = self.m.find_match('apples')
        self.shopping()

    def start(self):
        pyautogui.moveTo(1420,200)
        self.m.find_match('shtuka')

        pyautogui.keyDown('ctrl')
        pyautogui.scroll(-1000)
        sleep(0.3)
        pyautogui.keyUp('ctrl')
        sleep(.1)

        pyautogui.mouseDown(1000, 500)
        pyautogui.moveRel(200, -200, duration=0.3)
        if len(list(self.m.find_matches('close'))):
            raise EnvironmentError
        pyautogui.mouseUp()

        pyautogui.mouseDown(200, 500)
        pyautogui.moveRel(500,0)
        sleep(.2)

        pyautogui.moveRel(-200,0)
        sleep(.2)
        pyautogui.mouseUp()

    def remove_error(self):
        pyautogui.click(self.m.find_match('error'))


    def close_event(self):
        pyautogui.click(self.m.find_match('close'))
        sleep(1)
        pyautogui.click(self.m.find_match('close'))
        sleep(1)


    def close_continue(self):
        pyautogui.click(950, 950)

    def fix_crush(self):
        crush_report = self.m.find_match('crush_report')
        pyautogui.click(crush_report[0]-100, crush_report[1])
        sleep(5)

        pyautogui.click(self.m.find_match('logo'))
        sleep(15)
        pyautogui.click(1600,130)
        sleep(3)


