from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import urllib
from urllib import request
from bs4 import BeautifulSoup
import re
import math

__author__ = 'cyan'

# Neopets Dailies Automation. User can choose to execute individual dailies or run everything at once.


class Player:
    def __init__(self,user):
        self.username = user
        self.neopets = []
        self.money = 0
        self.inventory = 0

    def getPets(self):
        driver.get('http://www.neopets.com/userlookup.phtml?user={user}'.format(user=username_input))
        user_page_soup = str(BeautifulSoup(driver.page_source, "html.parser"))
        pet_regex = r"pet=(.+)\"\>"
        neopets_list = re.findall(pet_regex, user_page_soup)
        print(neopets_list)
        print(len(neopets_list))
        self.neopets = neopets_list


def jelly():  # gets free jelly. Sometimes jelly runs out, if jelly isn't there, program doesn't do anything
    driver.get("http://www.neopets.com/jelly/jelly.phtml")
    if driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/center[2]/form/input[2]'):
        getjelly = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/center[2]/form/input[2]')
        getjelly.click()
    else:
        WebDriverWait(driver,3)


def omelette():  # gets free omelette. See jelly (similar running out situation)
    driver.get('http://www.neopets.com/prehistoric/omelette.phtml')
    if driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/center[2]/form/input[2]'):
        getomelette = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/center[2]/form/input[2]')
        getomelette.click()
    else:
        WebDriverWait(driver, 3)


def springs():  # healing springs. Gets random fairy blessing
    driver.get('http://www.neopets.com/faerieland/springs.phtml')
    gotosprings = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/center[2]/form/input[2]')
    if driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/center[2]/form/input[2]'):
        gotosprings.click()
    else:
        WebDriverWait(driver,3)


def apples(): # apple bobbing
    driver.get('http://www.neopets.com/halloween/applebobbing.phtml')
    applebob = driver.find_element_by_id('bob_button')
    applebob.click()


def bank_interest(): # collect bank interest
    driver.get('http://www.neopets.com/bank.phtml')
    interest = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/div/form/input[2]')
    interest.click()


def shrine(): # visit coltzans shrine
    driver.get('http://www.neopets.com/desert/shrine.phtml')
    coltzan = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/div/form[1]/input[2]')
    coltzan.click()


def fruit_machine(): # spins fruit machine
    driver.get('http://www.neopets.com/desert/fruit/index.phtml')
    spin = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/input[3]').click()


def meteor(): # pokes meteor
    driver.get('http://www.neopets.com/moon/meteor.phtml?getclose=1')
    meteorAction = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/div/form/select/option[2]')
    meteorAction.click()
    # pokeSelect = Select(driver.find_element_by_name('pickstep')
    # pokeSelect.select_by_value('1')
    poke = driver.find_element_by_name('meteorsubmit')
    poke.click()


def slorg(): # visits shop of offers for money drop
    driver.get('http://www.neopets.com/shop_of_offers.phtml?slorg_payout=yes')


def symol(): # goes down symol hole
    driver.get('http://www.neopets.com/medieval/symolhole.phtml')
    symolHole = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/center/form/input[3]')
    symolHole.click()


def toychest(): # gets item from toy chest
    driver.get('http://www.neopets.com/petpetpark/daily.phtml')
    openToyChest = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td/div/div/div[2]/div/form/a/img')
    openToyChest.click()


def fishing(): # goes fishing
    driver.get('http://www.neopets.com/water/fishing.phtml')
    fish = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/center[1]/form/input[2]')
    fish.click()


def plushie(): # visit Grundo plushie for drop
    driver.get('http://www.neopets.com/faerieland/tdmbgpop.phtml')
    talkToPlushie = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/input[2]')
    talkToPlushie.click()


def tombola(): # draw tombola lottery
    driver.get('http://www.neopets.com/island/tombola.phtml')
    playTombola = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[2]/center[2]/form/input')
    playTombola.click()


