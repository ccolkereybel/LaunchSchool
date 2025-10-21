my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]



list_index = 0 
item_number = 0

while list_index < len(my_list):
    item_number = 0
    while item_number < len(my_list[list_index]):
        if my_list[list_index][item_number] % 2 == 0:
            print(my_list[list_index][item_number])
        item_number += 1    
    list_index += 1
    
 
    






        




 




