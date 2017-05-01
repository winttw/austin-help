count = 0

def getNewItem(list):
    item = []
    key = input("Enter the name of the new item")
    weight = int(input("Enter the weight of the new item"))
    cost = int(input("Enter cost of the new item"))
    magic = input("Is item magic? True, False")
    item.append(key)
    item.append(weight)
    item.append(cost)
    if magic == True:
        item.append(True)
    else:
        item.append(False)
    addInOrder(list,item)
    return

def modifyItem(list):
    index = int(input("\nEnter the index number for an item in inventory: "))
    x= int(input("which do you want to modify name =0 weight=1 or cost=2 "))
    if x=0:
        y=input("Enter the name of the new item")
    elif x=1:
        y=int(input("Enter the weight of the new item"))
    elif x=2:
        y=int(input("Enter cost of the new item"))
    else: print("Unknown choice")
    
    list[index,x]=y
    return

def inventoryCounter(list):
    if len(list) == 1:
        print("your inventory is full")
    choice = input("Enter your choice (Add, Modify, Delete, List,Save, Open)")
    choice=choice.lower()
    ProgramStart()
        
    else:
        pass
        
    return
    
def delete(list,item):
     index = int(input("\nEnter the index number for an item to delete in the inventory: "))
     list.delete(index)
    
def addInOrder(list,item):

    if(list==[]):
        list.append(item)
    else:
        index = 0
        
        #item = [name, weight, active(T/F)]
        
        while (index < len(list) and list[index][0] < item[0]):
            index = index + 1
        list.insert(index,item)
def ProgramStart():
    while (choice[0] != "q"):
    if (choice[0] == "a"):
        #add
        getNewItem(list)
    elif (choice[0] == "m"):
        #modify
        pass
    elif (choice[0] == "d"):
        #delete
        pass
    elif (choice[0] == "l"):
        #list
        #REMEMBER, your listing should be prettier than this!
        print(list)
        print(len(list))
        print(count)
    elif (choice[0] == "s"):
        #save
        pass
    elif (choice[0] == "o"):
        #open
        pass
    else:
        print("Unknown choice")

#main
list = []

choice = input("Enter your choice (Add, Modify, Delete, List,Save, Open)")
choice=choice.lower()
ProgramStart()
    choice = input("Enter your choice (Add, Modify, Delete, List,Save, Open)")
    choice=choice.lower()
    inventoryCounter(list)


