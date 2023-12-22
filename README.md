# Bottles, Cans, or Drafts: Pouring Over the Data to Decode the Perfect Sip ([Website](https://anne-valerie.github.io/))

## Abstract
In this dive into the beer world, our project seeks to figure out the subtle differences that various ways of serving—bottle, can, and draft—bring to beer reviews. We're curious about what makes people like one style over another. Why? Because beer fans are all about their personal choices, and we want to know if the container affects how they rate and describe the brew.  
By closely looking at a dataset of beer reviews, we want to spot any connections or trends that show how serving styles might sway the overall rating and what people say about the beer. As we take on this bubbly quest, we hope to quench the thirst for understanding how picking between a bottle, can, or draft might shape how beer lovers feel. 

## Research questions
In this analysis, we would like to answer the following questions:
* Does a particular serving type consistently receive higher or lower ratings compared to others?
  
* Are certain types of beers more frequently associated with a specific serving style?
  
* Do regional preferences influence the choice of a specific serving style 

## Methods
In order to find answers to these questions, we will use the following data analysis pipeline.

### Part 1: Getting to Know the Data

*Step 1: Preparing the Data*  
Some datasets were initially provided as txt files. We created a function to read these files line by line, converting their content into dictionaries. These dictionaries were then saved as .parquet files for simplified access.

*Step 2: Exploring Each Dataset*  
We carefully examined the contents of each dataset, streamlining them by removing unnecessary columns and ensuring any missing values were appropriately filled.

*Step 3: Building the Master Dataset*  
To facilitate seamless analysis, we merged all the datasets into one comprehensive dataset. This augmented dataset was also saved as a .parquet file, ensuring efficiency in subsequent stages of our work.

### Part 2: Data Enrichment

*Step 4: Serving Type Classification*  

We initiated the serving-type classification by creating a sample of 250 reviews. This sample underwent manual classification to assess the accuracy of various classifying algorithms, helping us determine the most suitable approach. Subsequently, we applied the chosen algorithm to the entire dataset.

Our approach first involves applying a rule-based function to the tokenized reviews, based on grammar and syntax rules. Unknown reviews were then analyzed using the tense-based method, which retains serving types that were in the past. Here, there is a trade-off between the accuracy of the function and the runtime, which can be significant when adding extra rules.

This is the function:
<hr style="clear:both">

**Input :**  Textual review
<hr style="clear:both">

$bottle \gets (\text{'bottle'}, \text{bottled'}, \text{'bottles'}, \text{'bomber'})$\
$can \gets (\text{'can'}, \text{'canned'}, \text{'cans'})$\
$draft \gets (\text{'draft'}, \text{'tap'}, \text{draught'}, \text{'taps'}, \text{'cask'}, \text{'growler'})$

$tokens \gets \text{nlp}(review)$\
$servings  \gets \text{empty set}$\
$serving \gets$ None

for $token$ in $tokens :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if $token$ in $bottle :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $servings \gets \text{'bottle'}$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if $token$ in $can :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $servings \gets \text{'can'}$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if $token$ in $draft :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $servings \gets \text{'draft'}$

if $\text{length}(servings) \neq 1:$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $serving \gets \text{'unknown'}$\
$\text{else}:$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $serving \gets \text{string}(servings)$
<hr style="clear:both">

**Output :** serving style
<hr style="clear:both">

*Step 5: Additional Review Metrics*  
In this step, we calculated the polarity, mean, and standard deviation for each review, which were subsequently utilized for statistical analysis.

### Part 3: Verifying the Dataset Representation

*Step 6: Verifying the Dataset Representation* :
Given that the dataset employed for analyses only uses reviews where a serving style has been specified, there is a substantial reduction in dataset size. (With the  approximately 56% of the original dataset has an unknown serving style.) It is imperative, therefore, to ensure that the utilized dataset remains representative of the initial dataset.
. 
### Part 4: Visualization 
*Step 7:  Temporal analysis* : 
We analyzed the number of reviews for each year and found that the website has grown in popularity throughout the years, reaching a peak in 2011. Since then, the number of reviews has been decreasing.

*Step 8:  geographical analysis*  :
We calculated the number of reviews per world region to determine the location of the reviewers, and we found that the majority were from North America or Europe.

*Step 9:  Beer style analysis* :
We separated the beers into nine groups and analyzed the distribution of serving styles among these groups. In each group, the predominant serving style was found to be the bottle. The same analysis was performed for different regions of the world, and once again, the bottle emerged as the popular choice for serving.

### Part 5: Statistical analysis 

*Step 10: Rating aspect* :
To comprehend all aspects of the ratings, we conducted linear regression on each aspect. It appears that taste has the most significant impact on the rating, while appearance has the least impact.

*Step 11: The influence of serving type* :
We analyzed the distribution of grades for each serving type and identified variations in ratings based on the serving type. As anticipated, there is a general preference for draft beers, indicating distinct consumer preferences.

Through t-tests, we observed that all p-values were below 0.05, indicating a statistically significant difference in scores. However, due to a higher number of bottle reviews compared to draft or cans, we employed a Kruskal-Wallis test. Even with this test, the p-values remained below 0.05, suggesting that serving style does not have a significant impact on the ratings.

*Step 12: Influence of serving type on the beer groups* :
We performed a chi-square test and a t-test that showed that the serving type is dependent on the beer group.

*Step 13: Influence of beer groups on the rating* :
Since the ratings were not dependent on the serving type, we sought other potential confounders. Through a one-way ANOVA test for each beer group, we concluded that the means of ratings are not equal across all beer styles.

Using an ordinary least square regression model, we analyzed the differences between ratings for each serving style. In most cases within each group, draft beers tended to have higher ratings compared to other serving types, with the exception being sour beers.


### Part 6: Conclusion

After conducting numerous analyses, it became apparent that the variations in ratings were not attributed to the serving style; rather, they could be attributed to personal preferences.


### Organization within team

<table class="tg" style="table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 16px">
<col style="width: 180px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax">Teammate</th>
    <th class="tg-0lax">Contributions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Anne-Valérie </td>
    <td class="tg-0lax"> (1)  <br> (2) <br> (3) <br> (4) <br> (5) </td>
  </tr>
  <tr>
    <td class="tg-0lax">Agatha </td>
    <td class="tg-0lax"> (1) <br> (2) <br> (3) <br> (4) </td>
  </tr>
  <tr>
    <td class="tg-0lax">Thamin</td>
    <td class="tg-0lax"> (1) <br> (2) <br> (3) <br> (4) </td>
  </tr>
  <tr>
    <td class="tg-0lax">Tristan</td>
    <td class="tg-0lax"> (1) <br> (2)  <br> (3) <br> (4) </td>
  </tr>
  <tr>
    <td class="tg-0lax">Victor</td>
    <td class="tg-0lax"> (1) <br> (2) <br> (3)  <br> (4) </td>
  </tr>
</tbody>
</table>