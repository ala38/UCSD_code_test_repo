import pandas as pd

t2_ec_df = pd.read_csv('t2_ec 20190619.csv')
t2_registry_df = pd.read_csv('t2_registry 20190619.csv')
joined_df = t2_registry_df.merge(t2_ec_df, how='left', left_on = ['RID', 'VISCODE'], right_on = ['RID', 'VISCODE'])
filter1 = joined_df['VISCODE'] == 'w02'
filter2 = joined_df['SVDOSE'] == 'Y'
filter3 = joined_df['ECSDSTXT'] != 280
filtered_df = joined_df[filter1 & filter2 & filter3]
final_df = filtered_df[['ID_x', 'RID', 'USERID_x', 'VISCODE', 'SVDOSE', 'ECSDSTXT']]
final_df.to_csv('results.csv', header=False)
