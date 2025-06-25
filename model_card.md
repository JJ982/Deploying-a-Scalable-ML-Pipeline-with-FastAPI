# Model Card

## Model Details
Julie Blevins created this model for project 2 of the WGU/D501: ML DevOps Udacity course titled 'Deploying a Machine Learning Model with FastAPI'. It utilizes Random Forest Classifier, an ensemble learning method that is part of scikit-learn 1.5.1. 

## Intended Use
The model analyzed Census Bureau data to try and learn how to predict the likelihood of an individual's annual income being greater than $50,000. Primary intended uses include exploring correlations between people making > $50K a year and other demographic data such as age, education level, race, gender, and occupation. Intended users could be social scientists and public policy makers.

## Training Data
The dataset presents a classification problem, which is why the Random Forest Classifier was chosen. It trains the model to make predictions based on training and test data sets.

## Evaluation Data
The dataset was collected by the Census Bureau and downloaded from the UCI Machine Learning Repository in a csv format: https://archive.ics.uci.edu/dataset/20/census+income. It contained 32,563 records and the following column names: age, workclass, fnlgt, education, education-num, matial-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, salary.

## Metrics
Precision, recall, and F1 scores were the model performance metrics used to analyze how well predictions were made on slices of categorical features. F1 scores ranged from 0.0000 to 1.000, meaning that the model performed inconsistently across slices. This may be due to limited data for a particular slice, or perhaps some form of bias is influencing the model's performance.

## Ethical Considerations
There is potential exclusion bias in the dataset, compiled in 1994. At that time listed races included 'Amer-Indian-Eskimo', 'Asian-Pac_islander', 'Black', 'Other', and 'White'. Researchers wanting to analyze trends focusing on Hispanics/Latinos, a major group residing in the U.S., will not find this model of value as is, since those indivduals will reside in the 'Other' category.

## Caveats and Recommendations
By 2030, the Census Bureau will add 'Middle Eastern / North African' and 'Hispanic / Latino' to the race category (https://www.census.gov/about/our-research/race-ethnicity/standards-updates.html). If this model is still in use, it will need to be retrained to account for the new options.