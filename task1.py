# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:53:53 2022

@author: sys
"""

import pandas as pd
df_Demogrph=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Demograph_Details")
df_Demogrph
df_finance=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Financial_Details")
df_finance
df_transaction=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Transactions_Details")
df_transaction
df_count=pd.pivot_table(df_transaction,values='Transaction_amount',index='Customer_ID',aggfunc='count')
df_count
df_Demogrph_cl_f1=df_Demogrph[['Customer_ID','Customer_Name']]
df_Demogrph_cl_f1
df_finance_cl_f2=df_finance[['Customer_ID','Income']]
df_finance_cl_f2
df_transaction_cl_f3=df_transaction[['Customer_ID','Transaction_amount']]
df_transaction_cl_f3
df1=df_Demogrph_cl_f1.merge(df_finance_cl_f2,how='inner',on='Customer_ID')
df1
df2=df1.merge(df_count,how='inner',on='Customer_ID')
df2
df_offer=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="offer_Details")
df_offer
df_offer_cl_f1=df_offer[['Type_of_loan_Description','Type_of_Loan']]
df_cc=df2[((df2['Income']>=10000) & (df2['Income']<30000) & (df2.Transaction_amount>2))]
df_cc
df_pl=df2[((df2['Income']>=30000) & (df2['Income']<50000) & (df2.Transaction_amount>1))]
df_pl
df_LL=df2[((df2['Income']>=50000) & (df2['Income']<60000) & (df2['Transaction_amount']>1))]
df_LL
df_HL=df2[((df2['Income']>60000) &  (df2['Transaction_amount']>2))]
df_HL
df_final=pd.concat([df_cc,df_pl,df_LL,df_HL],axis=0,ignore_index=True)
df_final
df_final_cl_f1=df_final[['Customer_ID','Customer_Name']]
df_final_cl_f1
df_output=pd.concat([df_final_cl_f1,df_offer_cl_f1],axix=1)
df_output
