# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:26:20 2021

@author: pruthvirajg
"""

import re

def merge_lists(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


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
            