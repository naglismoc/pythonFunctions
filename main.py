

# arr = [1, 5, 10]
# sum = 0
# count = 0
# for i in arr:
#     count += 1
#     sum += i
# print(sum / count)


# arr2 = [7,9,1,1,6,684,16,6,8,105,0.5,68,0.5,3551,31,165,3]
#
def avg(arr):
    sum = 0
    count = 0
    for i in arr:
        count += 1
        sum += i
    return sum / count


# print("Aušros gimnazijos studento pažymių vidurkis yra " + str(avg(arr)))


#
# print( avg(arr) )
# print( avg(arr2) )
#
# arr3 = [5,5,5,5,5,5,5,5,5,55,5]
#
# print(avg(arr3))



def sayHi(): #nieko nepriima ir nieko negražina
    print("hi")

sayHi()
sayHi()
sayHi()
sayHi()
print(sayHi())

def simPi(): #nieko nepriima, grazina skaiciu
    return 3.14

print( simPi() )

def sayHiTo(name): #priima, bet nieko negražina
    print(f'hi {name.upper()}')

sayHiTo("Jonas")
sayHiTo("Vilius")
vardas = "Jurgis"
sayHiTo(vardas)

def intSum (a, b):#priima, gražina
    return a + b

result = intSum(16,36)
print(result)

def makeCoffee(type, temperature = "hot"):
    print(f'There u go, your {temperature} {type} coffee')

makeCoffee("black")
makeCoffee("Latte", "cold")



range(10)
range(1, 10)
range(1, 10, 2)