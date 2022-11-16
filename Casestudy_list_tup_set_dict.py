# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 22:04:02 2022

@author: hp
"""
#1) what is the output of var= "james"*2*3
var= "james" * 2 * 3
print(var)

#2)create a list(month_list) with month names and print values as "Thia is month of January"
month_list=["January", "Febuary", "March", "April", "May", "June","July", "August", "September", "October","November", "December"]
for months in month_list:
    print("This is month of ", months)
      
   
    
#3)Create a tuple(year_tup) with years from 1947 to 2022    
tup=[]
for i in range (1947,2023):
    tup.append(i)
#tup
year_tup=tuple(tup)
year_tup





#flower=[]
#color_list=["Green","Yellow","Red","White","Pink"]
#for colors in color_list:
  # flower.append(colors)
#print(flower)
#flower_set=set(flower)
 


#flower={"Green","Yellow","Red","White","Pink","Orange","Voilet"}
#for colors in flower:
#    print(colors)
 #   flower_set=set("colors")
    
#4)Create a set (flowers_set) with colors names at least 5 colors names
color_list=["Green","Yellow","Red","White","Pink"]
set={color_list[i] for i in range(len(color_list))}
print(set)


#5)Create a dict with your friends names and his/her quality like(funny,intelligent,smart ect)
friend_names=["jyo","rani","bindu","mani","naidu","naik"]
quality=["smart","intelligent","friendly","hardworker","funny","jovial"]
dict={friend_names[i]:quality[i] for i in range(len(friend_names))}
print(dict)

#6) Create a dict with family members names and relations
family_member=["param","karthi","padma", "bhavani","srinu","lakshmi","venkatrao"]
relation=["husband","daughter","mother","sister","father","mother_inla","father_inla"]
dict={family_member[i]:relation[i] for i in range(len(family_member))}
print(dict)