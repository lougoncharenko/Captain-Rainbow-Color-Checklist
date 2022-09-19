# create
checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

checklist = []

def create(item):
    checklist.append(item)

#read
def read(index):
    return checklist[index]

#update
checklist = ['Blue', 'Orange']
checklist[0] = 'Cats'
print(checklist)

# delete
checklist = ['Blue', 'Cats']
def destroy(index):
    checklist.pop(index)
    print(checklist)

destroy(1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#list items
def list_all_colors():
    index=0
    for color in colors:
        print(f"{index} + {color}")
        index += 1

def mark_completed(index):
    index=0
    for color in colors:
        print(f"√{color}")
        index += 1
