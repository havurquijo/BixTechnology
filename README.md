[![Static Badge](https://img.shields.io/badge/BixTechnolog%20Challange-050A66?style=flat&logo=googledocs)](https://docs.google.com/document/d/1UXFxrIPrkJ8SiLIvvKET0z6PdcJNd1kqgj0io7_lYAM/edit)

[![Static Badge](https://img.shields.io/badge/Deployed%20Machine-2D2828?style=flat&logo=amazonec2)](http://bix-challange-deployed.alcantara-urquijo.com.br/)

[![Static Badge](https://img.shields.io/badge/linkedin-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/hvurquijo/)



# Introduction


## Challange Activities
1. [What steps would you take to solve this problem?.](#activity-1)
2. [Which technical data science metric would you use to solve this challenge?](#activity-2)
3. [Which business metric  would you use to solve the challenge?](#activity-3)
4. [How do technical metrics relate to the business metrics?](#activity-4)
5. [What types of analyzes would you like to perform on the customer database?](#activity-5)
6. [What techniques would you use to reduce the dimensionality of the problem?](#activity-6)
7. [What techniques would you use to select variables for your predictive model?](#activity-7)
8. [What predictive models would you use or test for this problem? Please indicate at least 3.](#activity-8)
9. [How would you rate which of the trained models is the best?](#activity-9)
10. [How would you explain the result of your model? Is it possible to know which variables are most important?](#activity-10)
11. [How would you assess the financial impact of the proposed model?](#activity-11)
12. [What techniques would you use to perform the hyperparameter optimization of the chosen model?](#activity-12)
13. [What risks or precautions would you present to the customer before putting this model into production?](#activity-13)
14. [If your predictive model is approved, how would you put it into production?](#activity-14)
15. [If the model is in production, how would you monitor it?](#activity-15)
16. [If the model is in production, how would you know when to retrain it?](#activity-16)

## Activity 1
What steps would you take to solve this problem?.
To solve this problem we'll need to follow the next steps:

### Enviroment set-up
First, we need to set up the environment. For example, we can use [Visual Studio Code](https://code.visualstudio.com/) and install some extensions to improve performance, such as Python and Jupyter Notebook. Then, we create a virtual environment on Windows:

```powershell
py -m venv .venv
```
With the enviroment created, we activate it by running:
```powershell
.\.venv\Script\activate
```
You should see something like `(.venv) PS C:\Users...`.  After that, we can install all the required packages with specific versions, ensuring there are no conflicts.

### Data Cleaning
As previously mentioned, the data had issues with missing values, which we needed to filter out. In the database, missing values were represented as the string "na". We converted these to Python's `NaN` value using the `.replace()` method of the DataFrame object.

Another concern was columns containing a large number of zeros. While zeros are valid data, an abundance of them (or any constant value) doesn't provide useful information. Therefore, we converted the zeros and removed columns that were mostly zeros or `NaN` values. This process reduced the number of columns from 171 to 108. For this purpose, we created a function named `isRemovable()` to check if a column predominantly contains bad data.

At this point, we used `.dropna()` to eliminate all rows with `NaN` values, which left us with approximately one-third of the total rows.

### Dimensionality reduction
What has been done so far is already a dimensionality reduction, but it is necessary because bad data is worse than noise in machine learning. At this stage, we're going to remove columns that can be considered dispensable, based on a condition we will analyze shortly.

To reduce the number of columns, we need to identify the most important ones for our problem. We can look for two types of issues:

- Information repetition: When a pair of columns have high correlation, it means they are influenced by similar variables. Having both does not improve our model and can even make it worse.
- Low variance variables: Low variance variables provide less information. A variable with an order of magnitude lower variance than others appears as noise or a constant value, similar to the zeros in the previous section.

Having a DataFrame object with the numerical columns, we can apply `.corr().abs()` to obtain a 108 by 108 matrix with all the correlations between columns quantified as positive numbers. Using a mask, we can identify columns with high correlation. In this model, we remove columns that have an absolute correlation value of `0.7` or higher.

After the process, we ended up with 41 independent columns, less than half of the original number.

To continue decreasing dimensionality, we can use two additional filters, and we use both. However, before applying the variance filter, we need to eliminate potential outliers. Since outliers have very low probability, we use a strategy to filter data below a certain quantile. We chose the 99.99% quantile, which proved sufficient. The images comparing before and after are saved in `Assets/figures/<column-name>`.

Starting in the previous section up to this point, all the programming is in the file `cleaning.ipynb`.

We can select columns using an object from the ensemble module: the `ExtraTreesClassifier()`. It extracts the most important features and lets us choose which ones to keep. Using this method, we selected 15 more significant columns.

The other method is the low variance filter, as previously explained. To choose a variance threshold, we used the 3rd quantile and kept all columns with variance greater than 75% of the others. This left us with only 11 features.

Finally we save all three files: the one with 41 features, the one with 15 and the one with 11. This last filtering is in a file named `exploratory.ipynb`.

### Understanding the problem
"With our current knowledge of the problem, we cannot predict why the trucks' air systems are breaking down. However, we can predict when a truck will need maintenance on this system based on the provided database. The client did not provide details on how expenses were calculated in previous years, but they did inform us how to calculate our model's expenses and its tendency over the previous years. We must also consider that the database only includes information about trucks that went to air system maintenance and whether a problem was found or not; it does not indicate the order in which trucks were sent for maintenance.

Based on this information, we can create a new class with two values `["send", "not send"]` for maintenance, which will correspond to the class given in the database, making the isomorphism `["pos", "neg"] -> ["send", "not send"]`. This means that if we can predict the class `["pos", "neg"]`, we can determine when it is time to send a truck for maintenance and when it is not necessary.

As the class to be predicted is binary we will certanly have a very useful confusion matrix.

Based on the informations given by the client each component of the the confusion matrix will have a cost:
- True negative ($$p_{--}$$) -> costs $0
- True positive ($$p_{++}$$) -> costs $25
- False positive ($$p_{-+}$$)-> costs $10
- False negative ($$p_{+-}$$)-> costs $500

So we need a machine learning model that minimize the function: $$f(p_{++},p_{-+},p_{+-}) = p_{++}\cdot25+p_{-+}\cdot10+p_{+-}\cdot500$$

### Testing some machine learning algorithms
We proposed several machine learning algorithms given that the class we're predicting is binary:
- Logistic Regression
- Naive Bayes
- Decision Tree Classifier
- Random Forest

The files containing the programming of these models are respectively:
- LogisticRegression.ipynb
- NaiveBayes.ipynb
- DecisionTreeClassifier.ipynb
- RandomForest.ipynb

We tested each algorithm with three datasets:
- The dataset with 41 features
- The dataset with 15 features
- The dataset with 11 features

In each case, we printed the confusion matrix and the value of  $$f(p_{++},p_{-+},p_{+-})$$, which represents the cost of maintenance for the selected data.

### Choosing a machine learning model
Firstly, we trained the machine learning model by dividing the data into training and test sets. We then selected the best-performing combination of model and dataset based on the lowest $$f(p_{++},p_{-+},p_{+-})$$ value. The Naive Bayes model with 11 features performed the best.

After that, we retrained the model using the entire filtered and cleaned data from previous years for each set of features. We then applied the model to the whole present year data after cleaning it as well.

Finally, we optimized the model using the `GridSearchCV` class from the `model_selection` module in the `sklearn` package. This performed cross-validation to minimize overfitting, and we obtained the same result as before, indicating a good result. For the Naive Bayes model, there are no parameters to tune, so the optimization ended at this point. However, we tuned parameters for the other algorithms, but none performed as well as Naive Bayes.

### Presenting the results


### Deploying the machine
We created a simple webpage using the Python Flask framework and the Bootstrap HTML framework. This allows the client to input the values of eleven features (still encrypted) and receive a prediction.

We deployed the machine learning algorithm in an AWS Elastic Compute Cloud (EC2) instance and served it through HTTP. Additionally, we included a section on the webpage for inputting new data to retrain the model, as well as a contact form for client feedback in case of issues.

## Activity 2
Which technical data science metric would you use to solve this challenge?

## Activity 3
Which business metric  would you use to solve the challenge?

## Activity 4
How do technical metrics relate to the business metrics?

## Activity 5
What types of analyzes would you like to perform on the customer database?

## Activity 6
What techniques would you use to reduce the dimensionality of the problem?

## Activity 7
What techniques would you use to select variables for your predictive model?

## Activity 8
What predictive models would you use or test for this problem? Please indicate at least 3.

## Activity 9
How would you rate which of the trained models is the best?

## Activity 10
How would you explain the result of your model? Is it possible to know which variables are most important?

## Activity 11
How would you assess the financial impact of the proposed model?

## Activity 12
What techniques would you use to perform the hyperparameter optimization of the chosen model?  

## Activity 13
What risks or precautions would you present to the customer before putting this model into production?

## Activity 14
If your predictive model is approved, how would you put it into production?
    
## Activity 15
If the model is in production, how would you monitor it?
    
## Activity 16
If the model is in production, how would you know when to retrain it?
    