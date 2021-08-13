# Heart-Disease-Prediction

# About the Project
This is a machine learning model that is used to predict if a person has a heart disease or not. In this project, I have tried 3 models which are Random Forest Classification, Support Vector Machines and Logistic Resgression and I have chosen the best model among them based on the AUC Score, Precision,Recall and F1 score and the model which had the best scores was Random Forest Classification.

# Demo and Screenshots of the App

The app can be checked out on the link given below:
https://hd-prediction.herokuapp.com/
Note : It may take a few seconds for the web app to open.

Here are a few screenshots of the app :

![Main](https://user-images.githubusercontent.com/66258607/113314146-9bb1e000-9329-11eb-935f-1a57fced0fec.PNG)

![Some](https://user-images.githubusercontent.com/66258607/113314283-c9972480-9329-11eb-9ca8-c2ae29bbe1cd.PNG)

![Predict Page](https://user-images.githubusercontent.com/66258607/113314651-27c40780-932a-11eb-8584-847ce1e34d5e.PNG)

# Deployment on Heroku

Before deploying, login to Heroku and create a new app. Once done, you can either connect your GitHub profile and select deploy the branch or use Heroku CLI to deploy the project. It can also be deployed manually as well.

# Workflow

# Data Preprocessing
- The missing values in the data were handled by either using  mean or mode values.
- The imbalance of the dataset was handled by using SMOTE.
- Feature Selection wasn't really done but correlation of all the features was checked and the education feature was negatively corealting to the target variable and was hence removed.
- The data exploration and visualization has been done in detail in a seperate notebook called Heart Disease Prediction(EDA).
- Hyperparameter Tuning was done for both Random Forest Clasiifier and SVM models to get the best results out of them.

# Tools Used
- Front End : HTML and Bootstrap
- Back End : Flask
- IDE : Jupyter Notebook

# Future Scope
Further, the model can be improved if hyperparameter tuning is done with more hyperparameters. Since my laptop is a bit slow, I have used only a few hyperparameters.
