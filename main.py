import xml.etree.ElementTree
from tkinter import filedialog as fd
import os
import getpass
import fnmatch
import xml.etree.ElementTree as ET
import time

missing_Text_id_list = []
missing_Describe_Population_list = []
missing_Describe_Wildlife_list = []
missing_Describe_Terrain_list = []
missing_Describe_Weather_list = []
missing_Describe_Tactical_list = []
missing_Describe_Advantage_list = []
missing_Describe_History_list = []
missing_Planet_Ability_Name_list = []
missing_Planet_Ability_Description_list = []
missing_Encyclopedia_Text_list = []
missing_Encyclopedia_Weather_Name_list = []
missing_Encyclopedia_Weather_Info_list = []
files_completed = 0


#<=============================================SELECT FILE DEPENDING ON OS=============================================>
if os.name == "posix":
    username = getpass.getuser()
    data_directory = fd.askdirectory(title="Please locate your 'Empire at War' mod data folder",
                                     initialdir=f'/home/{username}/.steam/steam/steamapps/common/Star Wars Empire at War/corruption')
    xml_directory = data_directory + '/XML'
    dat_file_location = data_directory + '/Text/mastertextfile_english.dat'
    #dat is referring to a .dat file and not the mispronunciation of the word 'That'

elif os.name == 'nt':
    data_directory = fd.askdirectory(title="Please locate your 'Empire at War' mod data folder",
                                     initialdir=f'C:/Program Files (x86)/Steam/steamapps/common/Star Wars Empire at War/corruption')
    xml_directory = data_directory + '/XML'
    dat_file_location = data_directory + '/Text/mastertextfile_english.dat'
    # dat is referring to a .dat file and not the mispronunciation of the word 'That'

else:
    data_directory = fd.askdirectory(title="Please locate your 'Empire at War' mod data folder")
    xml_directory = data_directory + '/XML'
    dat_file_location = data_directory + '/Text/mastertextfile_english.dat'
    # dat is referring to a .dat file and not the mispronunciation of the word 'That'


#<========================================FIND ALL XML FILES IN CORRECT FOLDER=========================================>
xml_files = fnmatch.filter(os.listdir(xml_directory), '*.xml') + fnmatch.filter(os.listdir(xml_directory), '*.XML')
number_of_files = len(xml_files) + 3
print(f'{number_of_files} files in the XML Folder')

with open(dat_file_location, 'rb') as dat_binary:
    content = str(dat_binary.read())


