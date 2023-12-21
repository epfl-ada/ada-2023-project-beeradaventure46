---
layout: home
title: Bottles, Cans, or Drafts
subtitle: Pouring Over the Data to Decode the Perfect Sip
---

# Abstract

In this dive into the beer world, our project seeks to figure out the subtle differences that various ways of serving—bottle, can, and draft—bring to beer reviews. We're curious about what makes people like one style over another. Why does it matter, you ask? Because beer enthusiasts, much like you and me, take their choices seriously. And we want to know if the container affects how they rate and describe the brew. By closely looking at a dataset of beer reviews, we want to spot any connections or trends that show how serving styles might sway the overall rating and what people say about the beer. As we take on this bubbly quest, we hope to quench the thirst for understanding how picking between a bottle, can, or draft might shape how beer lovers feel.

## The Curiosity Spark

Picture this: A cozy pub, friends gathered, and the bartender presenting three options – a bottled beauty, a canned contender, and a freshly poured draft. Each sip tells a story, and we're here to decode it. What makes a person lean towards one style over another? Is it the tactile satisfaction of popping a cap, the convenience of a can, or the experience of a perfectly pulled pint?

Our journey is fueled by burning questions:

1. Does a specific serving style consistently earn higher or lower ratings than its counterparts?
2. Are certain beer types more closely linked to a particular serving style?
3. Do regional preferences influence the choice of serving style in different corners of the globe or across the United States?


## Unveiling the Data
<b> Beer Styles and Reviews </b>

To start, let's take a look at the distribution of beer styles and the number of reviews each beer has received.

![10 most common beer styles](/assets/img/beer_styles.png)
![Number of reviews per beer](/assets/img/reviews_per_beer.png)

The first image unveils the top 10 most common beer styles, providing insights into the variety within our dataset. The second image presents a histogram, showcasing the distribution of reviews per beer in a logarithmic scale.

<b> Breweries and Locations </b>

Moving on, let's explore the brewery landscape and the most prevalent brewery locations.

![Number of beers per brewery](/assets/img/beers_per_brewery.png)
![10 most common brewery locations](/assets/img/brewery_locations.png)

Here, we delve into the brewery landscape, examining the distribution of beers per brewery and the top 10 locations where breweries thrive.

<b> User Reviews and Locations </b>

Our exploration wouldn't be complete without understanding the users behind the reviews. Let's unravel the story of reviews per user and the most common user locations.

![Number of reviews per user](/assets/img/reviews_per_user.png)
![10 most common user locations](/assets/img/user_locations.png)

In these images, we unveil the distribution of reviews per user and uncover the top 10 locations where our users hail from. Let the exploration continue!


<b> Separation of Beer Types into More General Groups </b>

These groupings provide us with a more generalized view of beer styles, setting the stage for uncovering hidden patterns within each category. Let's proceed with our intriguing exploration!

[![Beer Types Sunburst](/assets/plots/sunburst.png)](/assets/plots/sunburst.html)

But wait, we've got a missing ingredient – the serving style!

## Part 2: Serving Style Extraction

In our exploration of 250 hand-checked beer reviews, we set out to uncover the mysteries of serving types. We kicked things off with the simple Naïve method, choosing a serving type when the answer was obvious. However, as the reviews got more complex, we tried the fancier Similarity method, using calculations to compare review text with potential serving types.

Despite our efforts to enhance accuracy, the straightforward Naïve method proved to be more effective overall. The accuracy decreased, and the number of reviews categorized as unknown increased. Subsequently, we decided not to pursue the Similarity method further and continued refining the Naïve method. We acknowledged its limitations, especially when dealing with ambiguous statements like the one found in some reviews: "I actually found this more elegant and less bruising than expected. Stone can still surprise," where the word "can" functioned as a verb, not a serving type, but our algorithm mistakenly considered it one.

To address such challenges, we introduced a Rule-based method. This involved differentiating between the verb 'can' and the noun 'can' in the reviews and excluding serving types if certain verbs ("would," "could," "'d," "will") were present. For instance, in sentences like "and I will certainly be keeping an eye out for a bottle," the serving type 'bottle' wouldn't be considered because the user had not yet consumed from a bottle. Despite these efforts, challenges persisted, leading us to refine our approach further with a Tense-based method.

In the Tense-based method, we focused solely on the unknown reviews identified in the Rule-based analysis. The method involved analyzing the different tenses of the verbs before the serving type. When a verb in the past was found, the serving type was taken. However, if the verbs were all in the present, the serving was concidered unknown.

All these methods were applied by examining the 250 hand reviews and were modified to maximize accuracy. The journey from the simple Naïve method to the more refined Tense-based method underscores the complexities involved in recognizing serving types in reviews.reviews.


This journey from the simple Naïve method to the refined Tense-based method shows the complexities of recognizing serving types in reviews. Cheers to the adventure! 🍻

### Naive Approach

#### Results

---

### Similarity Approach

#### Results

---

### Rule-Based Approach

#### Results

---

### Tense-Based Approach

- Analyzing 'can' to differentiate the verb and the noun (I labeled the cans that were nouns).
- Analyzing the verbs before each serving type.
- If the verb before the serving type is a modal word, don't keep it.
- For the verbs that precede the serving type in the past and present:
  - Case 1: More than one verb in the past, keep the first.
  - Case 2: One (or more) verb in the past and one (or more) in the present, keep the first verb in the past.
- For the verbs that precede the serving type only in the present:
  - Case 1: More than one serving type in the list, unknown.
  - Case 2: Only one serving type in the list, keep the unique serving type.

#### Results

- Fewer unknowns.
- Achieved 94% accuracy on the evaluation set.
- Took longer to run than the rule-based approach; took the unknowns from the rule base (had 59% on the whole dataset) and applied the tense base to reduce the number of unknowns (reduced to 55%).
- A decrease of 4% represents around 100,000 more reviews for our analysis.

---

### Could Filtering Help?

---

### How About the Emotions Beer Evokes?

---

### Readability Score and Metrics Update

---

### Which Countries Are the Most Beer-Friendly?

---

### Which Beers Are the Most User-Friendly?

- Grouping all beer styles into broader categories (Ales, Stouts, Lagers, Strong Ales, Wheat Beers, Specialty and Unique Beers, Seasonal and Celebration Beers, Sour Beers, and Historical and Traditional Beers).
- Counting the number of beers in each category. This was done to address the imbalance in category sizes (e.g., there are 30 ales in our dataset but only 8 stouts).
- Counting the number of reviews per category.
- Calculating the average number of reviews per category (number of reviews divided by the number of beers in the given category). This analysis was conducted to further understand the imbalance in category sizes.
- Counting the number of reviewers per category.
- Calculating the average number of reviewers per category (number of reviews divided by the number of beers in the given category). This was also performed to address the imbalance in category sizes.
- Counting the number of reviews from each region for every category separately. The purpose of this step was to determine which countries consume or review specific types of beers the most. At this stage, it is not possible to ascertain preferences for specific beers in different regions but rather to identify which ones are consumed or reviewed more frequently.

## Part 3: Statistical Analysis

...

## Part 4: Regional Analysis

...

## Part 5: Conclusion

...

