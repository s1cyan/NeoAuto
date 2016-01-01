# NeoAuto

A Python automation program for Neopets. Does the most common neopets Dailies that do not require any maps. Also feed indicated pet x number of times. 

## How to use this project
**For Mac Users**
Assuming you already have python3 and Firefox installed.

If you do not already have pip installed- in terminal type: `sudo easy_install pip`

Install beautiful soup: `pip3 install beautifulsoup4`

Install selenium: `pip3 install selenium`

Download the file make sure the current directory in your terminal is in NeoAuto

To start the program, in terminal type: `python NeoAuto_CYAN.py`


## Things this project does 

**Dailies:**
**Note typing `do all` after the prompt `NeoAuto ---->` will do all the listed dailies in one go **
- Jelly 
- Omelette
- Healing Springs
- Apple Bobbing
- Bank Interest
- Coltzan's Shrine
- Fruit Machine
- Meteor
- Rich Slorg
- Symol Hole
- ToyChest
- Fishing Hole
- Plushie
- Tombola
- Lunar Temple (Selects correct answer every time)

**Feeding Pets**
When prompted and typing `feed` 
A list of your pets will appear. Select pet by number and after another prompt enter times you want to feed it. Food items will be used in the order of your inventory no matter the rarity of the item. Most commonly inedible items such as poisonous jelly/ smelly jelly will be automatically donated.  

Ex:
```
NeoAuto ---->feed
Which pet do you want to feed?
[ 0 ]   kiko_dance
[ 1 ]   noodles_t97
Select pet# ---->0
How many times do you want to feed? 
 ---->2
```
**Going to the bank**
Allows you to deposit/withdraw money from terminal

*Type `help` in prompt to get a list of all commands*

## Motivation 
This project was my final assignment for a python programming class. After the submission I made some tweaks to make it useable for everyone and also expanded the functionality of it. 
