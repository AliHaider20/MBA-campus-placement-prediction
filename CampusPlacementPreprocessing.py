import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


""" Data Description
Gender- Male='M',Female='F'
Secondary Education percentage- 10th Grade
Board of Education ssc-b - Central/ Others
Higher Secondary Education percentage- 12th Grade
Board of Education hsc-b - Central/ Others
Specialization in Higher Secondary Education
Degree Percentage
Under Graduation(Degree type)- Field of degree education
Work Experience Yes,No
Under Graduation(Degree type)- Field of degree education
Work Experience
Employability test percentage ( conducted by college)
Post Graduation(MBA)- Specialization
MBA percentage(mba_p)
Status of placement- Placed/Not placed
salary
"""


# # Questions:

# Which factor influenced a candidate in getting placed?
# Does percentage matters for one to get placed?
# Which degree specialization is much demanded by corporate?
# Play with the data conducting all statistical tests.

df = pd.read_csv('Placement_Data_Full_Class.csv')
df.shape
df.drop(['sl_no'],axis=1,inplace=True)
df.status.replace(['Placed','Not Placed'],[1,0],inplace=True)

""" Replacing the values of Male gender to 1 and Female gender to 0.
   Replacing the values of workEx with 1 and NoWorkEx to 0.
"""
df.gender.replace(['M','F'],[1,0],inplace=True)
df.workex.replace(['Yes','No'],[1,0],inplace=True)
df.head()

plt.figure(figsize=(9,7))
sns.heatmap(df.corr(),annot=True,cmap='YlGnBu')


# # The above correlation map tells us that the job offered highly depends upon
# # SSC Percentage

# # Most of the jobs offered after MBA are of Specialization Mkt & Fin
pd.crosstab(df.specialisation,df.status)
df.describe()

"""
Above description tells us the following.
1) Salary column contains outliers.
2) Salary column contains null values.
3) Avg Salary is 288655
4) Only 25% of students got salary above 300000
5) Max Salary is 940000 and it's male.
6) Gender column contains Male-65% and Female-35%
7) Highest percentage marks in MBA and etest_p  is received by a female candidate.
"""

# Creating a cleaned csv file with columns which has impact on status column.
df[['ssc_p','hsc_p','degree_p','mba_p','workex','etest_p','status']].to_csv('cleaned_placement.csv',index=False)
print('Precessed csv created Successfully')
