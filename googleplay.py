import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import csv 
import pandas as pd

# Initial dataframe of entire file
init_playstore = pd.read_csv("googleplaystore.csv")
#print(init_playstore.dtypes)

# De-duped the file
one_app = init_playstore.drop_duplicates()

# Aggregate all attributes and group by "App"
aggregations = {
    'Category': lambda x: x.value_counts().index[0] 
    ,'Rating': 'max'
    ,'Reviews':'max'
    ,'Size': lambda x: x.value_counts().index[0]
    ,'Installs':'max'
    ,'Type': 'min'
    ,'Price': 'max'
    ,'Content Rating': 'min'  
    ,'Genres': lambda x: x.value_counts().index[0]
    ,'Last Updated': 'max'
    ,'Current Ver': 'max'
    ,'Android Ver': 'max' 
}

one_app_agg = one_app.groupby(['App']).agg(aggregations)

# app_count = one_app_agg.groupby('App').agg('count')
# app_count.to_csv("agg_count.csv")

# remove invalid ratings
playstore = one_app_agg[(one_app_agg["Rating"].notna())]
playstore.to_csv("playstore_distinct.csv")

# add new gross revenue column
# revenue = installs * price
playstore['Price']= playstore['Price'].str.replace('$', '')
playstore['Price'] = pd.to_numeric(playstore['Price'], errors='coerce')

playstore['Installs']= playstore['Installs'].str.replace('+', '')
playstore['Installs']= playstore['Installs'].str.replace(',', '')
playstore['Installs'] = pd.to_numeric(playstore['Installs'], errors='coerce')

revenue = playstore.Installs * playstore.Price
#print(revenue)

playstore['Gross Revenue'] = revenue.where(playstore.Type == 'Paid', other=-revenue)
#print(playstore)
playstore.to_csv("playstore.csv")

# Show top 3 grosssing
#new = old[['A', 'C', 'D']].copy()
#top3 = playstore[['App', 'Category','Gross Revenue']]
top3 = playstore.filter(['App', 'Category','Gross Revenue'], axis=1)
top3apps = top3.groupby('Category')['Gross Revenue'].nlargest(3)
top3apps.to_csv("top3apps.csv")

