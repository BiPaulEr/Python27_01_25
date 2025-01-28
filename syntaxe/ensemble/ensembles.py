mon_ensemble = {1, 2, 3}
print(type(mon_ensemble)) #<class 'set'>
#set()
mon_ensemble.add(99)
mon_ensemble.add(99)
mon_ensemble.add(99)
mon_ensemble.add(99)
mon_ensemble.add(99)
print(mon_ensemble) #{99, 1, 2, 3}

doublon = ["Renard", "Lievre", "Tortue", "Renard"]
unique = set(doublon)
doublon = list(unique)
print(doublon) #'Renard', 'Tortue', 'Lievre']