#<======================================START FINDING MISSING TEXT_ID TAGS=============================================>
for xml_file in os.listdir(xml_directory):
    time.sleep(.01)
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
    files_completed = files_completed + 1
    if files_completed == number_of_files:
        percent_complete = ((files_completed / number_of_files)*100)
    else:
        percent_complete = ((files_completed / number_of_files)*100)-1
    print(f'''Checking for missing "Text_ID" tags.
    {files_completed} of {number_of_files} files.
    {percent_complete:.0f}% Complete''')
    current_file = xml_file
    if xml_file == 'ENUM' or xml_file == 'AI':
        pass
    else:
        # Ignore files that aren't xml or don't have  text in vanilla game
        if xml_file == 'ANIMATIONSFXMAPS.TXT' or \
                xml_file == 'SFXEVENTSUNITSREBELHEROES.XML' or \
                xml_file == 'SFXEVENTSUNITSCAPITAL.XML' or \
                xml_file == 'SFXEVENTS_EXP_HUD.XML' or \
                xml_file == 'SFXEVENTSCINEMATICS.XML' or \
                xml_file == 'SFXEVENTS_EXP_UNITSHEROES.XML' or \
                xml_file == 'SFXEVENTS_EXP_UNITSGROUND.XML' or \
                xml_file == 'SFXEVENTSUNITSEMPIREHEROES.XML' or \
                xml_file == 'SFXEVENTSUNITSGROUND.XML' or \
                xml_file == 'SFXEVENTSUNITSCORVETTES.XML' or \
                xml_file == 'SFXEVENTS_EXP_UNITSSPACE.XML' or \
                xml_file == 'SFXEVENTSUNITSTRANSPORTS.XML' or \
                xml_file == 'SFXEVENTSHUD.XML' or \
                xml_file == 'SFXEVENTSUNITSFIGHTERS.XML' or \
                xml_file == 'SFXEVENTSUNITSFRIGATES.XML' or \
                xml_file == 'SFXEVENTSGUI.XML' or \
                xml_file == 'PROJECTILES.XML' or \
                xml_file == 'PROPS_SNOW.XML' or \
                xml_file == 'PROPS_FOREST.XML' or \
                xml_file == 'PROPS_SWAMP.XML' or \
                xml_file == 'PROPS_URBAN.XML' or \
                xml_file == 'PROPS_VOLCANIC.XML' or \
                xml_file == 'PROPS_FELUCIA.XML' or \
                xml_file == 'PROPS_STORY.XML' or \
                xml_file == 'PROPS_GENERIC.XML' or \
                xml_file == 'PROPS_DESERT.XML' or \
                xml_file == 'PROPS_TEMPERATE.XML' or \
                xml_file == 'SPACEPROPS.XML' or \
                xml_file == 'SPEECHEVENTS.XML':
            pass
        else:
            try:
                #<===================== FIND ALL THE TEXT ID TAGS AND MAKE SURE WE HAVE A STRING ======================>
                xml_file = xml_directory + f'/{xml_file}'
                file = open(xml_file, 'r')
                tree = ET.parse(xml_file)
                root = tree.getroot()
                tag = 'Text_ID'
                for elm in root.iter(tag):
                    if elm.text is None:
                        pass
                    else:
                        string = str(elm.text)
                        string = string.replace(' ', '')
                        if string in content:
                            pass
                        else:
                            missing_Text_id_list.append(f'{string} is missing {tag} tag in the file {current_file}')
                file.close()
            except xml.etree.ElementTree.ParseError:
                pass


#<=========================================FIND MISSING DESCRIBE_POPULATION TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
    Checking for missing "Describe_Population" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_Population'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_Population_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()

#<=========================================FIND MISSING Describe_Wildlife TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
    Checking for missing "Describe_Wildlife" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_Wildlife'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_Wildlife_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Describe_Wildlife TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
    Checking for missing "Describe_Terrain" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_Terrain'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_Terrain_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Describe_Weather TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
    Checking for missing "Describe_Weather" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_Weather'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_Terrain_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Describe_Tactical TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
    Checking for missing "Describe_Tactical" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_Tactical'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_Tactical_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()

#<=========================================FIND MISSING Describe_Advantage TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
    Checking for missing "Describe_Advantage" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_Advantage'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_Advantage_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Describe_History TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
    Checking for missing "Describe_History" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Describe_History'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Describe_History_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Planet_Ability_Name TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
"Describe_History" tags ✅
    Checking for missing "Planet_Ability_Name" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Planet_Ability_Name'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Planet_Ability_Name_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Planet_Ability_Description TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
"Describe_History" tags ✅
"Planet_Ability_Name" tags ✅
    Checking for missing "Planet_Ability_Description" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Planet_Ability_Description'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Planet_Ability_Description_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Encyclopedia_Text TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
"Describe_History" tags ✅
"Planet_Ability_Name" tags ✅
"Planet_Ability_Description" tags ✅
    Checking for missing "Encyclopedia_Text" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Encyclopedia_Text'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Encyclopedia_Text_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Encyclopedia_Weather_Name TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
