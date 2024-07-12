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

### Understanding the problem

### Data Cleaning
As previously mentioned, the data had issues with missing values, which we needed to filter out. In the database, missing values were represented as the string "na". We converted these to Python's `NaN` value using the `.replace()` method of the DataFrame object.

Another concern was columns containing a large number of zeros. While zeros are valid data, an abundance of them (or any constant value) doesn't provide useful information. Therefore, we converted the zeros and removed columns that were mostly zeros or `NaN` values. This process reduced the number of columns from 171 to 108. For this purpose, we created a function named `isRemovable()` to check if a column predominantly contains bad data.

At this point, we used `.dropna()` to eliminate all rows with `NaN` values, which left us with approximately one-third of the total rows.

### Dimensionality reduction
What it has been done till now, is already a dimentionality reduction, but is one we can't avoid because bad data is worst that noise in machine learning science. On this stage, we're going to remove columns that can be considerer dispensables, that, based on a condition we'll be analyzing soon.


### Testing some machine learning algorithms

### Choosing a machine learning model

### Presenting the results

### Deploying the machine

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
    