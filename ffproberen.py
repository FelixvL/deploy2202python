import pandas
import matplotlib.pyplot as plt

bestand = pandas.read_csv("Pokemon.csv")
'''
print(bestand.sort_values(by=['HP'])["HP"])

tusse4en8 = bestand["HP"]>40
rest = bestand[tusse4en8]
filter2 = rest["HP"]<80
print(rest[filter2].sort_values(by=['HP'])["HP"])
print()
'''
lijst = []
for i, pok in bestand.iterrows():
#	print(pok)
	if (pok["HP"]>40 and pok["HP"]<80) :
		#print(pok)
		lijst.append(pok)

print(lijst)
for i in lijst:
	print(i.Name)

x = [1,2,3] 
y = [2,4,1] 
    
plt.scatter(bestand["Generation"], bestand["HP"]) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('My first graph!') 

plt.show() 

'''
print(bestand.columns)
print(bestand["Name"])
go = bestand["Generation"]==6 
nwlijst = bestand[go]
hoi = nwlijst["Legendary"]
print(nwlijst[hoi]["Name"])
for pok, ind in bestand.iterrows():
	print(ind)




print("test")

var1 = 4
var2 = "maandag"

print(var1)
print(var2)

# commentaar python vond java heel erg verbose boiler-plate-code
if var1 == 4:
	print("het is 4")
else:
	print("het is geen 4")

for x in range(2,10,3):
	print(x)

lijstje = [24,12,13,77,22,60,2]

for y in lijstje:
	print(y)
	print("-----")

var4 = int("6")
print(var4 * var4)

var6 = 55

print("dit is het getal"+str(var6))


def mijnfunctie():
	print("ik zit in de methode, mijn functie")

mijnfunctie()
mijnfunctie()


class Voetbal:
	kleur = 'wit'
	def voetballen(_Self):
		print("ik speel met de bal in kleur: "+_Self.kleur)

	def __init__(ab):
		print("dit is de construtor van Voetbal")

	def __init__(_self, nieuwekleur):
		_self.kleur = nieuwekleur

var9 = Voetbal("groen")
var9.voetballen()
var9.kleur = 'zwart'
var9.voetballen()

print(var9.kleur)

var10 = Voetbal('rood')

var10.voetballen()

'''









