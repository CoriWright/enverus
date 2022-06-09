import csv
import pandas as pd


playstore = pd.read_csv("googleplaystore.csv")
one_app = playstore.drop_duplicates()
remove_invalid_rating = one_app[(one_app["Rating"].notna())]
print(remove_invalid_rating)
print(one_app)
one_app.to_csv("dedupe.csv")


#8 Ball Pool






#filtered = filter(lambda p: 'Category' == "ART_AND_DESIGN", reader) 
#csv.writer(open(r"playstore_filtered.csv",'w'),delimiter=',').writerows(filtered)
