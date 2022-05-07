import pandas as pd

# read data from people output
facts = pd.read_csv('people.csv')

# convert datetime to date only
facts['aquisition_date'] = pd.to_datetime(facts['created_dt']).dt.date

# group on aquisition date
aquisition_facts = facts.groupby('aquisition_date').size().reset_index(name='aquisitions')

# export as csv
aquisition_facts.to_csv('aquisition_facts.csv',index=False)