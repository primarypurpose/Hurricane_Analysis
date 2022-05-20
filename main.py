# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatan Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatan Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatan Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:


def new_damages(new_lst):
    updated_list = []
    for item in new_lst:
        if item == "Damages not recorded":
            updated_list.append(item)
        else:
            m_b = item[-1]
            value = float(item[:-1])
            if m_b == "M":
                updated_list.append(value * 1000000.00)
            elif m_b == "B":
                updated_list.append(value * 1000000000.00)
    return updated_list


updated_damages = new_damages(damages)
# print(updated_damages)

# write your construct hurricane dictionary function here:


def new_dictionary(name, month, year, max_wind, areas, damage, death):
    hurricane_dict = {}
    for i in range(0, len(name)):
        key = name[i]
        value = {}
        value.update({"Name": name[i], "Month": month[i], "Year": year[i], "Max_Sustained_Wind": max_wind[i],
                      "Areas_Affected": areas[i], "Damages": damage[i], "Deaths": death[i]})
        hurricane_dict.update({key: value})
    return hurricane_dict


hurricanes = new_dictionary(names, months, years, max_sustained_winds,
                            areas_affected, updated_damages, deaths)
# print(hurricanes)

# write your construct hurricane by year dictionary function here:


def hurricane_year(name_dict):
    new_dict = {}
    for name in name_dict.values():
        current_year = name["Year"]
        current_cane = name
        if current_year in new_dict:
            new_dict[current_year].append(current_cane)
        else:
            new_dict[current_year] = [current_cane]
    return new_dict


hurricanes_by_year = hurricane_year(hurricanes)
# print(hurricanes_by_year)

# write your count affected areas function here:


def count_affected_areas(hurricane_dict):
    affected_areas_count = {}
    for cane in hurricane_dict:
        for area in hurricane_dict[cane]["Areas_Affected"]:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count


# print(count_affected_areas(hurricanes))
areas_affected_count = count_affected_areas(hurricanes)

# write your find most affected area function here:


def most_areas_affected(affected_count):
    max_area = ""
    max_area_count = 0
    for area in affected_count:
        if affected_count[area] > max_area_count:
            max_area = area
            max_area_count = affected_count[area]
    return max_area, max_area_count


max_areas_affected = most_areas_affected(areas_affected_count)

# write your greatest number of deaths function here:


def max_number_deaths(hurricane_dict):
    max_deaths = 0
    max_deaths_name = ""
    max_deaths_year = ""
    for cane in hurricane_dict:
        if hurricane_dict[cane]["Deaths"] > max_deaths:
            max_deaths = hurricane_dict[cane]["Deaths"]
            max_deaths_name = cane
            max_deaths_year = hurricane_dict[cane]["Year"]
    return max_deaths_name, max_deaths, max_deaths_year


max_deaths_cane = max_number_deaths(hurricanes)
# print(max_deaths_cane)

# write your category by mortality function here:


def mortality_ratings(hurricane_dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    canes_death_scale = {0: [],
                         1: [],
                         2: [],
                         3: [],
                         4: [],
                         5: []}
    for cane in hurricane_dict:
        death_num = hurricane_dict[cane]["Deaths"]
        if death_num == 0:
            canes_death_scale[0].append(hurricane_dict[cane])
        elif mortality_scale[0] < death_num <= mortality_scale[1]:
            canes_death_scale[1].append(hurricane_dict[cane])
        elif mortality_scale[1] < death_num <= mortality_scale[2]:
            canes_death_scale[2].append(hurricane_dict[cane])
        elif mortality_scale[2] < death_num <= mortality_scale[3]:
            canes_death_scale[3].append(hurricane_dict[cane])
        elif mortality_scale[3] < death_num <= mortality_scale[4]:
            canes_death_scale[4].append(hurricane_dict[cane])
        else:
            canes_death_scale[5].append(hurricane_dict[cane])
    return canes_death_scale


hurricane_mortality_scale = mortality_ratings(hurricanes)
# print(hurricane_mortality_scale)
# write your greatest damage function here:


def max_damage(hurricane_dict):
    max_damages = 0
    max_damages_cane = ""
    for cane in hurricane_dict:
        if hurricane_dict[cane]["Damages"] == "Damages not recorded":
            continue
        elif hurricane_dict[cane]["Damages"] > max_damages:
            max_damages = hurricane_dict[cane]["Damages"]
            max_damages_cane = cane
    return max_damages_cane, max_damages


greatest_damage_hurricane = max_damage(hurricanes)
print(greatest_damage_hurricane)

# write your category by damage function here:


def damages_category(hurricane_dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    damages_cat = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in hurricane_dict:
        damages_num = hurricane_dict[cane]["Damages"]
        if damages_num == "Damages not recorded":
            continue
        elif damages_num == 0:
            damages_cat[0].append(hurricane_dict[cane])
        elif damage_scale[0] < damages_num <= damage_scale[1]:
            damages_cat[1].append(hurricane_dict[cane])
        elif damage_scale[1] < damages_num <= damage_scale[2]:
            damages_cat[2].append(hurricane_dict[cane])
        elif damage_scale[2] < damages_num <= damage_scale[3]:
            damages_cat[3].append(hurricane_dict[cane])
        elif damage_scale[3] < damages_num <= damage_scale[4]:
            damages_cat[4].append(hurricane_dict[cane])
        else:
            damages_cat[5].append(hurricane_dict[cane])
    return damages_cat


hurricane_damage_scale = damages_category(hurricanes)
# print(hurricane_damage_scale)
