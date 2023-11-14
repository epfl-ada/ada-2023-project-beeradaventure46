# Bottles, Cans, or Drafts: Pouring Over the Data to Decode the Perfect Sip

## Abstract
In this dive into the beer world, our project seeks to figure out the subtle differences that various ways of serving—bottle, can, and draft—bring to beer reviews. We're curious about what makes people like one style over another. Why? Because beer fans are all about their personal choices, and we want to know if the container affects how they rate and describe the brew.  
By closely looking at a dataset of beer reviews, we want to spot any connections or trends that show how serving styles might sway the overall rating and what people say about the beer. As we take on this bubbly quest, we hope to quench the thirst for understanding how picking between a bottle, can, or draft might shape how beer lovers feel. 

## Research questions
In this analysis, we would like to answer the following questions:
* Does a particular serving type consistently receive higher or lower ratings compared to others?
  
* Are certain types of beers more frequently associated with a specific serving style?
  
* Do regional preferences influence the choice of a specific serving style in different parts of the world or the US?

## Methods
In order to find answers to these questions, we will use the following data analysis pipeline.

### Part 1: Getting to Know the Data

*Step 1: Preparing the Data*  
Some datasets were initially provided as txt files. We created a function to read these files line by line, converting their content into dictionaries. These dictionaries were then saved as CSV files for simplified access.

*Step 2: Exploring Each Dataset*  
We carefully examined the contents of each dataset, streamlining them by removing unnecessary columns and ensuring any missing values were appropriately filled.

*Step 3: Building the Master Dataset*  
To facilitate seamless analysis, we merged all the datasets into one comprehensive dataset. This amalgamated dataset was also saved as a CSV file, ensuring efficiency in subsequent stages of our work.

### Part 2: Data Enrichment

*Step 4: Serving Type Classification*  
We initiated the serving type classification by creating a sample of 250 reviews. This sample underwent manual classification to assess the accuracy of various classifying algorithms, aiding us in determining the most suitable approach. Subsequently, we applied the chosen algorithm to the entire dataset. Our approach first consists in applying a rule-based function to the tokenized reviews, according to grammar and syntax rules. Here there will be a trade-off between the accuracy of the function and the run time that can be consequent when adding extra rules. 

Pseudo-code :
<hr style="clear:both">

**Input :**  Textual review
<hr style="clear:both">

$bottle \gets (\text{'bottle'}, \text{bottled'}, \text{'bottles'}, \text{'bomber'})$\
$can \gets (\text{'can'}, \text{'canned'}, \text{'cans'})$\
$draft \gets (\text{'draft'}, \text{'tap'}, \text{draught'}, \text{'taps'}, \text{'cask'}, \text{'growler'})$

$tokens \gets \text{nlp}(review)$\
$servings  \gets \text{empty set}$\
$serving \gets \text{None}$

$\text{for} \; token \; \text{in} \; tokens :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\text{if} \; token \; \text{in} \; bottle :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $servings \gets \text{'bottle'}$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\text{if} \; token \; \text{in} \; can :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $servings \gets \text{'can'}$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\text{if} \; token \; \text{in} \; draft :$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $servings \gets \text{'draft'}$

$\text{if} \; \text{length}(servings) \neq 1:$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $serving \gets \text{'unknown'}$\
$\text{else}:$\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $serving \gets \text{string}(servings)$
<hr style="clear:both">

**Output :** serving style
<hr style="clear:both">

*Step 5: Additional Review Metrics*  
In this step, we computed additional metrics for each review, including readability score, polarity, and subjectivity.

### Part 3: Analysis and answering the scientific questions *(TBD in Milestone 3)*

*Step 6: ---* 

*Step 7: ---* 

*Step 8: Create datastory* 

## Proposed timeline

**17.11.2023** : Step 1 to 5

**01.12.2023** : Homework 2

**08.12.2023** : 

**15.12.2023** : 

**20.12.2023** : Step 8

**22.12.2023** : Deadline Milestone 3

## Organization within the team
Anne-Valérie :  
Agatha :  
Thamin :  
Tristan :  
Victor :  
