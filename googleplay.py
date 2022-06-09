import csv
import pandas as pd

# Initial dataframe of entire file
playstore = pd.read_csv("googleplaystore.csv")

# De-duped the file
one_app = playstore.drop_duplicates()

#test 8 Ball Pool
eightball = one_app[one_app["App"] == "8 Ball Pool"]
aggregations = {
    'Reviews':'max',
    'Category': lambda x: x.value_counts().index[0]
    
}
#eightball1 = eightball.groupby(['App','Rating','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver','Android Ver']).agg(aggregations)
#print(eightball1)
#eightball1 = eightball.groupby(['App','Rating','Size','Installs','Type','Price','Content Rating','Reviews','Genres','Last Updated','Current Ver','Android Ver'])
#'Category'].apply(lambda x: x.value_counts().index[0]).reset_index()
one_app_agg = one_app.groupby(['App','Rating','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver','Android Ver']).agg(aggregations)
print(one_app_agg)
app_count = one_app_agg.groupby('App').agg('count')
print(app_count)
app_count.to_csv("agg_count.csv")
one_app_agg.to_csv("one_app_agg.csv")


'''
# Aggregate out duplicate app names by frequency of Category and Largest number of Ratings
aggregation_functions = {'Reviews': 'max'}
one_app = one_app.groupby(one_app['App']).agg(aggregation_functions)
print(one_app)
one_app.to_csv("dedupe.csv")

remove_invalid_rating = one_app[(one_app["Rating"].notna())]
print(remove_invalid_rating)xs
print(one_app)
one_app.to_csv("dedupe.csv")

'''
#8 Ball Pool






#filtered = filter(lambda p: 'Category' == "ART_AND_DESIGN", reader) 
#csv.writer(open(r"playstore_filtered.csv",'w'),delimiter=',').writerows(filtered)
