num_list = [1,2,3,4]
name_list = ["one","two","three","four"]

print (dict([[y,num_list[x]] for x,y in enumerate(name_list)]))