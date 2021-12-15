# 1 - crear una funcion que genere una escusa aleatoria con esos datos 
# 2 - creeis otra funcion que cuente el numero de repeticiones de letras en cada array
# 3 - suprimir repeticiones en un array y devolver el array sin la repeticion
# 4 - function que invierta todos los valores de el array

# datos iniciales 
surnames = ['10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
escuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined']
dates = ['Jeferson', 'Matilda', 'R@fael', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M']

import random, operator

def numRadom (arr):
    return arr[random.randint(0,(len(arr)-1))]

def generateExcuse (arr1,arr2,arr3):
    excuse = numRadom(arr1)+' '+numRadom(arr2)+' '+numRadom(arr3)
    return excuse
print(generateExcuse(surnames,escuses,dates))

############################################################################

def reverseString(value):
    return value[::-1]

def reverseArr(arr):
    newArr=[]
    reverArr=arr[::-1]
    for i in reverArr:
        newArr.append(reverseString(i))
    return newArr
print(reverseArr(surnames))

############################################################################

def deleteRepetition(arr):
    return list(set(arr))
print(deleteRepetition(surnames))

###########################################################################

def countWord(word):
    obj={}
    wordLC= word.lower()
    for i in wordLC:
        if i in obj:
            obj[i]=obj[i]+1
        else:
            obj[i]=1
    return obj

def countArr(arr):
    newArr=[]
    for i in arr:
       newArr.append((i+':'+str(countWord(i))))
    return newArr
print(countArr(surnames))



