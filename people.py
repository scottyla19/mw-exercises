import pandas as pd

# extract data from various files
cons = pd.read_csv('https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv')
emails = pd.read_csv('https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv')
chSubs = pd.read_csv('https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv')

# filter on chapter_id = 1 and primary emails only
chSubs = chSubs[chSubs['chapter_id'] == 1]
emails = emails[emails['is_primary'] == 1]

# merge chapter subscriptions, emails, and constituent information on relevent keys
people = pd.merge(chSubs, emails[['cons_email_id','cons_id', 'email']], how='inner', on='cons_email_id', suffixes=('_subs', '_emails'))
people = pd.merge(people, cons[['cons_id','source','create_dt','modified_dt']], how='inner', on='cons_id', suffixes=('_people', '_cons'))

# drop unneccessary columns and rename
people_final = people[['email', 'source', 'isunsub','create_dt','modified_dt_cons']]
people_final = people_final.rename(columns={'source':'code','isunsub':'is_unsub','create_dt':'created_dt','modified_dt_cons':'updated_dt'})

# export as a csv
people_final.to_csv('people.csv', index=False)