"Describe_History" tags ✅
"Planet_Ability_Name" tags ✅
"Planet_Ability_Description" tags ✅
"Encyclopedia_Text" tags ✅
    Checking for missing "Encyclopedia_Weather_Name" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Encyclopedia_Weather_Name'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Encyclopedia_Weather_Name_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<=========================================FIND MISSING Encyclopedia_Weather_Info TAGS=======================================>
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
print(f'''
"Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
"Describe_History" tags ✅
"Planet_Ability_Name" tags ✅
"Planet_Ability_Description" tags ✅
"Encyclopedia_Text" tags ✅
"Encyclopedia_Weather_Name" tags ✅
    Checking for missing "Encyclopedia_Weather_Info" tags.''')

current_file = '/PLANETS.XML'
planet_xml = xml_directory + current_file
file = open(planet_xml, 'r')
tree = ET.parse(planet_xml)
root = tree.getroot()
tag = 'Encyclopedia_Weather_Info'
for elm in root.iter(tag):
    if elm.text is None:
        pass
    else:
        string = str(elm.text)
        string = string.replace(' ', '')
        if string in content:
            pass
        else:
            missing_Encyclopedia_Weather_Info_list.append(f'{string} is missing {tag} tag in the file {current_file}')
file.close()


#<======================================START FINDING MISSING Encyclopedia_Text TAGS=============================================>
files_completed = 0
for xml_file in os.listdir(xml_directory):
    time.sleep(.01)
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
    files_completed = files_completed + 1
    if files_completed == number_of_files:
        percent_complete = ((files_completed / number_of_files)*100)
    else:
        percent_complete = ((files_completed / number_of_files)*100)-1
    print(f'''"
Text_ID" tags ✅
"Describe_Population" tags ✅
"Describe_Wildlife" tags ✅
"Describe_Terrain" tags ✅
"Describe_Weather" tags ✅
"Describe_Tactical" tags ✅
"Describe_Advantage" tags ✅
"Describe_History" tags ✅
"Planet_Ability_Name" tags ✅
"Planet_Ability_Description" tags ✅
"Encyclopedia_Text" tags ✅
"Encyclopedia_Weather_Name" tags ✅
    Checking for missing "Encyclopedia_Text" tags (in all files).
    {files_completed} of {number_of_files} files.
    {percent_complete:.0f}% Complete''')
    current_file = xml_file
    if xml_file == 'ENUM' or xml_file == 'AI':
        pass
    else:
        # Ignore files that aren't xml or don't have  text in vanilla game
        if xml_file == 'ANIMATIONSFXMAPS.TXT' or \
                xml_file == 'SFXEVENTSUNITSREBELHEROES.XML' or \
                xml_file == 'SFXEVENTSUNITSCAPITAL.XML' or \
                xml_file == 'SFXEVENTS_EXP_HUD.XML' or \
                xml_file == 'SFXEVENTSCINEMATICS.XML' or \
                xml_file == 'SFXEVENTS_EXP_UNITSHEROES.XML' or \
                xml_file == 'SFXEVENTS_EXP_UNITSGROUND.XML' or \
                xml_file == 'SFXEVENTSUNITSEMPIREHEROES.XML' or \
                xml_file == 'SFXEVENTSUNITSGROUND.XML' or \
                xml_file == 'SFXEVENTSUNITSCORVETTES.XML' or \
                xml_file == 'SFXEVENTS_EXP_UNITSSPACE.XML' or \
                xml_file == 'SFXEVENTSUNITSTRANSPORTS.XML' or \
                xml_file == 'SFXEVENTSHUD.XML' or \
                xml_file == 'SFXEVENTSUNITSFIGHTERS.XML' or \
                xml_file == 'SFXEVENTSUNITSFRIGATES.XML' or \
                xml_file == 'SFXEVENTSGUI.XML' or \
                xml_file == 'PROJECTILES.XML' or \
                xml_file == 'PROPS_SNOW.XML' or \
                xml_file == 'PROPS_FOREST.XML' or \
                xml_file == 'PROPS_SWAMP.XML' or \
                xml_file == 'PROPS_URBAN.XML' or \
                xml_file == 'PROPS_VOLCANIC.XML' or \
                xml_file == 'PROPS_FELUCIA.XML' or \
                xml_file == 'PROPS_STORY.XML' or \
                xml_file == 'PROPS_GENERIC.XML' or \
                xml_file == 'PROPS_DESERT.XML' or \
                xml_file == 'PROPS_TEMPERATE.XML' or \
                xml_file == 'SPACEPROPS.XML' or \
                xml_file == 'PLANETS.XML' or \
                xml_file == 'PLANETS.XML' or \
                xml_file == 'SPEECHEVENTS.XML':
            pass
        else:
            try:
                #<===================== FIND ALL THE Encyclopedia_Text TAGS AND MAKE SURE WE HAVE A STRING ======================>
                xml_file = xml_directory + f'/{xml_file}'
                file = open(xml_file, 'r')
                tree = ET.parse(xml_file)
                root = tree.getroot()
                tag = 'Encyclopedia_Text'
                for elm in root.iter(tag):
                    if elm.text is None:
                        pass
                    else:
                        string = str(elm.text)
                        string = string.replace(' ', '')
                        if string in content:
                            pass
                        else:
                            missing_Encyclopedia_Text_list.append(f'{string} is missing {tag} tag in the file {current_file}')
                file.close()
            except xml.etree.ElementTree.ParseError:
                pass

