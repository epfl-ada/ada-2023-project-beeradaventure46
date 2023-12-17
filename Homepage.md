# Introduction


# How is Beer served ?


## Naive approach


### Results


## Similarity approach


### Results


## Rule-based approach



### Results


## Tense-based approach
•	Analyze the ‘can’ to diffirentiate the verbe and the noun (I labeled the can that were nouns)
•	Analyze the verbs before each serving type 
•	If the verb before the serving type is a modal word --> don’t keep

For the verbs that precede the serving type are in the past and present: 
•	Case 1: more then one verb in the past --> keep the first 
•	Case 2: one (or more) verb in the past and one (or more) in the present --> keep the first verb in the past. 

For the verbs that precede the serving type only in the present: 
•	Case 1: more then one serving type in the list --> unknown 
•	Case 2: only one serving type in the list --> keep the unique serving type 


### Results
•	Less unknowns
•	94% accuracy on the evaluation set 
•	longer to run then rule based took the unknown from the rule base (had 59% on the hole data set) and apply tense base to reduce the number of unknown (reduced to 55%)
•	and decrease in 4 % is around 100 000 reviews more for our analysis 


# Could filtering help ?


# How about the emotions beer evokes ?


# Readability score and metrics update


# Which countries are the most beer-friendly ?


# Which beers are the most user-friendly ?
- Grouping all beer styles into broader categories (Ales, Stouts, Lagers, Strong Ales, Wheat Beers, Specialty and Unique Beers, Seasonal and Celebration Beers, Sour Beers, and Historical and Traditional Beers).
- Counting the number of beers in each category. This was done to address the imbalance in category sizes (e.g., there are 30 ales in our dataset but only 8 stouts).
- Counting the number of reviews per category.
- Calculating the average number of reviews per category (number of reviews divided by the number of beers in the given category). This analysis was conducted to further understand the imbalance in category sizes.
- Counting the number of reviewers per category.
- Calculating the average number of reviewers per category (number of reviews divided by the number of beers in the given category). This was also performed to address the imbalance in category sizes.
- Counting the number of reviews from each region for every category separately. The purpose of this step was to determine which countries consume or review specific types of beers the most. At this stage, it is not possible to ascertain preferences for specific beers in different regions but rather to identify which ones are consumed or reviewed more frequently.


# Statistical analysis


# Conclusion



