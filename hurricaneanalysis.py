# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def update_damages(damages):
  updated_damages = []
  for data in damages:
    if data == "Damages not recorded":
      updated_damages.append(data)
    elif data != "Damages not recorded":
      convert_num = float(data[:-1])
      for key, value in conversion.items():
          if data[-1] == key:
              updated_damages.append(float(convert_num * value))
  return updated_damages
updated_damages = update_damages(damages)
# 2 
# Create a Table

# Create and view the hurricanes dictionary
def dictionary_creator(names):
  dataset = {}
  for i in range(0, len(names)):
    dataset[names[i]] = {"Name":names[i], "Month":months[i], "Year":years[i], "Max Sustained Wind":max_sustained_winds[i], "Areas Affected":areas_affected[i], "Damage":updated_damages[i], "Deaths":deaths[i]}
  return dataset
dataset = dictionary_creator(names)
#print(dataset)
# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

#Explaining my code: thsi function goes will take in the dataset that you want to organize. It will create a new dictionary
# for tracking purposes called, "year_dictionary". Then it will go through three loops. The first loop is to make sure
# that we go through every key,value option within the original dataset. The second for loop will go through every key, value option within the dictionary. e.g. 'Cuba I' is the key, the value is another dictionary. 'Bahamas' is the key, the value is another dictionary. The third for loop will make sure that we iterate through the dictionary key,values. We then check to see if any of the keys are equal to "Year" if they are, we then will add the value of that key to our 'year_dictionary' and assigning the value of the entire dictionary. Thus, the only thing we are changing in this dictionary is the key for every value. Instead of it being the 'name' it will be the year. We then assign the same value as the previous dictionary dataset. 
def reorg_by_year(dataset):
  year_dictionary = {}
  for i in range(0, len(dataset)):
    for key, value in dataset.items():
      for key2,value2 in value.items():
        if key2 == "Year":
          year_dictionary[value[key2]] = value
    return year_dictionary

year_dictionary = reorg_by_year(dataset)
#print(year_dictionary)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def affected_counter(dataset):
  affected_dictionary = {}
  for key,value in dataset.items():
    for key2,value2, in value.items():
      if key2 == "Areas Affected":
        for affected_area in value2:
          if affected_area not in affected_dictionary.keys():
            affected_dictionary[affected_area] = 1
          else:
            affected_dictionary[affected_area] += 1
  return affected_dictionary

affected_areas_dataset = affected_counter(dataset)
#print(affected_areas_dataset)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def max_hurricane_counter(affected_areas_dataset):
  highest_value = 0
  highest_affectedArea = {}
  for key,value in affected_areas_dataset.items():
    if value > highest_value:
      highest_affectedArea[key] = value
      highest_value = value
  return highest_affectedArea

most_affected = max_hurricane_counter(affected_areas_dataset)
#print(most_affected)
# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def highest_mortality(dataset):
  highest_mortality_list = ["", 0]
#First go around at obtaining largest values in total number of deaths
  for key,value in dataset.items():
    for key2, value2 in value.items():
      if key2 == "Deaths":
        if value2 > highest_mortality_list[1]:
          highest_mortality_list[0] = key
          highest_mortality_list[1] = value2
  return highest_mortality_list


highest_deaths_data = highest_mortality(dataset)
#print(highest_deaths_data)
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
def mortality_rating(dataset):
  rating_dictionary = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for key,value in dataset.items():
    for key2,value2 in value.items():
      finderVar = 0
      if key2 == "Deaths":
        # We find the associated "finderVar" which basically just assigns the key (name of the hurricane) a mortality range value that can alter be used to find its score. 
        if value2 == 0:
          rating_dictionary[0].append(key)
        elif value2 > mortality_scale[4]:
          rating_dictionary[5].append(key)
        else:
          for i in range(0, len(mortality_scale)-1):
            if value2 > mortality_scale[i] and value2 < mortality_scale[i+1]:
              rating_dictionary[i+1].append(key)     
  return rating_dictionary        
rating_dictionary = mortality_rating(dataset)
#print(rating_dictionary)

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
#print(dataset)
def highest_damage(dataset):
  name = ""
  cost = 0
  highest_damage = [name, cost]

  for key,value in dataset.items():
    for key2,value2 in value.items():
      if key2 == "Damage":
        if value2 != "Damages not recorded" and value2 > cost:
          cost = value2
          name = key
  return name, cost

highest_damage_data = highest_damage(dataset)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def hurricane_damage(dataset):
  hurricane_damage_data = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for key, value in dataset.items():
    for key2,value2 in value.items():
      if key2 == "Damage":
        #now we add all the zeros and amounts greater than 4 to dictionary to key 0 & 5's list respectively
        if value2 == "Damages not recorded":
          pass
        elif value2 == 0:
          hurricane_damage_data[0].append(key)
        elif value2 > damage_scale[4]:
          hurricane_damage_data[5].append(key)
        else:
          for i in range(0, len(damage_scale)-1):
            if value2 > damage_scale[i] and value2 < damage_scale[i+1]:
              hurricane_damage_data[i+1].append(key)
  return hurricane_damage_data

hurricane_damage_ratings = hurricane_damage(dataset)
#print(hurricane_damage_ratings)

#Completed by Abraham M on 02/23/2022