def lunartemple():  # goes to lunar temple and picks correct answer to puzzle
    driver.get('http://www.neopets.com/shenkuu/lunar/?show=puzzle')
    soup = BeautifulSoup(driver.page_source,"html.parser")
    soupString = str(soup) #have to convert to string because page creates a new unique item every time
    soupRegex = r'(angleKreludor=)([0-9]{1,3})'
    findAngle = re.search(soupRegex, soupString)
    kAngle = int(findAngle.group(2))
    phase = ['//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[1]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[2]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[3]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[4]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[5]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[6]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[7]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[1]/td[8]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[1]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[2]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[3]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[4]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[5]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[6]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[7]/input',
             '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr[2]/td[8]/input']
    # Angle answers taken from http://www.thedailyneopets.com/articles/solving-lunar-temple-puzzle/
    if 169 <= kAngle <= 191:
        phaseSelect = driver.find_element_by_xpath(phase[0])
        phaseSelect.click()
    elif 192 <= kAngle <= 213:
        phaseSelect = driver.find_element_by_xpath(phase[1])
        phaseSelect.click()
    elif 214 <= kAngle <= 236:
        phaseSelect = driver.find_element_by_xpath(phase[2])
        phaseSelect.click()
    elif 237 <= kAngle <= 258:
        phaseSelect = driver.find_element_by_xpath(phase[3])
        phaseSelect.click()
    elif 259 <= kAngle <= 281:
        phaseSelect = driver.find_element_by_xpath(phase[4])
        phaseSelect.click()
    elif 283 <= kAngle <= 303:
        phaseSelect = driver.find_element_by_xpath(phase[5])
        phaseSelect.click()
    elif 304 <= kAngle <= 326:
        phaseSelect = driver.find_element_by_xpath(phase[6])
        phaseSelect.click()
    elif 327 <= kAngle <= 348:
        phaseSelect = driver.find_element_by_xpath(phase[7])
        phaseSelect.click()
    elif 0 <= kAngle <= 11 or 349 <= kAngle <= 360:
        phaseSelect = driver.find_element_by_xpath(phase[8])
        phaseSelect.click()
    elif 12 <= kAngle <= 33:
        phaseSelect = driver.find_element_by_xpath(phase[9])
        phaseSelect.click()
    elif 34 <= kAngle <= 56:
        phaseSelect = driver.find_element_by_xpath(phase[10])
        phaseSelect.click()
    elif 57 <= kAngle <= 78:
        phaseSelect = driver.find_element_by_xpath(phase[11])
        phaseSelect.click()
    elif 79 <= kAngle <= 101:
        phaseSelect = driver.find_element_by_xpath(phase[12])
        phaseSelect.click()
    elif 102 <= kAngle <= 123:
        phaseSelect = driver.find_element_by_xpath(phase[13])
        phaseSelect.click()
    elif 124 <= kAngle <= 146:
        phaseSelect = driver.find_element_by_xpath(phase[14])
        phaseSelect.click()
    elif 147 <= kAngle <= 168:
        phaseSelect = driver.find_element_by_xpath(phase[15])
        phaseSelect.click()


def allTheFreebies(): # gets the most common freebies
    jelly()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    omelette()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    springs()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    apples()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    bank_interest()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    shrine()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    fruit_machine()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "fruitResult")))
    meteor()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    slorg()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    symol()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    toychest()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    fishing()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "content")))
    plushie()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/table/tbody/tr/td[2]/center/form/input')))
    tombola()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/table/tbody/tr/td[1]/div[1]/table/tbody/tr[2]/td')))
    lunartemple()


def visitBank():  # visits bank, lets user deposit/withdraw
    print('Please Wait')
    driver.get('http://www.neopets.com/bank.phtml')
    currentNP = driver.find_element_by_css_selector('#npanchor')
    print('Current NP: ', currentNP.text)
    doneBanking = False
    while not doneBanking:
        bankDW = input('Deposit or Withdraw?:')
        if bankDW == 'Deposit' or 'deposit':
            addNP = input('How much would you like to deposit? -->')
            depositNP = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[1]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/form/input[2]')
            depositNP.send_keys(addNP)
            submit = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[1]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/form/input[3]')
            submit.click()
            driver.switch_to.alert.accept()
            doneBanking = True

        elif bankDW == 'Withdraw' or 'withdraw':
            takeNP = input('How much would you like to withdraw? -->')
            withdrawNP = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[1]')
            withdrawNP.send_keys(takeNP)
            submit = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[2]')
            submit.click()
            driver.switch_to.alert.accept()
            doneBanking = True


