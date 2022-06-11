# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:16:56 2022

@author: ppulivarthi
"""
#1st problem
student_roll_number_updated=[121,131,141,151]
for i in range(len(student_roll_number_updated)):
    student_roll_number_updated[i]+=100
print(student_roll_number_updated)

student_roll_number_updated
      
#  
a=[121,131,141,151]
for i in range(len(a)):
    a[i]+=100
    print("student_roll_number_updated",a[i])
    a[-1]    
    
#2  problem  
student_roll_number_updated=[121,131,141,151]
for i in range(len(student_roll_number_updated)):
    student_roll_number_updated[i]+=100
print(student_roll_number_updated)

student_roll_number_updated[-1]
 
#1
student_roll_number_updated=[]
for i in range(121,161,10):
    student_roll_number_updated.append(i)
print(student_roll_number_updated)

student_roll_number_updated[-1]
 


#3 problem     
student_roll_number_updated=[]   
for i in range(10,100,10):
    student_roll_number_updated.append(i)
# print(student_roll_number_updated,end=" ")
student_roll_number_updated


#4th problem
student_names=["ajay","ravi","kiranmai","tanuja","hamida"]
for i in student_names:
    print("The student is",i)
    
    
student_names=["ajay","ravi","kiranmai","tanuja","hamida"]
print("The student is",student_names[0]) 
print("The student is",student_names[1]) 
print("The student is",student_names[2])
print("The student is",student_names[3])
print("The student is",student_names[4])




student_names=["ajay","ravi","kiranmai","tanuja","hamida"]
for i in student_names:
    print("The student is",i)





student_names=["ajay","ravi","kiranmai","tanuja","hamida"] 
print("The student is",student_names[1]+" "+"10thclass") 
print("The student is",student_names[2]+" "+"10thclass")
print("The student is",student_names[3]+" "+"10thclass")
print("The student is",student_names[4]+" "+"10thclass")





def final_order_amount(predict_score,ipl_score,order_amount):
    if predict_score<ipl_score:
        discount=order_amount*.10
        final_amount=(order_amount-discount)
    elif predict_score==ipl_score:
        discount=order_amount*.50
        final_amount=(order_amount-discount)
    elif predict_score>ipl_score:
        discount=order_amount*.20
        final_amount=(order_amount-discount)
    return final_amount
final_order_amount(250,241,1000)
final_order_amount(250,250,1000)



def credit_limit(account_opening_amount,investment_amount):
    if account_opening_amount <100000:
        credit_limit=investment_amount*.50
    elif account_opening_amount>=100000 and account_opening_amount <500000:
        credit_limit=investment_amount*.80
    elif account_opening_amount>=500000 and account_opening_amount <=1000000:
        credit_limit=investment_amount*1.0
    elif account_opening_amount>1000000:
        credit_limit=investment_amount*5.0
    return credit_limit
credit_limit(200000,500000)



        
