# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:52:47 2021

@author: pruthvirajg
"""


with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        Split_grades = grades.split('\n')
        # match = [grades for grades in grades.split() if grades.endswith('B')]
        list_Names = list()
        for gline in Split_grades:
            if not gline: continue
            Names_found = gline.split(':')
            Names_found = [x.strip(' ') for x in Names_found]
            if Names_found[1].endswith('B'):
                list_Names.append(Names_found[0])

                