def inv_navigator(inventory_number):  # returns correct xpath for cell in inventory
    if math.floor(inventory_number % 6) == 0:
        row = math.floor(inventory_number/6)
        cell = 6
    else:
        row = math.floor(inventory_number/6)+1
        cell = inventory_number % 6
    return '//*[@id="content"]/table/tbody/tr/td[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[{line}]/td[{cell_num}]'.format(line=row, cell_num=cell)


def feedPet(pet):  # feeds indicated pet
    feed_input = input('How many times do you want to feed? \n ---->')
    feed_int = int(feed_input)
    driver.get('http://www.neopets.com/inventory.phtml')
    for x in range(0, feed_int):
        i = 1
        while i < 50:  # checks if first item in inventory is edible, keeps moving to next cell until food is found
            try:
                cell = driver.find_element_by_xpath(inv_navigator(i))
                cell.click()
                WebDriverWait(driver,3)
                driver.switch_to.window(driver.window_handles[1])
                select = Select(driver.find_element_by_name("action"))
                try:
                    select.select_by_visible_text("Feed to {pet_name}.".format(pet_name=pet))
                    driver.find_element_by_id("submit").click()
                    WebDriverWait(driver,2)
                    driver.find_element_by_tag_name('input').click()
                    driver.switch_to.window(driver.window_handles[0])
                    i = 100
                except NoSuchElementException:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    # print('Item not food')
                    i += 1
            except NoSuchElementException:
                print('There is no food in your inventory. Stock up!')
                i = 100


def stats():  # displays basic status of neopets things
    driver.get('http://www.neopets.com/inventory.phtml')
    np_amount = driver.find_element_by_xpath('//*[@id="npanchor"]')
    inv_amount = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[2]/div[3]/table/tbody/tr[2]/td/b[1]')
    active_pet_hunger = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[1]/div[1]/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/b')
    print('Current NP:', np_amount.text)
    print('Inventory: ', inv_amount.text)
    print('Active Pet Hunger: ', active_pet_hunger.text)






print('Welcome to NeoAuto.')
username_input = input('Username:')
password_input = input('Password:')

driver = webdriver.Firefox()
driver.get("http://www.neopets.com/")

login = driver.find_element_by_link_text("Log in")
login.click()

username = driver.find_element_by_name("username")
username.send_keys(username_input)
username.send_keys(Keys.TAB)

password = driver.find_element_by_name("password")
password.send_keys(password_input)
password.send_keys(Keys.RETURN)

driver.find_element_by_css_selector('#npanchor')

getPets()

donePlaying = False
prompts = ['jelly', 'omelette', 'springs', 'apple', 'interest', 'shrine',  'fruit', 'meteor', 'slorg', 'symbol',
           'toychest', 'fishing', 'plushie', 'tombola', 'temple', 'do all', 'bank', 'feed kiko', 'feed aisha',
           'status', 'exit']
while not donePlaying:
    freebie = input('NeoAuto ---->')
    if freebie == 'jelly':
        jelly()
    elif freebie == 'omelette':
        omelette()
    elif freebie == 'springs':
        springs()
    elif freebie == 'apple':
        apples()
    elif freebie == 'interest':
        bank_interest()
    elif freebie == 'shrine':
        shrine()
    elif freebie == 'fruit':
        fruit_machine()
    elif freebie == 'meteor':
        meteor()
    elif freebie == 'slorg':
        slorg()
    elif freebie == 'symbol':
        symol()
    elif freebie == 'toychest':
        toychest()
    elif freebie == 'fishing':
        fishing()
    elif freebie == 'plushie':
        plushie()
    elif freebie == 'tombola':
        tombola()
    elif freebie == 'temple':
        lunartemple()
    elif freebie == 'do all':
        allTheFreebies()
    elif freebie == 'bank':
        visitBank()
    elif freebie == 'feed kiko':
        feedPet(pets[1])
    elif freebie == 'feed aisha':
        feedPet(pets[0])
    elif freebie == 'status':
        stats()
    elif freebie == 'exit':
        donePlaying = True

    elif freebie == 'help':
        print('Note all prompts should be entered in lowercase.\n')
        for prompt in prompts:
            print(prompt, '\n')
    else:
        print('Invalid prompt. Type \'help\' to see all prompts')

driver.close()
