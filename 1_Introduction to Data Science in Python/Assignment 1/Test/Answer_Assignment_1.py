"""
#**********************************************************************************************************
# Name : Assignment_1
# Author : Pruthvi Raj G :: (www.prudhvy.com )
# Version : Version 1.0 
# Description : Answer for Assignment_1.
# Input : 
# Date : 22-May-2021
#************************************************************************************************************

Question below:


"""

# Answer
# Part A
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    match = re.findall('[A-Z]\w+',simple_string) 
    return match   
        
    
names   
# raise NotImplementedError()

# Part B
# import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        Split_grades = grades.split('\n')
        # match = [grades for grades in grades.split() if grades.endswith('B')]
        list_Names = list()
        for gline in Split_grades:
            if not gline: continue
            if gline.endswith('B'):
                Names_found = gline.split(':')
                list_Names.append(Names_found[0])
    return list_Names

grades
# raise NotImplementedError()

def merge_lists(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

# import re


def merge_lists(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def logs():
    with open("assets/logdata.txt", "r") as file:
            logdata = file.read()
            Split_log = logdata.split('\n')
            Main_list = list()
            list_header = ['host','user_name','time','request']
            
            for splitted in Split_log:
                if not splitted: continue
                In_split = splitted.split(' ')
                host = In_split[0]
                user_name = In_split[2]
                time_temp = re.findall('\[.*?\]',splitted)
                time1 = time_temp[0][1:len(time_temp[0])-1]
                request_temp = re.findall('\".*?\"',splitted)
                request = request_temp[0][1:len(request_temp[0])-1]
                listdata = list()
                listdata.append(host)
                listdata.append(user_name)
                listdata.append(time1)
                listdata.append(request)
                
                Merged_list_single = merge_lists(list_header, listdata)
                Merged_list_single = dict(Merged_list_single)
                Main_list.append(Merged_list_single)
                listdata.clear()
            
    # raise NotImplementedError()
