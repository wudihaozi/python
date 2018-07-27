import shelve
shelFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelFile['cats'] = cats
shelFile.close()

shelFile = shelve.open('mydata')
print(type(shelFile))
# <class 'shelve.DbfilenameShelf'>
print(shelFile['cats'])
# ['Zophie', 'Pooka', 'Simon']
print(list(shelFile.keys()))
# ['cats']
print(list(shelFile.values()))
# [['Zophie', 'Pooka', 'Simon']]
shelFile.close()