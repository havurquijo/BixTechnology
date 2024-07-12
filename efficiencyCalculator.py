import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def financialImpact():
    previous_years_years =np.arange(2016,2021,1).reshape(-1,1)
    previous_years_expenses = np.asarray([24*1e4,26*1e4,29*1e4,32*1e4,37*1e4]).reshape(-1,1)
    linearRegression = LinearRegression()
    linearRegression.fit(previous_years_years,previous_years_expenses)
    coefs = linearRegression.coef_
    x=np.arange(2016,2023,1).reshape(-1,1)
    y = linearRegression.predict(x)
    plt.figure(figsize=(10,8))
    plt.title("Maintanence expenses in air system and its estimative for year 2022",fontsize=18)
    plt.plot(previous_years_years,previous_years_expenses,'ok',markersize=10)
    plt.bar(np.append(previous_years_years,x[-1]),np.append(previous_years_expenses,y[-1]),width=0.6,color="green",alpha=0.5)
    plt.plot(x,y,'--r',linewidth=1.8)
    plt.plot(x[-1],y[-1],'or',markersize=10)
    plt.ylabel("Cost in dollars ($)",fontsize=18)
    plt.xlabel("Years",fontsize=18)
    plt.legend(["Known cost in previous years","Expenses tendency","Expected cost in 2022"],fontsize=12)
    plt.savefig("financial_impact.png")
    plt.show()
    plt.figure(figsize=(10,8))
    plt.title("Maintanence expenses in air system and its estimative for year 2022",fontsize=18)
    plt.plot(previous_years_years,previous_years_expenses,'ok',markersize=10)
    plt.bar(np.append(previous_years_years,x[-1]),np.append(previous_years_expenses,y[-1]),width=0.6,color="green",alpha=0.5)
    plt.plot(x,y,'--r',linewidth=1.8)
    plt.plot(x[-1],y[-1],'or',markersize=10)
    plt.plot([2022],[16434],'ob',markersize=10)
    plt.bar([2022],[16434],width=0.4,color="blue",alpha=0.6)
    plt.ylabel("Cost in dollars ($)",fontsize=18)
    plt.xlabel("Years",fontsize=18)
    plt.legend(["Known cost in previous years","Expenses tendency","Expected cost in 2022","Predicted expenses using ML"],fontsize=12)
    plt.savefig("financial_impact_ML.png")
    plt.show()

def modelComparision():
    mcc_NB = [0.30547499059677724,0.3328558545756571,0.34573229841249564]
    f2_NB = [0.38934426229508196,0.41589648798521256,0.4343629343629344]
    weigthed_NB = [19.38317757009346,14.028037383177569,13.598130841121495]

    mcc_DTC = [0.5516334740586822,0.4679504872106558,0.42958727053546203]
    f2_DTC = [0.5447470817120622,0.4770992366412214,0.40160642570281124]
    weigthed_DTC = [24.130841121495326,26.94392523364486,31.233644859813083]

    mcc_LR = [0.5013971978505218,0.4021704503460155,0.2859146595680097]
    f2_LR = [0.5019305019305019,0.30303030303030304,0.21645021645021645]
    weigthed_LR = [25.981308411214954,36.33644859813084,39.96261682242991]

    mcc_RF = [0.4790746172284624,0.3338616205944314]
    f2_RF = [0.2727272727272727,0.2222222222222222]
    weigthed_RF = [37.94392523364486,39.850467289719624]

    features_name=["41 features", "15 features", "11 features"]
    models_name = ["Naive Bayes","Logistic Regression","Decision Tree Classifier", "Random Forest"]
    plt.figure(figsize=(10,10))
    plt.suptitle("ML's performance for different scores metrics")
    plt.subplot(2,2,1)
    plt.plot(features_name,mcc_NB,'o-')
    plt.plot(features_name,mcc_LR,'o-')
    plt.plot(features_name,mcc_DTC,'o-')
    plt.plot(features_name[1:],mcc_RF,'o-')
    plt.legend(models_name)
    plt.title("Matthews correlation coefficient")
    plt.subplot(2,2,2)
    plt.plot(features_name,f2_NB,'o-')
    plt.plot(features_name,f2_LR,'o-')
    plt.plot(features_name,f2_DTC,'o-')
    plt.plot(features_name[1:],f2_RF,'o-')
    plt.legend(models_name)
    plt.title("F2-Score")
    plt.subplot(2,2,3)
    plt.plot(features_name,weigthed_NB,'o-')
    plt.plot(features_name,weigthed_LR,'o-')
    plt.plot(features_name,weigthed_DTC,'o-')
    plt.plot(features_name[1:],weigthed_RF,'o-')
    plt.legend(models_name)
    plt.title("Weigthed Score")
    plt.savefig("metrics_comparision.png")
    plt.show()