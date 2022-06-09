# Readme
# Enverus
Enverus Take Home

## Code Walkthrough
I used python and the pandas library to complete the work.  I have commented the python file to explain each step.  The final dataset is named “final_playstore_ratings.csv” .  I have also kept files created along the way for reasoning purposes.

### Question 1

> Filter the dataset to have 
>     1. one entry per App name 
>     2. remove apps with invalid ratings

1. I de-duped the dataset and put it into the “one_app” data frame.
2. I noticed that apps like “8 Ball Pool” still had 7 entries because each record had a unique number of ratings, and one had a different category than the rest
	1. **Assumption** Since the number of ratings were so similar, I  assumed that the record was pulled multiple times at different times.
	2. To solve this, I created one record that had the highest frequency of category and the max amount of ratings .
3. I took the last dataset and removed the invalid ratings by removing null values.  This field has a datatype of float64 so if it were not a number, the record would be invalid.

### Question 2
> Add a new gross revenue feature for each app 


### Question 3
> Return the top 3 grossing apps in each category
