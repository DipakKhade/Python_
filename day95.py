# Regular Expressions in Python 

import re

# pattern="correlation"
text='''Canonical correlation analysis is a method for exploring the relationships between two multivariate sets of variables (vectors), all measured on the same individual.
Consider, as an example, variables related to exercise and health. On one hand, you have variables associated with exercise, observations such as the climbing rate on a stair stepper, how fast you can run a certain distance, the amount of weight lifted on bench press, the number of push-ups per minute, etc. On the other hand, you have variables that attempt to measure overall health, such as blood pressure, cholesterol levels, glucose levels, body mass index, etc.  Two types of variables are measured and the relationships between the exercise variables and the health variables are of interest.
As a second example consider variables measured on environmental health and environmental toxins. A number of environmental health variables such as frequencies of sensitive species, species diversity, total biomass, productivity of the environment, etc. may be measured and a second set of variables on environmental toxins are measured, such as the concentrations of heavy metals, pesticides, dioxin, etc.
For a third example consider a group of sales representatives, on whom we have recorded several sales performance variables along with several measures of intellectual and creative aptitude. We may wish to explore the relationships between the sales performance variables and the aptitude variables.
One approach to studying relationships between the two sets of variables is to use canonical correlation analysis which describes the relationship between the first set of variables and the second set of variables. We do not necessarily think of one set of variables as independent and the other as dependent, though that may potentially be another approach.
Canonical Variates
'''

# match=re.search(pattern,text)
# print(match)


    

pattern=r'[A-Z]+anonical'
# match=re.search(pattern,text)
# print(match)




match=re.finditer(pattern,text)
print(match)

for match in match:
    print(match.span())