#<===============================================PRINT MISSING STRINGS=================================================>
dat_binary.close()

for file in missing_Text_id_list:
    print(file)
for file in missing_Describe_Population_list:
    print(file)
for file in missing_Describe_Wildlife_list:
    print(file)
for file in missing_Describe_Terrain_list:
    print(file)
for file in missing_Describe_Weather_list:
    print(file)
for file in missing_Describe_Tactical_list:
    print(file)
for file in missing_Describe_Advantage_list:
    print(file)
for file in missing_Describe_History_list:
    print(file)
for file in missing_Planet_Ability_Name_list:
    print(file)
for file in missing_Planet_Ability_Description_list:
    print(file)
for file in missing_Encyclopedia_Text_list:
    print(file)
for file in missing_Encyclopedia_Weather_Name_list:
    print(file)
for file in missing_Encyclopedia_Weather_Info_list:
    print(file)


total = len(missing_Text_id_list) + len(missing_Describe_Population_list) + len(missing_Describe_Wildlife_list) + len(missing_Describe_Terrain_list) + len(missing_Describe_Weather_list) + len(missing_Describe_Tactical_list) + len(missing_Describe_Advantage_list) + len(missing_Describe_History_list) + len(missing_Planet_Ability_Name_list) + len(missing_Planet_Ability_Description_list) + len(missing_Encyclopedia_Text_list) + len(missing_Encyclopedia_Weather_Name_list) + len(missing_Encyclopedia_Weather_Info_list)

print(f'''
Missing "Text_ID" Tag {len(missing_Text_id_list)}
Missing "Describe_Population" Tag {len(missing_Describe_Population_list)}
Missing "Describe_Wildlife" Tag {len(missing_Describe_Wildlife_list)}
Missing "Describe_Terrain" Tag {len(missing_Describe_Terrain_list)}
Missing "Describe_Weather" Tag {len(missing_Describe_Weather_list)}
Missing "Describe_Tactical" Tag {len(missing_Describe_Tactical_list)}
Missing "Describe_Advantage" Tag {len(missing_Describe_Advantage_list)}
Missing "Describe_History" Tag {len(missing_Describe_History_list)}
Missing "Planet_Ability_Name" Tag {len(missing_Planet_Ability_Name_list)}
Missing "Planet_Ability_Description" Tag {len(missing_Planet_Ability_Description_list)}
Missing "Encyclopedia_Text" Tag {len(missing_Encyclopedia_Text_list)}
Missing "Encyclopedia_Weather_Name" Tag {len(missing_Encyclopedia_Weather_Name_list)}
Missing "Encyclopedia_Weather_Info" Tag {len(missing_Encyclopedia_Weather_Info_list)}
TOTAL MISSING TAGS: {total}''')
