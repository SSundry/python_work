#Make of list of three people you'd like to invite and print messages to them.
guest_list= ['kaz brekker', 'roxas', 'yusuke urameshi']
print(guest_list)
kaz= 'kaz brekker'
roxas= guest_list[1]
yusuke= guest_list[-1]
print(f"{kaz.upper()} didn't need a reason.")
print(f"It's sad that {roxas.title()} realized that he is a nobody!")
print(f'"SPIRIT GUN!!!" said {yusuke.title()}.')
#Modify your list and replace the name of a guest with another
guest_list[1]= 'isaac'
#Print the new messages
print(f"Unfortunately, {roxas.title()} is on the run and is unable to attend.")
print(f"{guest_list[1].upper()} is the best character.")
#Print the new guest list
print(guest_list)
#insert() a new guest at the beginning and middle of your list
guest_list.insert(0, 'kurapika')
guest_list.insert(2, 'utena')
#append() a new guest at the end of your list
guest_list.append('haru okumura')
#print new guest list
print(guest_list)
#print the messages
kura= guest_list[0]
utena= guest_list[2]
haru= guest_list[-1]
print(f"{kura.upper()} has scarlet eyes.")
print(f"{utena.title()} wants to be a prince!")
print(f"I think {haru.title()} needs to spend time away from her boyfriends??")
final_message= "I must apologize for the late notice, but my abode can house only two guests for now."
print(final_message)
#pop method w/o numb er will remove the final item. Use number to pick which item is removed
popped_guest_1= guest_list.pop(1)
print(f"{popped_guest_1.upper()} did not leave a reason.")
popped_guest_2= guest_list.pop(0)
print(f"{popped_guest_2.upper()} will skip the dinner because he has not found all of the scarlet eyes!")
print(guest_list)
popped_guest_3= guest_list.pop(0)
popped_guest_4= guest_list.pop(1)
print(f"{popped_guest_3.title()} and {popped_guest_4.title()} will not be joining because they are with their significant others.")
print(guest_list)
#Check how many guests are coming and print a message
number= len(guest_list)
#f"" is always at the beginning of the string
print(f"\nThere will be {number} guests that will be coming over for dinner.")