#%% Task 1 - Edit code to print as requested
#PS3: Code Block 1

mountain = "Denali"
nickname = '\"Mt. McKinley\"'
elevation = "20322\'" 

print (mountain + ", formerly \nknown as " + nickname + "\nis " + elevation + "above sea level.")

#%% Task 2 - Lists and Iteration
data_folder = r"W:\859_data\triangle"
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]
user_item = "roads.shp"
data_list.append(user_item)

for item in data_list:
    print(data_folder + "\\" + item)

#%% Task 3 - Lists and iteration

user_numbers = []

for x in range(3):
    prompt = input('Enter an integer: ')
    user_numbers.append(int(prompt))

user_numbers.sort()
print(user_numbers[2])



# %% Challenge Task
userNumbers = []

for x in range(3):
    user_prompt = input('Enter an integer:')
    userNumbers.append(int(user_prompt))

userNumbers.sort(reverse=True)
print(userNumbers)


