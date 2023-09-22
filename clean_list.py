list_1 = [1, 2, 3, 4, 5, "hello", 6, "hello", 7, "hello", 8, 9, 10]

def clean_list(list_obj, target):
    counter = list_obj.count(target)    

    for i in range(counter):

        try:
            target_index = list_obj.index(target)
            del list_obj[target_index]
        except:
            continue

    if list_obj.count(target) == 0:

        print("The List has been cleared of the value:", target)
        print(list_obj)

    else:
	    print("List cleaning has failed. Aborting ...")
	    

clean_list(list_1, "hello")
