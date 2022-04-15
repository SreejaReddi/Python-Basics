emp_details={'employee':{'sreeja':{'id':'574','salary':'2000','designation':'manager'},
                        'anusha':{'id':'579','salary':'1000','designation':'associate'}}}
print(emp_details)
#converting dictionary into dataframe
import pandas as pd
df=pd.DataFrame(emp_details['employee'])
print(df)